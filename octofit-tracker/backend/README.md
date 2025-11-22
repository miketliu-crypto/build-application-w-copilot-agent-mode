# OctoFit Tracker — Backend

This README covers quick steps to activate the backend virtual environment and run the Django project.

Activate the virtualenv (no `cd` required):

```bash
source /workspaces/build-application-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
```

Run Django migrations (no `cd` required):

```bash
python /workspaces/build-application-w-copilot-agent-mode/octofit-tracker/backend/manage.py migrate
```

Run the development server (exposes port `8000`):

```bash
python /workspaces/build-application-w-copilot-agent-mode/octofit-tracker/backend/manage.py runserver 8000
```

Notes:
- The project uses a local virtual environment at `octofit-tracker/backend/venv`.
- Do not change directories when using agent-mode commands; use full paths as shown above.
