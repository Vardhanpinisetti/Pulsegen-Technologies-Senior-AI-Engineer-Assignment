### Pulsegen Technologies ### 
### Senior AI Engineer Assignment ### 
### AI Agent: Swiggy / Zomato Review Trend Analysis ### 

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


Step 7: python -m venv venv and then press Enter.(It may take 5–10 seconds)

Step 8:  venv\Scripts\activate

---
<img width="666" height="311" alt="image" src="https://github.com/user-attachments/assets/61739f08-9d49-4a67-9fc1-3848d9bdb8a4" />


Step 9: python -m pip install --upgrade pip 

Step 10: pip install pandas numpy tqdm python-dateutil

Step 11: Creating folder for raw review data:
- mkdir data
- mkdir output
- mkdir src

Step 12: Now run this command in cmd: type nul > src\main.py

---
<img width="843" height="293" alt="image" src="https://github.com/user-attachments/assets/c0ad8ed2-d2a7-456a-bc4a-455241d9d22b" />



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
