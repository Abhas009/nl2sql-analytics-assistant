import sqlglot
from sqlglot.errors import ParseError

BLOCKED = {'insert', 'update', 'delete', 'drop', 'truncate', 'alter', 'create', 'merge'}

def validate_sql(sql: str) -> str:
    sql = sql.replace('`sql', '').replace('`', '').strip()
    try:
        parsed = sqlglot.parse(sql, read='duckdb')
    except ParseError as e:
        raise ValueError(f'SQL parse error: {e}')
        
    if len(parsed) != 1:
        raise ValueError('Only a single statement is allowed')
        
    node = parsed[0]
    if node.key != 'select':
        raise ValueError('Only SELECT statements are allowed')
        
    lowered = sql.lower()
    for kw in BLOCKED:
        if f' {kw} ' in f' {lowered} ':
            raise ValueError(f'Blocked keyword: {kw}')
    return sql
