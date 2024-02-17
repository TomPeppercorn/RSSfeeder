# RSS Feederizer by Tom Peppercorn (February 14, 2024)

# In the case this needs test input, here
# https://news.ycombinator.com/rss

import feedparser,csv,datetime,timedelta,timezone
# from datetime import datetime,timedelta,timezone

rsslink = input("Welcome to the Peppercorn RSS feed parser.\nPlease insert a valid RSS link.\n")
rssfeed = feedparser.parse(rsslink)

# Define the time range (e.g., the last 24 hours)
now = datetime.now(timezone.utc)
time_range = timedelta(days=1)
# Iterate through entries and filter by the time range
for entry in rssfeed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print(entry.title)
        print(entry.link)
        print(entry.published)
        print(entry.summary)
        print("\n")