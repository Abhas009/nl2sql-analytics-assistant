import os
import duckdb
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.nl2sql import nl_to_sql, summarize

app = FastAPI(title='NL2SQL Analytics Assistant')

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql: str
    rows: list[dict]
    summary: str

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/query', response_model=QueryResponse)
def query(req: QueryRequest):
    try:
        # 1. Translate to SQL
        sql = nl_to_sql(req.question)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 2. Execute SQL on DuckDB
    try:
        conn = duckdb.connect('nl2sql.duckdb', read_only=True)
        result = conn.execute(sql).fetchdf()
        rows = result.to_dict(orient='records')
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Database error: {str(e)}')

    # 3. Summarize results
    summary = summarize(req.question, rows)
    
    return QueryResponse(sql=sql, rows=rows, summary=summary)
