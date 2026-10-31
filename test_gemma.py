
import tomllib
from pathlib import Path
from google import genai

# Read the local Streamlit secrets file.
secrets_path = Path(".streamlit/secrets.toml")
secrets = tomllib.loads(secrets_path.read_text(encoding="utf-8"))

api_key = secrets["GEMINI_API_KEY"]
model_name = secrets["GEMMA_MODEL"]

client = genai.Client(api_key=api_key)

print(f"Testing model: {model_name}")

response = client.models.generate_content(
    model=model_name,
    contents="Reply with exactly: The ghost is awake.",
)

print("\nGemma replied:")
print(response.text)
