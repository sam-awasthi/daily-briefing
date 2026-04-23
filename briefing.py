import os
import requests
import anthropic
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def fetch_news():
    queries = [
        "technology news",
        "startup funding venture capital",
        "artificial intelligence",
        "growth marketing GTM",
        "creator economy"
    ]
    
    all_articles = []
    
    for query in queries:
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWSAPI_KEY}"
        response = requests.get(url)
        data = response.json()
        
        if data.get("articles"):
            for article in data["articles"]:
                all_articles.append({
                    "title": article["title"],
                    "description": article["description"],
                    "url": article["url"],
                    "source": article["source"]["name"],
                    "category": query
                })
    
    return all_articles

def generate_briefing(articles):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    articles_text = ""
    for a in articles:
        articles_text += f"Category: {a['category']}\nTitle: {a['title']}\nDescription: {a['description']}\nURL: {a['url']}\nSource: {a['source']}\n\n"
    
    prompt = f"""You are writing a daily news briefing for Sam, a London-based growth and GTM operator, content creator with 400k+ audience, and startup person. Keep the entire briefing under 3500 characters total.

Here are today's articles:

{articles_text}

Write a briefing in this exact format:

☀️ Good morning Sam. Here's what's happening.

[2 sentence TLDR of the single most important thing worth knowing today]

🤖 AI
- [bullet with key insight and link]
- [bullet with key insight and link]

🚀 Startups & VC
- [bullet with key insight and link]
- [bullet with key insight and link]

📈 Growth & GTM
- [bullet with key insight and link]
- [bullet with key insight and link]

🎨 Creator Economy
- [bullet with key insight and link]
- [bullet with key insight and link]

💻 Tech
- [bullet with key insight and link]
- [bullet with key insight and link]

Keep bullets sharp and specific. No waffle. Include the actual URL for each bullet. Skip anything that isn't genuinely interesting or relevant."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    response = requests.post(url, json=payload)
    return response.json()

def run_briefing():
    print("Fetching news...")
    articles = fetch_news()
    print(f"Got {len(articles)} articles. Generating briefing...")
    briefing = generate_briefing(articles)
    print("Sending to Telegram...")
    result = send_telegram(briefing)
    print("Done.", result)

run_briefing()
