import urllib.request
import json

API_KEY = "your_api_key_here"
BASE_URL = "https://newsapi.org/v2/top-headlines"

CATEGORIES = {
    "1": "business",
    "2": "entertainment",
    "3": "health",
    "4": "science",
    "5": "sports",
    "6": "technology",
    "7": "general"
}

def get_headlines(category):
    url = f"{BASE_URL}?category={category}&country=us&pageSize=10&apiKey={API_KEY}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data.get("articles", [])
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []

def show_headlines(articles):
    if not articles:
        print("\n📰 No headlines found!\n")
        return
    print("\n📰 Top Headlines:\n")
    for i, article in enumerate(articles, 1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown")
        print(f"  {i}. {title}")
        print(f"     — {source}\n")

def main():
    print("📰 Welcome to News Headlines!")

    while True:
        print("Pick a category:")
        for key, value in CATEGORIES.items():
            print(f"  {key} - {value.title()}")
        print("  8 - Quit")

        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "8":
            print("👋 Stay informed!")
            break
        elif choice in CATEGORIES:
            print(f"\n⏳ Fetching {CATEGORIES[choice].title()} headlines...")
            articles = get_headlines(CATEGORIES[choice])
            show_headlines(articles)

            detail = input("Enter a headline number to see more detail (or press Enter to skip): ").strip()
            if detail.isdigit():
                num = int(detail)
                if 1 <= num <= len(articles):
                    article = articles[num - 1]
                    print(f"\n📌 {article.get('title')}")
                    print(f"🔗 {article.get('url')}")
                    print(f"📝 {article.get('description', 'No description available.')}\n")
        else:
            print("❌ Please enter 1–8.\n")

main()

