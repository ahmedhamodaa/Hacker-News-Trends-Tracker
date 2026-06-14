# Hacker News Trends Tracker

Data pipeline that fetches Hacker News stories and stores them in PostgreSQL for trend analysis.

## What it does

- Fetches top 50 stories from Hacker News API
- Stores them in a PostgreSQL database
- Allows SQL queries to analyze trends, scores, and authors

## Tech Stack

- Python
- PostgreSQL
- psycopg2
- requests

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create the database:
   createdb hn_tracker

3. Create the table:
   psql hn_tracker -c "CREATE TABLE stories (
   id BIGINT PRIMARY KEY,
   title TEXT,
   link TEXT,
   score INTEGER,
   author TEXT,
   fetched_at TIMESTAMP DEFAULT NOW()
   );"

4. Run the script:
   python3 hn_tracker.py

## Example Queries

-- Top stories by score
SELECT title, score FROM stories ORDER BY score DESC LIMIT 10;

-- Most active authors
SELECT author, COUNT(\*) as stories, AVG(score) as avg_score
FROM stories
GROUP BY author
ORDER BY avg_score DESC
LIMIT 10;
