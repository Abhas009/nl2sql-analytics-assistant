# 📊 NL2SQL Analytics Assistant

An end-to-end AI Data Engineering project that translates natural language into SQL, executes it against a local data warehouse, and summarizes the results.

## 🏗️ Architecture
1. **Data Layer**: `dbt` transforms raw event data into a dimensional model inside a local `DuckDB` database.
2. **Backend API**: `FastAPI` receives a plain-English question, uses `LangChain` + `Google Gemini` to generate SQL, validates the SQL (to prevent DDL/DML injection), queries DuckDB, and returns the data.
3. **Frontend**: `Streamlit` provides a clean UI to ask questions and view results.

## 🛠️ Tech Stack
- **Data Warehouse**: DuckDB
- **Transformations**: dbt (data build tool)
- **LLM / AI**: Google Gemini, LangChain
- **Backend**: Python, FastAPI, SQLGlot (for SQL validation)
- **Frontend**: Streamlit

## 🚀 How to Run Locally
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt

   Generate the local data:

bash
python scripts/generate_data.py
Build the dbt models:

bash
cd dbt && dbt run --profiles-dir . && cd ..
Add your Gemini API key to a .env file:

env
GEMINI_API_KEY=your_key_here
Start the FastAPI backend:

bash
uvicorn app.main:app --reload
Start the Streamlit frontend (in a new terminal):

bash
streamlit run ui.py
text

### Step 3: Save and Push
1. Save the file in Notepad (`Ctrl + S`) and close Notepad.
2. Go back to your terminal and run:
```powershell
git add README.md
git commit -m "docs: fix README formatting"
git push origin main

