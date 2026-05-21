# Log Classifier

Project that classifies log messages using multiple processors: BERT-based embeddings, regex rules, a logistic regression model, and an LLM-backed processor.

**Purpose:** provide a small pipeline to experiment with hybrid log classification methods and evaluate results on CSV test data.

**Folder structure**
- `server.py`: FastAPI backend server for log classification.
- `classify.py`: Core classification function called by the server.
- `processor_bert.py`: BERT-based embedding classifier.
- `processor_llm.py`: LLM-based processor wrapper.
- `processor_regex.py`: Regex-based rules processor.
- `model.joblib`: Trained logistic regression (or other sklearn) model artifact.
- `requirements.txt`: Python dependencies.
- `synthetic_logs.csv`: Example synthetic logs for development.
- `test.csv`: Sample test set used for quick evaluation.
- `output.csv`: Output file produced by classification runs.
- `Log_classifier.ipynb`: Notebook with experiments and analysis.

**Quickstart — setup**
- Create a Python 3.8+ virtual environment and activate it.

	Windows (PowerShell):

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	```

	macOS / Linux:

	```bash
	python -m venv .venv
	source .venv/bin/activate
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	```

**Usage**

**Running the FastAPI Server**

Start the backend server:

```bash
uvicorn server:app --reload
```

The server will be available at `http://localhost:8000`. 

**Classification API Endpoint**

- **Endpoint:** `POST /classify/`
- **Input:** Upload a CSV file with `source` and `log_message` columns
- **Output:** Returns a CSV file with the added `target_label` column containing classifications

**Example using curl:**

```bash
curl -X POST "http://localhost:8000/classify/" -F "file=@test.csv"
```

**Example using Python:**

```python
import requests

with open("test.csv", "rb") as f:
    response = requests.post("http://localhost:8000/classify/", files={"file": f})
    with open("output.csv", "wb") as out:
        out.write(response.content)
```

**Using the Notebook**

Alternatively open the notebook `Log_classifier.ipynb` to walk through preprocessing, model loading (`model.joblib`), and evaluation steps.

**What each processor does**
- `processor_bert.py`: extract embeddings from a BERT model (or a lightweight transformer), then classify using a downstream model.
- `processor_regex.py`: apply rule-based classification using regular expressions.
- `processor_llm.py`: call an LLM (local or remote) to classify logs where other processors are inconclusive.

**Model artifact**
- `model.joblib` contains the trained sklearn (or compatible) model used by the pipeline. If you want to retrain, add a training script that saves to this path.

**Testing**
- To run a quick test, use `test.csv` as input and inspect `output.csv` for predictions. Adjust scripts accordingly.

**Development notes**
- Keep `requirements.txt` up to date with any new packages you add.
- Store large model artifacts outside of Git or use Git LFS for model binaries.

**How to push these changes to GitHub (example commands)**
- Ensure a remote is configured (replace `origin` URL if needed):

```bash
git remote -v
# if no remote exists, add one:
git remote add origin git@github.com:<your-username>/<your-repo>.git
```

- Create a branch, commit and push (example):

```bash
git checkout -b update-readme
git add README.md
git commit -m "docs: update README with setup and usage"
git push --set-upstream origin update-readme
```

If you want these changes merged into `main`/`master`, open a Pull Request on GitHub after pushing.

**Contributing**
- Feel free to submit issues or PRs. Describe dataset, preprocessing steps and the model training parameters when adding new models.

**License**
- Add a LICENSE file to declare project licensing.

---
If you want, I can also: update `requirements.txt`, add a small `run.sh`/`run.ps1` runner, or commit & push these changes for you.
