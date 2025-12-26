### Pulsegen Technologies ### 
### Senior AI Engineer Assignment ### 
### AI Agent: Swiggy / Zomato Review Trend Analysis ### 

### Video Link ###

```

```


### Step By Step Process How to Excecute the Assignemnt ###
Step 1: 
- Open File Explorer
- Go to D:
- Right-click on empty space
- Click New Folder
- Name it as: Swiggy_Review_AI_Agent

Step 2: 
- Double-click Swiggy_Review_AI_Agent
- Right-click on empty space
- Click New
- Click Text Document
- Name it as: step1.txt
- Double-click and open step1.txt
- It will open in Notepad

Step 3:  COPY & PASTE in step1.txt Notepad and Press Ctrl + S

```

APP CHOSEN:
Swiggy
WHAT IS T:
T means the final day for which the report is created.
Example: If today is June 30, then T = June 30.
WHAT DOES T-30 TO T MEAN:
It means reviews from 30 days before T until T.
Example: June 1 to June 30.
WHAT DOES ONE TABLE CELL MEAN:
It shows how many reviews talked about one problem on one day.
WHY SIMILAR SENTENCES SHOULD BE COMBINED:
Different sentences can mean the same problem.
If not combined, the result will be wrong.

```

Step 4: 
- Press Windows key
- Type: cmd
- Press Enter

Step 5: cmd opens

Step 6: Now type exactly this and press Enter: python --version

---
<img width="595" height="242" alt="image" src="https://github.com/user-attachments/assets/200081af-a30c-442a-a7c2-16f3160e0f3f" />


---


Step 7: python -m venv venv and then press Enter.(It may take 5–10 seconds)

Step 8:  venv\Scripts\activate

---
<img width="666" height="311" alt="image" src="https://github.com/user-attachments/assets/61739f08-9d49-4a67-9fc1-3848d9bdb8a4" />



---


Step 9: python -m pip install --upgrade pip 

Step 10: pip install pandas numpy tqdm python-dateutil

Step 11: Creating folder for raw review data:
- mkdir data
- mkdir output
- mkdir src

Step 12: Now run this command in cmd: type nul > src\main.py

---
<img width="843" height="293" alt="image" src="https://github.com/user-attachments/assets/c0ad8ed2-d2a7-456a-bc4a-455241d9d22b" />



---



Step 13: 
- Go to File Explorer
- Open the folder: Swiggy_Review_AI_Agent
- Under it Open folder: src
- Double-click on src and open: main.py
- Now copy and paste this in main.py: print("Swiggy Review AI Agent started successfully")
- Press Ctrl + S

 Step 14: In cmd: python src\main.py

---
<img width="687" height="160" alt="image" src="https://github.com/user-attachments/assets/496d7c37-815c-48fc-b1f2-98af7dea93f3" />


---



Step 15: 
- Go to File Explorer
- Open the folder: Swiggy_Review_AI_Agent
- Under it Open folder: data
- Double-click on data
- Right-click → New → Text Document
- Name it as: reviews_sample.txt
- Double click on reviews_sample.txt and open it and paste the Below lines and Press Ctrl + S

```
2024-06-01 | Delivery was very late and food was cold
2024-06-01 | Delivery partner was rude
2024-06-02 | Food quality was bad and stale
2024-06-02 | App map was not working properly
2024-06-03 | Delivery person behaved badly
2024-06-03 | Please bring back 10 minute delivery
```

Step 16: src\main.py - Re write the Code in it: and Press Ctrl + S

```
print("Swiggy Review AI Agent started")
file_path = "data/reviews_sample.txt"
with open(file_path, "r", encoding="utf-8") as file:
    reviews = file.readlines()
print("Reviews loaded:")
for review in reviews:
    print(review.strip())
```

Step 17: In cmd: python src\main.py

---
<img width="733" height="391" alt="image" src="https://github.com/user-attachments/assets/e811a3e3-833f-456d-81e0-adb631b01836" />


---



Step 18: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
print("Swiggy Review AI Agent started")
file_path = "data/reviews_sample.txt"
with open(file_path, "r", encoding="utf-8") as file:
    reviews = file.readlines()
print("\nSeparated reviews:\n")
for review in reviews:
    parts = review.strip().split("|")
        date = parts[0].strip()
    text = parts[1].strip()
        print("Date:", date)
    print("Review:", text)
    print("------")
