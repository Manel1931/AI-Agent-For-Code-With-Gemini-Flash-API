# AI Agent For Code (with Gemini Flash API)

This repository contains a small AI coding agent that uses Google's Gemini (Flash) API to analyze and modify code in a workspace. The agent can list files, read and write files, and run Python files via function calls.

Key features
- Uses the Google Gemini (Flash) model via the `google-genai` client
- Provides helper functions to inspect and modify project files
- Example project included (`calculator/`) and small tooling in `functions/`

Status
- Minimal proof-of-concept. Not production hardened.

Prerequisites
- Python 3.9+ (virtual environment recommended)
- A Gemini API key (GEMINI_API_KEY) with access to the GenAI APIs

Security note (important)
- Do NOT commit API keys or service-account JSON to the repository. This project previously had an API key in a local `.env` file. Before publishing this repo to GitHub, remove any secrets and rotate keys if they were accidentally exposed.
- Use environment variables or a secret manager instead. See the "Environment" section below.

Quick start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies. This project uses a standard Python layout; if you maintain a `requirements.txt` add it and then run:

```bash
# If you have requirements.txt
pip install -r requirements.txt

# OR install from pyproject.toml with pip (if applicable)
pip install -e .
```

3. Set your Gemini API key as an environment variable. Create a `.env` file (not tracked) or export directly.

Example `.env` (DO NOT commit this file):

```
GEMINI_API_KEY=your-real-gemini-api-key-here
```

Or export in your shell (macOS/Linux):

```bash
export GEMINI_API_KEY="your-real-gemini-api-key-here"
```

4. Run the agent with a prompt. The `main.py` script expects a prompt argument.

```bash
python main.py "Find TODOs and suggest improvements for the calculator package" --verbose
```

How it works (high level)
- `main.py` loads the environment with `load_dotenv()` and then reads `GEMINI_API_KEY`.
- It creates a `genai.Client(api_key=...)` and calls `client.models.generate_content(...)` with the model configured in the script (e.g. `gemini-2.5-flash` / `gemini-2.0-flash-001`).
- The agent is configured to call local helper functions defined in `functions/` to list files, read file contents, write files, or run python files.

Repository layout

- `main.py` — entrypoint that wires the Gemini client and agent loop
- `config.py` — simple project configuration (e.g. `MAX_CHARS`)
- `functions/` — helper function handlers exposed to the agent (read/write/list/run)
- `calculator/` — example subproject with a small calculator package and tests
- `call_function.py` — dispatcher used by the agent to call local functions
- `.env` — local environment variables (may contain `GEMINI_API_KEY` during development; DO NOT commit)

Usage examples

- Run with a short prompt:

```bash
python main.py "Refactor the calculator to add logging" 
```

- Run tests in the `calculator/` package (if a test runner is present):

```bash
python -m pytest calculator/tests.py
```

Recommended next steps before publishing to GitHub

1. Remove any `.env` file that contains keys and add `.env` to `.gitignore`.
2. Rotate any keys that may have been committed or exposed.
3. Add a small `requirements.txt` or complete `pyproject.toml` with pinned versions.
4. Add a LICENSE (MIT is a permissive default) and CONTRIBUTING.md if you want collaborators.

Contact / Attribution

If you'd like help improving the README or adding CI, tests, or example workflows, open an issue or request in the repo.

