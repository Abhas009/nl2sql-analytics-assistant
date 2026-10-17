{{ config(materialized='view') }}

select
  event_id,
  event_type,
  actor_login,
  repo_name,
  created_at,
  cast(created_at as date) as event_date
from raw_github_events
