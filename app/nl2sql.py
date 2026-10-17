import os
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from app.schema_context import SCHEMA_CONTEXT
from app.validator import validate_sql

env_path = Path(__file__).resolve().parent.parent / ".env"
api_key = None

if env_path.exists():
    with open(env_path, "r", encoding="utf-8-sig") as f:
        for line in f:
            if "GEMINI_API_KEY=" in line:
                api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break

if not api_key:
    api_key = os.getenv("GEMINI_API_KEY", "").strip().strip('"').strip("'")

llm = ChatGoogleGenerativeAI(
    model='gemini-3.8-flash', 
    temperature=0, 
    api_key=api_key
)

prompt = ChatPromptTemplate.from_messages([
    ('system', 'You translate natural language to SQL. Return ONLY SQL, no markdown, no commentary.\n' + SCHEMA_CONTEXT),
    ('human', '{question}')
])

# HELPER FUNCTION: safely extracts text whether it comes back as a string or a list
def extract_text(response):
    content = response.content
    if isinstance(content, list):
        # Extract text from the first block
        return content[0].get('text', '') if isinstance(content[0], dict) else str(content[0])
    return str(content)

def nl_to_sql(question: str) -> str:
    response = (prompt | llm).invoke({'question': question})
    sql = extract_text(response).strip()
    return validate_sql(sql)

def summarize(question: str, rows: list[dict]) -> str:
    if not rows:
        return 'No data found for this query.'
    preview = rows[:10]
    msg = f'User asked: {question}\nReturned {len(rows)} rows. Preview: {preview}\nSummarize the findings in 1 clear sentence.'
    response = llm.invoke(msg)
    return extract_text(response).strip()
