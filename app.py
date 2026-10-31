
import html
import streamlit as st
from case_data import CASE
from detective import ask_detective
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION AND STATE
# --------------------------------------------------

st.set_page_config(
    page_title="The Ghost Detective",
    page_icon="👻",
    layout="wide",
    initial_sidebar_state="expanded",
)

DEFAULTS = {
    "messages": [],
    "revealed_clues": set(),
    "investigated_hauntings": set(),
    "haunting_encounters": {},
    "field_notes": [],
    "deductions": [],
    "active_haunting": None,
    "hints_used": 0,
    "verdict": False,
    "reveal_solution": False,
    "current_minutes": 22 * 60 + 50,  # 10:50 PM
    "chime_observed": False,
    "focused_suspect": "General investigation",
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy() if isinstance(
            value, (list, set, dict)
        ) else value

def format_game_time(minutes):
    minutes = minutes % (24 * 60)
    hour = minutes // 60
    minute = minutes % 60

    suffix = "AM" if hour < 12 else "PM"
    display_hour = hour % 12 or 12

    return f"{display_hour}:{minute:02d} {suffix}"


def advance_time(minutes):
    old_time = st.session_state.current_minutes
    new_time = old_time + minutes

    chime_time = 23 * 60 + 47

    if (
        old_time < chime_time <= new_time
        and not st.session_state.chime_observed
    ):
        st.session_state.chime_observed = True
        st.session_state.field_notes.append(
            "11:47 PM — The hall clock chimes while Rowan is "
            "investigating. The sound is real; its significance "
            "remains uncertain."
        )

    st.session_state.current_minutes = new_time

# --------------------------------------------------
# DESIGN SYSTEM
# --------------------------------------------------

with st.sidebar:
    st.markdown("## 👻 THE GHOST DETECTIVE")
    st.caption("A mystery at Blackthorn Manor")
    st.divider()

    st.markdown("### Your investigation")
    st.caption("CASE FILE 001")

    st.metric(
    "Time",
    format_game_time(st.session_state.current_minutes),
    )   

    total_clues = len(CASE["clues"])
    found_clues = len(st.session_state.revealed_clues)

    total_hauntings = len(CASE["hauntings"])
    found_hauntings = len(st.session_state.investigated_hauntings)

    st.progress(
        found_clues / total_clues if total_clues else 0,
        text=f"Evidence: {found_clues}/{total_clues}",
    )

    st.progress(
        found_hauntings / total_hauntings if total_hauntings else 0,
        text=f"Unexplained incidents: {found_hauntings}/{total_hauntings}",
    )

    st.metric("Hints used", st.session_state.hints_used)

    st.divider()
    st.caption("Trust the evidence. Question everything.")


css = Path("styles.css").read_text(encoding="utf-8")

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True,
)


# --------------------------------------------------
# CASE FILE HEADER
# --------------------------------------------------

st.markdown(
    '<div class="eyebrow">The Blackthorn Files · No. 001</div>',
    unsafe_allow_html=True,
)

st.title("The Ghost Detective")

