# Contributing

Use the Python version in the Dockerfile. From the repository root, set up
a virtual environment and run the tests.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

To try the app locally, run `python -m flask --app app.app run --port 8080`.
Open `http://localhost:8080/`.

Open a pull request with a short description of the change and how you tested it.
For deployment changes, describe what changed in `deploy/` and how you verified it.
