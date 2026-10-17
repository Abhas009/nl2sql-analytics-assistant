{{ config(materialized='table') }}

select
  event_date,
  repo_name,
  sum(event_count) as total_events,
  sum(unique_actors) as total_actor_actions
from {{ ref('int_events_daily') }}
group by 1, 2