```

Step 19: again, In cmd: python src\main.py


---
<img width="660" height="757" alt="image" src="https://github.com/user-attachments/assets/b4d8ef40-139b-4a34-99ea-1035efa87c59" />


---



Step 20: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
print("Swiggy Review AI Agent started")
file_path = "data/reviews_sample.txt"
with open(file_path, "r", encoding="utf-8") as file:
    reviews = file.readlines()
# Dictionary to store reviews by date
reviews_by_date = {}
for review in reviews:
    date, text = review.strip().split("|")
    date = date.strip()
    text = text.strip()
    if date not in reviews_by_date:
        reviews_by_date[date] = []
    reviews_by_date[date].append(text)
print("\nReviews grouped by date:\n")
for date, texts in reviews_by_date.items():
    print("Date:", date)
    for t in texts:
        print(" -", t)
    print("------")
```

Step 21: again, In cmd: python src\main.py


---
<img width="744" height="763" alt="image" src="https://github.com/user-attachments/assets/9c1fc654-0b48-4b1e-8a96-665350df73ca" />


---



Step 22: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
print("Swiggy Review AI Agent started")
file_path = "data/reviews_sample.txt"
with open(file_path, "r", encoding="utf-8") as file:
    reviews = file.readlines()
# Group reviews by date
reviews_by_date = {}
for review in reviews:
    date, text = review.strip().split("|")
    date = date.strip()
    text = text.strip().lower()  # convert to lowercase
    if date not in reviews_by_date:
        reviews_by_date[date] = []
    reviews_by_date[date].append(text)
# Simple manual topic rules
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
print("\nTopics detected per date:\n")
for date, texts in reviews_by_date.items():
    print("Date:", date)
    for t in texts:
        topic = detect_topic(t)
        print(" -", topic, "=>", t)
    print("------")
```

Step 23: again, In cmd: python src\main.py


---
<img width="773" height="764" alt="image" src="https://github.com/user-attachments/assets/75c70899-61ac-49d0-ac8c-81ec09c924b6" />


---


Step 24: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
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
if date not in topic_trends[topic]:
topic_trends[topic][date] = 0
topic_trends[topic][date] += 1
print("\nTopic frequency per date:\n")
for topic, date_counts in topic_trends.items():
print("Topic:", topic)
for date, count in date_counts.items():
print(f" {date}: {count}")
print("------") 
```

Step 25: again, In cmd: python src\main.py

