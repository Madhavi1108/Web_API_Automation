# 📅 Task Scheduler with Google Sheets, Email & Google Calendar

A mini productivity project that helps you manage tasks with **Google Sheets**, sends you a **daily email digest**, and syncs tasks with **Google Calendar** for reminders.  
Built step-by-step over **21 days** as a practice project.

---

## 🎯 Features
- Add tasks in Google Sheets (TaskID, Date, Title, Description, Priority, Status, Notes).
- Daily morning email → Today’s tasks, overdue tasks, motivational quote.
- Priority highlighting with emojis (🔥 High, ⏳ Medium, 🌱 Low).
- Automatic sync with Google Calendar.
- Weekly summary email with stats and streak tracking.
- Runs automatically on cloud / system scheduler.

---

## 🗓️ 21-Day Roadmap

**Day 1:** Create Google Sheet → Add columns (TaskID, Date, Title, Description, Priority, Status, Notes) + sample tasks.  
**Day 2:** Set up Python environment. Install `pandas`, `gspread`, `oauth2client`, `smtplib`.  
**Day 3:** Enable Google Sheets API in Google Cloud Console → Download `credentials.json`.  
**Day 4:** Connect Python to Google Sheets API → Read sample tasks.  
**Day 5:** Write logic to filter tasks where Date = today. Print in console.  
**Day 6:** Design neat text format for tasks (with priority labels).  
**Day 7:** Connect Python to Gmail SMTP → Send a test email to yourself.  

**Day 8:** Combine steps → Read today’s tasks from Google Sheets → Send as an email digest.  
**Day 9:** Add logic → Include overdue tasks in the email.  
**Day 10:** Add motivational quote of the day (hardcoded list or API).  
**Day 11:** Add priority coloring/emoji in email (🔥 High, ⏳ Medium, 🌱 Low).  
**Day 12:** Test end-to-end: Google Sheet → Python → Email.  

**Day 13:** Enable Google Calendar API in Google Cloud Console → Download credentials.  
**Day 14:** Write Python code to create a Google Calendar event from one sample task.  
**Day 15:** Extend code → Push all tasks from Google Sheet into Google Calendar.  
**Day 16:** Prevent duplicates (only push new tasks).  
**Day 17:** (Optional) Read Google Calendar events back into Google Sheets.  

**Day 18:** Automate script → Set it to run every morning (Task Scheduler / cron / cloud).  
**Day 19:** Add weekly summary email (e.g., “You completed 7/10 tasks this week = 70%”).  
**Day 20:** Add streak tracker → Count consecutive days with completed tasks.  
**Day 21:** Final polish → Test everything, document setup, and showcase project.  

---

## 🛠️ Tech Stack
- **Python** (pandas, gspread, google-api-python-client, smtplib)
- **Google Sheets API** (task storage)
- **Google Calendar API** (reminders & sync)
- **Gmail SMTP** (email digest)
- **Scheduler** (Windows Task Scheduler / cron / cloud automation)

---

## 🚀 How It Works
1. Add tasks in Google Sheets.  
2. Python script fetches today’s tasks + overdue tasks.  
3. Script sends an email digest every morning.  
4. Tasks are synced into Google Calendar for reminders.  
5. Weekly summary email tracks progress and streaks.  

---

## 📌 Future Improvements
- Simple Tkinter or Flask interface for adding tasks.  
- Mobile notifications instead of just email.  
- AI-powered task prioritization.  

---

## 🤝 Contribution
This is a practice project built step by step. Suggestions and improvements are welcome!
