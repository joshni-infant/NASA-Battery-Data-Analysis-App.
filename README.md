# NASA Battery Data Analysis App

Lightweight Streamlit app for visualizing and analysing NASA battery cycling data.

## What this repo contains

- `app/` — Streamlit entrypoint (`app/main.py`).
- `data/` — dataset CSVs and `metadata.csv` (small metadata file is tracked).
- `src/` — application modules: chart creation, KPI calculations, tabs content, notebooks.
- `venv/` — optional local virtual environment (ignored by git).

## Quick start (Windows PowerShell)

Prerequisites:

- Python 3.8+ installed.
- Git (optional).

Steps:

1. Clone the repo (if not already):

```powershell
git clone <your-repo-url>
cd NASA_BatteryDataAnalysisApp
```

2. (Recommended) Create a virtual environment and activate it:

```powershell
python -m venv venv
; .\venv\Scripts\Activate.ps1
```

3. Install dependencies (create `requirements.txt` if you want to pin versions):

```powershell
pip install --upgrade pip
pip install streamlit pandas matplotlib plotly
```

4. Run the Streamlit app from the repository root:

```powershell
# Run using the venv python module
python -m streamlit run app\main.py

# Or if venv is active and `streamlit` is on PATH
streamlit run app\main.py
```

Notes:
- If you see launcher errors referencing another venv, run Streamlit with `python -m streamlit run ...` to bypass a broken `streamlit.exe`.
- The app expects `data/metadata.csv` and `data/files/*.csv` to be present. `data/metadata.csv` is tracked; large `data/files/` are ignored by default.

## Minimal architecture / file structure

Top-level layout (important files only):

- app/
  - main.py            # Streamlit entrypoint, creates tabs and calls `src.tabs_content`
- src/
  - tabs_content.py    # UI tab render functions (tab1_render, tab2_render, tab3_render)
  - charts_creation.py # Chart helper functions returning Plotly/matplotlib figures
  - kpi_calculations.py# Functions to compute capacity, etc.
- data/
  - metadata.csv       # tracked small metadata file
  - files/             # raw cycle CSVs (ignored by git)

Flow (very small):

main.py -> src.tabs_content.tab*_render -> src.charts_creation / src.kpi_calculations -> display

## Development tips

- Keep the virtual environment out of git (root `.gitignore` already configured).
- If you add or change dependencies, add a `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

- To debug Streamlit launcher issues, use `python -m streamlit run app\main.py`.

## Next steps (optional)

- Add `requirements.txt` with pinned versions.
- Add simple unit tests for `kpi_calculations.py` and run with pytest.
- Add a CI job to run linting/tests.

-ssss

## Docker / Containerization

You can run this app inside a Docker container to make deployments easier and reproducible.

Build and run locally with Docker:

```powershell
# build the image (tag with your repo name)
docker build -t nasa-battery-app:latest .

# run it locally and open http://localhost:8501
docker run -p 8501:8501 nasa-battery-app:latest
```

Or use docker-compose for development (binds the project directory so live edits are reflected):

```powershell
docker-compose up --build
```

Docker tips:
- `.dockerignore` contains common things you don't want placed in the image (venv, data, git metadata).
- Use the `requirements.txt` — if you change dependencies, update it and rebuild the image.

Deploying to a host (short guide):

1. Docker Hub + a cloud runner (Render, Fly.io, AWS ECS, Azure App Service etc.)

```powershell
# tag and push to your Docker Hub repo
docker tag nasa-battery-app:latest <your-hub-username>/nasa-battery-app:latest
docker push <your-hub-username>/nasa-battery-app:latest
```

2. Create a new Web Service on Render or Fly.io and point it to your Docker image on DockerHub (or build from GitHub).

- Render can use `Dockerfile` auto-build from the repo; set port 8501 as the instance's port.
- Fly.io supports `fly launch` and deploys using Docker.

If you want I can add a `Dockerfile.prod` tuned for production, GitHub Actions workflow to build and push images, or a quick step-by-step for Render — which do you prefer?