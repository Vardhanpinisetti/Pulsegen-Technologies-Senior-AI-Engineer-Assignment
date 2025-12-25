import pandas as pd

print("Swiggy Review AI Agent started")

file_path = "data/reviews_sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    reviews = file.readlines()

# Group reviews by date
reviews_by_date = {}

for review in reviews:
    date, text = review.strip().split("|")
    date = date.strip()
    text = text.strip().lower()

    if date not in reviews_by_date:
        reviews_by_date[date] = []

    reviews_by_date[date].append(text)

# Topic detection rules
def detect_topic(review_text):
    if "late" in review_text:
        return "Delivery issue"
    elif "rude" in review_text or "behaved badly" in review_text:
        return "Delivery partner rude"
    elif "stale" in review_text or "bad" in review_text:
        return "Food quality issue"
    elif "map" in review_text:
        return "App issue"
    elif "10 minute" in review_text:
        return "Feature request"
    else:
        return "Other"

# Count topic frequency per date
topic_trends = {}

for date, texts in reviews_by_date.items():
    for text in texts:
        topic = detect_topic(text)

        if topic not in topic_trends:
            topic_trends[topic] = {}

        topic_trends[topic][date] = topic_trends[topic].get(date, 0) + 1

# Convert to Pandas DataFrame
df = pd.DataFrame(topic_trends).fillna(0).astype(int).T
df = df.reindex(sorted(df.columns), axis=1)


print("\nFINAL TREND TABLE:\n")
print(df)

# Save output
output_path = "output/topic_trend_table.csv"
df.to_csv(output_path)

print(f"\nTrend table saved to: {output_path}")
