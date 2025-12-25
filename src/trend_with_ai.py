import pandas as pd
import json
from collections import defaultdict
from ai_agent import extract_topics


# ------------------------------------
# Sample review data (can be replaced with real CSV later)
# ------------------------------------
reviews_data = [
    ("2024-06-01", "delivery was very late and food was cold"),
    ("2024-06-01", "delivery partner was rude"),
    ("2024-06-02", "food quality was bad and stale"),
    ("2024-06-02", "app map was not working properly"),
    ("2024-06-03", "delivery person behaved badly"),
    ("2024-06-03", "please bring back 10 minute delivery"),
]

# ------------------------------------
# Group reviews by date
# ------------------------------------
reviews_by_date = defaultdict(list)
for date, review in reviews_data:
    reviews_by_date[date].append(review)

# ------------------------------------
# Extract AI topics per date
# ------------------------------------
trend_counter = defaultdict(lambda: defaultdict(int))

for date, reviews in reviews_by_date.items():
    ai_output = extract_topics(reviews)

    topics = json.loads(ai_output)
    for item in topics:
        topic = item["topic"]
        trend_counter[topic][date] += 1

# ------------------------------------
# Convert to DataFrame
# ------------------------------------
df = pd.DataFrame(trend_counter).fillna(0).astype(int).T

# ------------------------------------
# Save output
# ------------------------------------
output_path = "output/ai_topic_trend_table.csv"
df.to_csv(output_path)

print("\nAI-POWERED TREND TABLE:\n")
print(df)
print(f"\nSaved to: {output_path}")
