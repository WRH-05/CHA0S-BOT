
# ChaosBot 🌀

ChaosBot is a Python bot that interacts with a Google Spreadsheet, allowing you to either **shuffle** all non-empty cells or **replace** them with a specific string of your choice. It's designed to provide chaotic or uniform transformations on any Google Sheet you have editor access to.

---

## 🚀 Features
- **Shuffle Mode**: Randomly shuffles all non-empty cells in the spreadsheet.
- **Replace Mode**: Replaces all non-empty cells with a string you provide.
- **Real-time Updates**: Continuously runs and updates the sheet based on your inputs.

---

## 📄 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/WRH-05/CHA0S-BOT.git
cd chaosBot
```

### 2. Install the Required Python Packages
Make sure you have Python 3 installed. Then, install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Setup Google Sheets API
To allow the bot to connect to your Google Sheets, follow these steps:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Sheets API** for the project.
4. Create **Service Account Credentials**:
   - Go to **APIs & Services → Credentials**.
   - Select **Create Credentials → Service Account**.
   - Download the `creds.json` file.
5. Place the downloaded `creds.json` file in the root of the project directory.
6. Share the Google Sheet with the **Service Account email** you find in your `creds.json` file (with **Editor** permission).

### 4. Configure the Bot
- Replace the placeholder `sheet_id` in the code (`bot.py`) with the **ID of your Google Sheet**.
  - Example:
    ```python
    sheet_id = 'your_google_sheet_id_here'
    ```

### 5. Run the Bot
```bash
python bot.py
```

---

## 📝 How to Use
Once running, the bot will prompt you:
- Enter **`shuffle`** to shuffle all non-empty cells.
- Enter any **other string** to replace all non-empty cells with that string.

Changes will be applied directly to your Google Sheet, and the updated values will be displayed in the console.

---

## 🔒 .gitignore
The following files are ignored from version control for security and cleanliness:
```
chaos/
creds.json
```

---

## 📜 License
MIT License

Copyright (c) 2025 Wassim Hachemi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 📌 Notes
- Don't forget to protect your `creds.json` file! It should **never** be uploaded publicly.
- The `.gitignore` file has been configured to exclude it from commits.
