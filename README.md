# 📊 NL2SQL Analytics Assistant

An end-to-end AI data engineering project that translates natural language questions into SQL, executes queries against a local data warehouse, and summarizes the results.

## 🏗️ Architecture

1. **Data Layer:** Uses `dbt` to transform raw event data into a dimensional model stored in a local `DuckDB` database.
2. **Backend API:** Uses `FastAPI` to receive natural language questions. `LangChain` and Google Gemini generate SQL, while `SQLGlot` validates the query before execution against DuckDB.
3. **Frontend:** Uses `Streamlit` to provide an interactive interface for asking questions and viewing query results.

## 🛠️ Tech Stack

- **Data Warehouse:** DuckDB
- **Transformations:** dbt (data build tool)
- **LLM / AI:** Google Gemini, LangChain
- **Backend:** Python, FastAPI
- **SQL Validation:** SQLGlot
- **Frontend:** Streamlit

## 📋 Prerequisites

Before getting started, ensure you have:

- Python installed
- A Google Gemini API key
- Git installed
- The required project dependencies listed in `requirements.txt`

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the Local Data

Run the data generation script from the project root:

```bash
python scripts/generate_data.py
```

### 4. Build the dbt Models

Run the following commands from the project root:

```bash
cd dbt
dbt run --profiles-dir .
cd ..
```

This executes the dbt models and builds the transformed datasets in DuckDB.

### 5. Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Ensure the application loads environment variables from this file and uses the variable name expected by your code.

**Security:** Never commit your `.env` file or expose your API key in a public repository.

### 6. Start the FastAPI Backend

From the project root, run:

```bash
uvicorn app.main:app --reload
```

The API will start locally. Check the terminal for the server URL.

### 7. Start the Streamlit Frontend

Open a new terminal, navigate to the project root, and run:

```bash
streamlit run ui.py
```

Open the local URL displayed in the terminal to interact with the application.

## 🔒 Security Considerations

- Validate generated SQL before execution.
- Restrict queries to read-only operations, such as `SELECT`, where appropriate.
- Reject DDL and DML statements, including `DROP`, `DELETE`, `UPDATE`, and `INSERT`.
- Use parameterized queries for user-supplied values wherever applicable.
- Apply query timeouts and resource limits where appropriate.
- Never expose API keys or other secrets in source code or Git commits.

**Note:** SQLGlot-based validation is one layer of defense, not a complete security boundary. Enforce read-only database access and validate the parsed query structure before execution.

## 📌 Project Goals

- Convert natural language questions into SQL queries.
- Automate data retrieval from a local analytical warehouse.
- Transform raw data into dimensional models using dbt.
- Provide an interactive analytics interface.
- Generate understandable summaries of query results using AI.

## 🐙 Save and Push to GitHub

After saving your changes to `README.md`, run the following commands in PowerShell from your repository directory:

```powershell
git add README.md
git commit -m "docs: fix README formatting"
git push origin main
```

If Git reports that there is nothing to commit, the changes may already be committed. If your branch is not `main`, replace `main` with your current branch name.