st.markdown(
    f"""
    <div class="case-hero">
        <div class="eyebrow">
            ACTIVE CASE &nbsp; / &nbsp;
            {html.escape(CASE["location"])}
        </div>
        <div class="case-title">
            {html.escape(CASE["title"])}
        </div>
        <p>{html.escape(CASE["intro"].strip())}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    "Evidence examined",
    f"{found_clues} / {total_clues}",
)

metric2.metric(
    "Haunting reports",
    f"{found_hauntings} / {total_hauntings}",
)

metric3.metric(
    "Investigation hints",
    st.session_state.hints_used,
)

st.divider()


# --------------------------------------------------
# MAIN INVESTIGATION
# --------------------------------------------------

investigation_col, chat_col = st.columns(
    [1.05, 0.95],
    gap="large",
)

with investigation_col:
    st.markdown("## Casebook")
    st.caption("Examine the evidence. Build your theory.")

    evidence_tab, people_tab, haunting_tab, deductions_tab, notes_tab = st.tabs(
        [
            "🔎 Evidence",
            "🕵️ Suspects",
            "👻 Incidents",
            "🧩 Deductions",
            "📓 Notes",
        ]
    )

    with evidence_tab:
        st.markdown(
            '<div class="section-label">Physical evidence & documents</div>',
            unsafe_allow_html=True,
        )
        st.write("Open an item to examine it and record your findings.")

        for clue in CASE["clues"]:
            clue_id = clue["id"]
            investigated = clue_id in st.session_state.revealed_clues

            status = "✓ Examined" if investigated else "○ Unexamined"

            with st.expander(
                f"{'✓' if investigated else '◇'}  {clue['name']}  ·  {status}"
            ):
                st.caption(
                    f"EVIDENCE {clue_id:02d}  /  {clue['category'].upper()}"
                )
                st.write(clue["description"])

                if investigated:
                    st.success("Recorded in your investigation.")
                elif st.button(
                    "Examine evidence",
                    key=f"clue_{clue_id}",
                    use_container_width=True,
                ):
                    st.session_state.revealed_clues.add(clue_id)

                    note = f"Examined evidence: {clue['name']}"
                    if note not in st.session_state.field_notes:
                        st.session_state.field_notes.append(note)

                    st.rerun()

    with people_tab:
        st.markdown(
            '<div class="section-label">Persons of interest</div>',
            unsafe_allow_html=True,
        )

        suspect_names = list(CASE["suspects"].keys())

        for name, suspect in CASE["suspects"].items():
            with st.container(border=True):
                st.markdown(f"### {name}")
                st.caption(
                    f"{suspect['role']}  ·  "
                    f"{suspect['attitude_to_ghost']} about the haunting"
                )

                st.write(suspect["personality"])

                st.markdown("**Recorded statement**")
                st.write(f"“{suspect['statement']}”")

                if st.button(
                    f"Focus interrogation on {name}",
                    key=f"focus_{name}",
                    use_container_width=True,
                ):
                    st.session_state.focused_suspect = name
                    st.rerun()

        st.caption(
            "A statement is a claim to investigate, not necessarily a fact."
        )

    with haunting_tab:
        st.markdown(
            '<div class="section-label">Unexplained occurrences</div>',
            unsafe_allow_html=True,
        )
        st.write(
            "Investigate each incident. Your choices may reveal "
            "something—or leave you with more questions."
        )

        st.markdown("### The Waiting Hours")

        if not st.session_state.chime_observed:
            current_time = st.session_state.current_minutes
            chime_time = 23 * 60 + 47

            if current_time < chime_time:
                if st.button("Wait until 11:47 PM"):
                    advance_time(chime_time - current_time)
                    st.rerun()

        haunting_choices = {
            1: {
                "Follow the footsteps": (
                    "You follow the sound to the west-wing landing. "
                    "The footsteps stop above a section of floor "
                    "that sounds hollow. You cannot establish what "
                    "made the sound."
                ),
                "Stay still and listen": (
                    "The footsteps repeat in a slow pattern, then "
                    "stop abruptly. You notice the final two steps "
                    "sound closer together. The source remains unknown."
                ),
                "Inspect the ceiling": (
                    "You find no visible opening or fresh damage. "
                    "A narrow service space may run above the landing, "
                    "but you have not established that it was used."
                ),
            },
            2: {
                "Follow the shadow": (
                    "You follow the reported path past the study door. "
                    "The corridor ends at a curtained window. A draft "
                    "moves the curtain, but this does not prove what "
                    "Iris saw."
                ),
                "Inspect the corridor": (
                    "You find no clear footprints or physical trace. "
                    "The polished floor could conceal faint marks, "
                    "so the absence of evidence is inconclusive."
                ),
                "Ask Iris to describe it again": (
                    "Iris insists the shadow moved against the light. "
                    "Her account is consistent, but it remains a "
                    "single-witness report."
                ),
            },
            3: {
                "Watch the key hook": (
                    "You wait beside the hook. The key does not move "
                    "while you watch. You cannot determine who returned "
                    "it or when."
                ),
                "Inspect the hook and dust": (
                    "The dust is disturbed around the hook. The marks "
                    "are too indistinct to identify a hand or establish "
                    "the exact time the key was replaced."
                ),
                "Question the house staff": (
                    "The staff member repeats that the key appeared "
                    "after being reported missing. They did not see "
                    "who returned it."
                ),
            },
        }

        if st.session_state.chime_observed:
            st.warning(
                "🕰️ 11:47 PM — The hall clock chimes. "
                "For a moment, every sound in the manor stops. "
                "You cannot tell whether this is coincidence "
                "or connected to the reports."
            )

        for event in CASE["hauntings"]:
            event_id = event["id"]
            encounter = st.session_state.haunting_encounters.get(event_id)
            investigated = event_id in st.session_state.investigated_hauntings

            status = "✓ Investigated" if investigated else "○ Uninvestigated"

            with st.expander(
                f"👻 {event['name']}  ·  {status}",
                expanded=(
                    st.session_state.active_haunting == event_id
                ),
            ):
                st.write(event["description"])
                st.caption(f"Reported by: {event['reported_by']}")

                if encounter:
                    st.markdown("**Your observation**")
                    st.write(encounter["result"])
                    st.caption(f"Approach: {encounter['choice']}")

                elif not investigated:
                    st.markdown("**How will you investigate?**")

                    choice = st.radio(
                        "Choose your approach",
                        list(haunting_choices[event_id].keys()),
                        key=f"haunting_choice_{event_id}",
                    )

                    if st.button(
                        "Investigate occurrence",
                        key=f"investigate_haunting_{event_id}",
                        use_container_width=True,
                    ):
                        result = haunting_choices[event_id][choice]

                        advance_time(15)

                        st.session_state.haunting_encounters[event_id] = {
                            "choice": choice,
                            "result": result,
                        }

                        st.session_state.investigated_hauntings.add(event_id)
                        st.session_state.active_haunting = event_id

                        note = (
                            f"Haunting investigated — {event['name']}: "
                            f"{result}"
                        )

                        if note not in st.session_state.field_notes:
                            st.session_state.field_notes.append(note)
                            st.session_state.active_haunting = event_id

                        st.rerun()

    with deductions_tab:
        st.markdown(
            '<div class="section-label">Connect the evidence</div>',
            unsafe_allow_html=True,
        )
        st.write(
            "Choose two examined clues and explain how they connect. "
            "A deduction is a theory—not necessarily a proven fact."
        )

        available_clues = [
            clue
            for clue in CASE["clues"]
            if clue["id"] in st.session_state.revealed_clues
        ]

        if len(available_clues) < 2:
            st.info("Examine at least two pieces of evidence to make a deduction.")
        else:
            clue_names = [clue["name"] for clue in available_clues]

            with st.form("deduction_form"):
                clue_one = st.selectbox(
                    "First piece of evidence",
                    clue_names,
                    key="deduction_clue_one",
                )

                clue_two = st.selectbox(
                    "Connect it with",
                    clue_names,
                    index=1,
                    key="deduction_clue_two",
                )

                reasoning = st.text_area(
                    "Your reasoning",
                    placeholder="What do these clues suggest when considered together?",
                    key="deduction_reasoning",
                )

                submitted = st.form_submit_button(
                    "Record deduction",
                    use_container_width=True,
                )

            if submitted:
                if clue_one == clue_two:
                    st.warning("Choose two different clues.")
                elif not reasoning.strip():
                    st.warning("Explain the connection before recording it.")
                else:
                    st.session_state.deductions.append(
                        {
                            "clue_one": clue_one,
                            "clue_two": clue_two,
                            "reasoning": reasoning.strip(),
                        }
                    )

                    st.session_state.field_notes.append(
                        f"Deduction: {clue_one} + {clue_two} — "
                        f"{reasoning.strip()}"
                    )

                    st.rerun()

        if st.session_state.deductions:
            st.markdown("### Your recorded deductions")

            for i, deduction in enumerate(
                st.session_state.deductions,
                start=1,
            ):
                with st.container(border=True):
                    st.markdown(
                        f"**Deduction {i}:** "
                        f"{deduction['clue_one']} + {deduction['clue_two']}"
                    )
                    st.write(deduction["reasoning"])

    with notes_tab:
        st.markdown(
            '<div class="section-label">Detective Rowan Hale’s notebook</div>',
            unsafe_allow_html=True,
        )

        if st.session_state.field_notes:
            for i, note in enumerate(
                st.session_state.field_notes, start=1
            ):
                st.markdown(
                    f"""
                    <div class="note-card">
                        <p><span style="color:#D8B879;">
                        {i:02d} &nbsp; / &nbsp;</span>
                        {html.escape(note)}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info(
                "Your notebook is empty. Examine evidence or investigate "
                "an unexplained occurrence to begin."
            )

        if st.button("Add a personal note", use_container_width=True):
            st.session_state.show_note_input = True

        if st.session_state.get("show_note_input", False):
            with st.form("personal_note_form"):
                personal_note = st.text_area(
                    "Your deduction",
                    placeholder="What do you think happened? Which details matter?",
                )
                save_note = st.form_submit_button("Save to notebook")

                if save_note:
                    if personal_note.strip():
                        st.session_state.field_notes.append(
                            f"Detective's deduction: {personal_note.strip()}"
                        )
                        st.session_state.show_note_input = False
                        st.rerun()
                    else:
                        st.warning("Write a note before saving.")

    st.divider()

    st.markdown("## Need a nudge?")
    st.caption("Hints get more specific as you use them.")

    if st.button("Reveal next hint", use_container_width=True):
        if st.session_state.hints_used < len(CASE["hints"]):
            st.session_state.last_hint = CASE["hints"][
                st.session_state.hints_used
            ]
            st.session_state.hints_used += 1
        else:
            st.session_state.last_hint = (
                "No more hints remain. Revisit the evidence and compare "
                "each suspect's claims with the physical facts."
            )

    if "last_hint" in st.session_state:
        st.info(st.session_state.last_hint)


# --------------------------------------------------
# GEMMA INTERROGATION
# --------------------------------------------------

with chat_col:
    st.markdown("## The interrogation room")
    st.caption("Ask questions. Test theories. Follow contradictions.")

    st.markdown(
        f"""
        <div class="note-card">
            <p><strong>ROWAN HALE'S CASEBOOK</strong></p>
            <p style="color: #C0B8A7;">
                The house has its stories. The evidence has its limits.
                Keep the two separate.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.selectbox(
        "Focus your questioning",
        ["General investigation"] + list(CASE["suspects"].keys()),
        key="focused_suspect",
    )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask about a clue, suspect, or strange occurrence..."
    )

    if question:
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        focused = st.session_state.focused_suspect

        contextual_question = question
        if focused != "General investigation":
            contextual_question = (
                f"The player is focusing on {focused}. "
                f"Their question is: {question}"
            )

        with st.spinner("Reviewing the case files..."):
            try:
                answer = ask_detective(
                    question=contextual_question,
                    case={
                        **CASE,
                        "current_game_time": format_game_time(
                            st.session_state.current_minutes
                        ),
                        "investigated_hauntings": [
                            event["name"]
                            for event in CASE["hauntings"]
                            if event["id"]
                            in st.session_state.investigated_hauntings
                        ],
                        "revealed_clues": [
                            clue["name"]
                            for clue in CASE["clues"]
                            if clue["id"]
                            in st.session_state.revealed_clues
                        ],
                    },
                    api_key=st.secrets["GEMINI_API_KEY"],
                    model_name=st.secrets["GEMMA_MODEL"],
                    history=st.session_state.messages[:-1],
                )
            except Exception:
                answer = (
                    "The connection to the spirit world was interrupted. "
                    "Your investigation is safe. Please try again."
                )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("## Deliver your verdict")
    st.caption("Name your suspect only when you are ready.")

    with st.form("verdict_form"):
        accused = st.selectbox(
            "Who do you believe stole the prototype?",
            list(CASE["suspects"].keys()),
        )

        reasoning = st.text_area(
            "Your reasoning",
            placeholder="Connect the clues, question the timeline, and explain your theory...",
        )

        submit_verdict = st.form_submit_button(
            "Submit final verdict",
            use_container_width=True,
        )

    if submit_verdict:
        st.session_state.verdict = True
        st.session_state.accused = accused
        st.session_state.reasoning = reasoning

    if st.session_state.verdict:
        if st.session_state.accused == CASE["solution"]["culprit"]:
            st.success("Your accusation matches the case solution.")
        else:
            st.warning(
                "That accusation doesn't match the intended solution. "
                "Revisit the evidence before trying again."
            )

        if st.session_state.get("reasoning", "").strip():
            with st.expander("Review your deduction"):
                st.write(st.session_state.reasoning)

        if st.button("Reveal the case solution", use_container_width=True):
            st.session_state.reveal_solution = True

    if st.session_state.reveal_solution:
        solution = CASE["solution"]

        st.markdown("### The truth behind Blackthorn Manor")
        st.write(f"**Responsible:** {solution['culprit']}")
        st.write(f"**Motive:** {solution['motive']}")
        st.write(f"**Method:** {solution['method']}")
        st.write(solution["explanation"])