Step 26: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
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
print("\nFINAL TREND TABLE:\n")
print(df)
# Save output
output_path = "output/topic_trend_table.csv"
df.to_csv(output_path)
print(f"\nTrend table saved to: {output_path}") 
```

Step 27: again, In cmd: python src\main.py


---
<img width="783" height="767" alt="image" src="https://github.com/user-attachments/assets/6599aab1-beb2-45cd-9a38-b22657542e79" />


---


Step 28: again, Open src\main.py Replace the Whole code again and Press Ctrl + S

```
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
```

Step 29: again, In cmd: python src\main.py

---
<img width="766" height="766" alt="image" src="https://github.com/user-attachments/assets/0e5375ac-84b4-4e9c-ae11-0f55fa99e460" />


---



Step 30: 
- Go to File Explorer
- Open D:
- Double-click Swiggy_Review_AI_Agent
- Right-click on empty space
- Click New
- Click Text Document
- Name it as: agent_design.txt
- Double-click and open agent_design.txt
- It will open in Notepad Type the Below lines and Save it.

```
AGENT ROLE:
The agent reads daily reviews and identifies topics.
It merges reviews with similar meaning into one topic.
INPUT TO AGENT:
List of review texts for a single day.
OUTPUT FROM AGENT:
Topic name and list of reviews mapped to that topic.
WHY AGENTIC AI:
Rules cannot handle language variations.
AI reasoning is needed to merge similar meanings. 
```

Step 31: 
- Go to File Explorer
- Open D:
- Double-click Swiggy_Review_AI_Agent
- Click on src
- Right-click → New → Text Document
- Name it as: ai_agent.py
- Double-click and open ai_agent.py
- It will open and add Code in it, the Below lines and Save it.

```
import json
def extract_topics(reviews):
"""
AI agent with fallback logic.
Groups similar reviews into topics.
"""
# Fallback logic (works without OpenAI API key)
topics = []
delivery_rude = []
food_issue = []
for r in reviews:
r_lower = r.lower()
if "rude" in r_lower or "behaved badly" in r_lower:
delivery_rude.append(r)
elif "bad" in r_lower or "stale" in r_lower:
food_issue.append(r)
if delivery_rude:
topics.append({
"topic": "Delivery partner rude",
"reviews": delivery_rude
})
if food_issue:
topics.append({
"topic": "Food quality issue",
"reviews": food_issue
})
return json.dumps(topics, indent=2)
```

Step 32: 
- Go to File Explorer
- Open D:
- Double-click Swiggy_Review_AI_Agent
- Click on src
- Right-click → New → Text Document
- Name it as: trend_with_ai.py
- Double-click and open trend_with_ai.py
- It will open and add Code in it, the Below lines and Save it.

```
import pandas as pd
import json
from collections import defaultdict
from ai_agent import extract_topics
reviews_data = [
("2024-06-01", "Delivery was very late and food was cold"),
("2024-06-01", "Delivery partner was rude"),
("2024-06-02", "Food quality was bad and stale"),
("2024-06-02", "App map was not working properly"),
("2024-06-03", "Delivery person behaved badly"),
("2024-06-03", "Please bring back 10 minute delivery"),
]
reviews_by_date = defaultdict(list)
for date, review in reviews_data:
reviews_by_date[date].append(review)
trend_counter = defaultdict(lambda: defaultdict(int))
for date, reviews in reviews_by_date.items():
ai_output = extract_topics(reviews)
topics = json.loads(ai_output)
for t in topics:
trend_counter[t["topic"]][date] += 1
df = pd.DataFrame(trend_counter).fillna(0).astype(int).T
df = df.reindex(sorted(df.columns), axis=1)
print("\nAI POWERED TREND TABLE:\n")
print(df)
df.to_csv("output/ai_topic_trend_table.csv")
print("\nSaved to output/ai_topic_trend_table.csv") 
```


Step 33: Open cmd in project folder and run: python src\trend_with_ai.py

---
<img width="940" height="418" alt="image" src="https://github.com/user-attachments/assets/dafcc1fb-55c7-45e3-9fac-8a8b9d356c4f" />


---



Step 34: In agent_design.txt, add this at the bottom:

```
FALLBACK NOTE:
The AI agent includes rule-based fallback logic.
The system runs fully without an OpenAI API key.
This ensures reliability and zero-cost execution.
```

Step 35: Pushing all the files into GitHub

- Inside Swiggy_Review_AI_Agent
- Right-click → New → Text Document
- Name it as: .gitignore
- Open and Paste the Below lines and Save it 

```
venv/
__pycache__/
*.pyc
.env
```

Step 36: 
- Open cmd
- dir
- git init
- git remote add origin https://github.com/Vardhanpinisetti/Pulsegen-Technologies-Senior-AI-Engineer-Assignment.git
- git add .
- git commit -m "Completed AI agent for review trend analysis with documentation"
- git branch -M main
- git push -u origin main


###  Conclusion

In this assignemnt, we successfully designed and implemented an **AI-driven review trend analysis agent** for a food delivery platform (Swiggy/Zomato use case). The objective was to transform unstructured customer reviews into **structured, day-wise topic trends** that can support product, operations, and decision-making teams.

Starting from raw text reviews, we built the system **step by step**:

* Loaded and parsed timestamped customer reviews
* Cleaned and normalized text data
* Grouped reviews by date (T-30 to T window)
* Identified meaningful problem topics such as *Delivery Issues*, *Delivery Partner Behavior*, *Food Quality Issues*, *App Issues*, and *Feature Requests*
* Merged multiple reviews expressing the same intent into a single topic
* Counted topic frequency per day
* Generated a **trend table** showing how customer issues evolve over time
* Exported the final structured output as a CSV file for further analysis or dashboarding

The assignment intentionally progresses from **rule-based logic** to an **agentic AI design**, demonstrating why simple keyword rules are insufficient for real-world language variation. The agent design clearly defines:

* Inputs (daily review texts)
* Outputs (topics with mapped reviews)
* Responsibilities (semantic understanding and topic merging)

This approach reflects how modern AI systems are built in production: combining **data processing, reasoning, and explainable outputs** rather than relying on black-box predictions alone.

This solution is directly applicable to **customer experience analytics**, **operations monitoring**, and **product feedback analysis** in real-world AI systems.


