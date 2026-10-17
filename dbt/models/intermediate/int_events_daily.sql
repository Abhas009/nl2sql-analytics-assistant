{{ config(materialized='view') }}

select
  event_date,
  event_type,
  repo_name,
  count(*) as event_count,
  count(distinct actor_login) as unique_actors
from {{ ref('stg_github_events') }}
group by 1, 2, 3
