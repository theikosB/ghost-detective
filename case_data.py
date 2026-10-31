
CASE = {
    "title": "The Clockmaker's Last Hour",
    "case_id": "001",
    "location": "Blackthorn Manor",
    "victim": "Elias Voss",
    "stolen_object": "The Nocturne Prototype",

    "intro": """
Blackthorn Manor has a reputation.

For decades, residents have reported footsteps in
empty corridors, doors opening without explanation,
and a clock that chimes at hours when it should be still.

Some call it superstition. Others refuse to sleep alone.

Tonight, something more tangible has happened.

The Nocturne Prototype, Elias Voss's most valuable
clockwork invention, has vanished from his locked study.

The windows are latched. The study door was locked.
And several people insist they saw something in the hall.

You are Detective Rowan Hale. You do not believe in ghosts.

Your task is to find the thief, reconstruct what happened,
and decide what to make of the strange events at Blackthorn.

The house may be haunted. The evidence must speak for itself.
""",

    "detective": {
        "name": "Rowan Hale",
        "belief": "Sceptical",
        "description": (
            "A methodical detective who trusts physical evidence "
            "and human motives. Rowan initially dismisses "
            "supernatural explanations, but records every "
            "unusual event rather than ignoring it."
        ),
    },

    "suspects": {
        "Mara Voss": {
            "role": "Apprentice",
            "attitude_to_ghost": "Frightened",
            "motive": (
                "Mara secretly copied parts of Elias's designs "
                "and fears he will expose her."
            ),
            "statement": (
                "I was in the kitchen after eleven. I heard "
                "footsteps upstairs, but nobody was there "
                "when I looked."
            ),
            "personality": (
                "Nervous, defensive, and genuinely unsettled "
                "by the house's reputation."
            ),
        },

        "Silas Reed": {
            "role": "Business partner",
            "attitude_to_ghost": "Opportunistic",
            "motive": (
                "Silas has serious debts and hoped to sell "
                "the prototype to a private collector."
            ),
            "statement": (
                "I left before half past eleven. If a ghost "
                "stole the clock, perhaps you should question it."
            ),
            "personality": (
                "Charming, evasive, and quick to turn "
                "uncomfortable questions into jokes."
            ),
        },

        "Iris Bell": {
            "role": "Neighbour",
            "attitude_to_ghost": "Believer",
            "motive": (
                "Iris believes Elias used an invention of hers "
                "without credit, though she has no established "
                "connection to the theft."
            ),
            "statement": (
                "I heard the hall clock chime at 11:47. "
                "Then I saw a shadow pass the study door. "
                "I know what I saw."
            ),
            "personality": (
                "Solemn, observant, and convinced that "
                "Blackthorn Manor is haunted."
            ),
        },
    },

    "timeline": [
        {
            "time": "10:50 PM",
            "event": (
                "Elias records the Nocturne Prototype's "
                "final calibration in his workshop ledger."
            ),
            "type": "fact",
        },
        {
            "time": "11:10 PM",
            "event": (
                "Elias and Silas argue about the proposed "
                "sale of the prototype."
            ),
            "type": "witness_report",
        },
        {
            "time": "11:20 PM",
            "event": (
                "Silas claims he leaves the manor."
            ),
            "type": "claim",
        },
        {
            "time": "11:30 PM",
            "event": (
                "Mara says she is in the kitchen."
            ),
            "type": "claim",
        },
        {
            "time": "11:47 PM",
            "event": (
                "The hall clock chimes. Iris reports seeing "
                "a shadow near the study."
            ),
            "type": "witness_report",
        },
        {
            "time": "11:55 PM",
            "event": (
                "The missing prototype is discovered."
            ),
            "type": "fact",
        },
    ],

    "clues": [
        {
            "id": 1,
            "name": "The Maintenance Ledger",
            "description": (
                "A diagram reveals a narrow service passage "
                "behind the grandfather clock. A note records "
                "that Elias and his apprentice were taught "
                "how to operate its mechanism."
            ),
            "category": "Physical Evidence",
        },
        {
            "id": 2,
            "name": "The Empty Key Hook",
            "description": (
                "The service-passage key is missing from its "
                "usual hook. A clean outline in the dust "
                "suggests it was removed recently, although "
                "the key's last user is unknown."
            ),
            "category": "Physical Evidence",
        },
        {
            "id": 3,
            "name": "The Brass Dust",
            "description": (
                "Fine brass dust lies beneath the workbench and "
                "continues into the service passage behind the "
                "grandfather clock. A matching trail ends near "
                "the apprentice's work area. The dust establishes "
                "a possible route for moving the prototype, but "
                "does not identify who carried it."
            ),
            "category": "Physical Evidence",
        },
        {
            "id": 4,
            "name": "The Scheduled Chime",
            "description": (
                "The hall clock can chime automatically. "
                "Its 11:47 chime does not prove that anyone "
                "was in the study at that exact moment."
            ),
            "category": "Technical Evidence",
        },
        {
            "id": 5,
            "name": "The Unsent Letter",
            "description": (
                "Elias wrote that someone had copied his "
                "prototype designs. He planned to confront "
                "the person after completing the calibration."
            ),
            "category": "Document",
        },
        {
            "id": 6,
            "name": "The Apprentice's Notebook",
            "description": (
                "A notebook contains a sketch resembling "
                "a distinctive gear arrangement in the "
                "prototype. The sketch bears the initials M.V."
            ),
            "category": "Document",
        },
        {
            "id": 7,
            "name": "The Torn Cuff",
            "description": (
                "A torn piece of dark fabric is caught on a sharp "
                "edge inside the service passage. Mara's work "
                "jacket has a fresh tear at the cuff, but the "
                "fabric has not yet been tested to confirm a match. "
                "This is a lead, not proof of identity."
            ),
            "category": "Physical Evidence",
        },
    ],

    "hauntings": [
        {
            "id": 1,
            "name": "Footsteps Above",
            "description": (
                "Footsteps cross the upstairs landing, "
                "although no one is visible there."
            ),
            "reported_by": "Mara Voss",
            "status": "Unverified",
        },
        {
            "id": 2,
            "name": "The Shadow",
            "description": (
                "Iris reports a human-shaped shadow passing "
                "the study door shortly after the hall clock "
                "chimes. No second witness confirms it."
            ),
            "reported_by": "Iris Bell",
            "status": "Unverified",
        },
        {
            "id": 3,
            "name": "The Moving Key",
            "description": (
                "The service-passage key appears on its hook "
                "after having been reported missing. Nobody "
                "admits returning it."
            ),
            "reported_by": "House staff",
            "status": "Unverified",
        },
    ],

    "hints": [
        (
            "Begin with what can be physically established. "
            "A witness's certainty is not the same as proof."
        ),
        (
            "The service passage, the brass dust, and the "
            "copied design may connect the theft to someone "
            "who knew the workshop."
        ),
        (
            "Mara had access to the passage and a possible "
            "motive. The chime and shadow do not establish "
            "who stole the prototype."
        ),
    ],

    "solution": {
        "culprit": "Mara Voss",
        "motive": (
            "Mara feared that Elias would expose her copying "
            "of the prototype design."
        ),
        "method": (
            "The intended theory is that Mara used her "
            "knowledge of the service passage to remove "
            "the prototype. The scheduled chime confused "
            "the apparent timeline."
        ),
        "explanation": (
            "The maintenance ledger establishes that a "
            "service passage exists and that Mara knew "
            "how to operate it. The missing key and brass "
            "dust support the possibility that the passage "
            "was used. The notebook links Mara to a copied "
            "design, providing a possible motive. The "
            "scheduled chime weakens the assumption that "
            "the theft occurred at exactly 11:47 PM. "
            "These clues point toward Mara, but the "
            "current evidence does not conclusively prove "
            "every step of the theft."
        ),
    },
}
