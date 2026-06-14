import requests
import psycopg2

# Connect to database
conn = psycopg2.connect(
    dbname="hn_tracker",
    user="ahmedelsayed",
    host="localhost"
)
cur = conn.cursor()

# Fetch stories
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
story_ids = response.json()[:10]

for story_id in story_ids:
    story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
    
    title = story.get("title")
    link = story.get("url", "")
    score = story.get("score", 0)
    author = story.get("by", "")

    cur.execute("""
        INSERT INTO stories (id, title, link, score, author)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (story_id, title, link, score, author))
    
    print(f"Saved: {title} — {score} points")

conn.commit()
cur.close()
conn.close()