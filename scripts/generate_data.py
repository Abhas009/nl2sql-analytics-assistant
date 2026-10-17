import duckdb
import pandas as pd
import random
from datetime import datetime, timedelta

# Create fake data
repos = ['apache/spark', 'facebook/react', 'tensorflow/tensorflow', 'langchain-ai/langchain', 'dbt-labs/dbt-core']
users = ['user_1', 'user_2', 'dev_alice', 'data_bob', 'coder_charlie']
events = []

for _ in range(10000):
    events.append({
        'event_id': random.randint(100000, 999999),
        'event_type': random.choice(['PushEvent', 'PullRequestEvent', 'IssueCommentEvent']),
        'actor_login': random.choice(users),
        'repo_name': random.choice(repos),
        'created_at': datetime.now() - timedelta(days=random.randint(0, 30))
    })

df = pd.DataFrame(events)

# Save to DuckDB (Corrected path)
conn = duckdb.connect('nl2sql.duckdb')
conn.execute('CREATE OR REPLACE TABLE raw_github_events AS SELECT * FROM df')
conn.close()
print('Successfully created local database and loaded 10,000 rows!')
