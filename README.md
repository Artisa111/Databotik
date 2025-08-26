<div dir="rtl" lang="he">

# 📊 דאטהבוטיק - עוזר ניתוח נתונים חכם

עוזר AI חכם לניתוח נתונים שמאפשר לך לנתח קבצי CSV, ליצור גרפים אינטראקטיביים ולקבל תובנות עמוקות מהנתונים שלך.

## 🚀 הפעלה מקומית

### שלב 1: הורדת הפרויקט
```bash
git clone https://github.com/Artisa111/Databotik.git
cd Databotik
```

### שלב 2: הגדרת סביבה וירטואלית
**Windows:**
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### שלב 3: הגדרת מפתחות API
צור קובץ `.env` בתיקיית הפרויקט:
```env
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_ASSISTANT_ID=asst-your-assistant-id-here
```

### שלב 4: יצירת עוזר OpenAI (אם עדיין אין לך)
```bash
python create_assistant.py
```

### שלב 5: הפעלת האפליקציה
```bash
chainlit run app.py --host 127.0.0.1 --port 8000
```

פתח בדפדפן: `http://localhost:8000`

---

## ☁️ פריסה ב-Railway

להפעלה מהירה בענן:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/databotik)

**הוראות פריסה:**
1. לחץ על כפתור Railway למעלה
2. חבר את חשבון GitHub שלך
3. הוסף את משתני הסביבה:
   - `OPENAI_API_KEY` - המפתח שלך מ-OpenAI
   - `OPENAI_ASSISTANT_ID` - מזהה העוזר שלך
4. לחץ "Deploy" והמתן שהפריסה תושלם
5. האפליקציה שלך תהיה זמינה בכתובת שRailway מספק

---

## 🎯 איך להשתמש

1. **העלה קובץ CSV** - פשוט גרור ושחרר את הקובץ
2. **שאל שאלות** - כתב בעברית או אנגלית על הנתונים שלך
3. **קבל תובנות** - העוזר ינתח וייצור גרפים אינטראקטיביים
4. **שמור תוצאות** - הורד את הגרפים והניתוחים

---

## 🔧 מה נתמך

**פורמטי קבצים:**
- 📄 CSV (מומלץ)
- 📊 Excel (XLSX)
- 📋 JSON

**סוגי גרפים:**
- 📊 גרפי עמודות ועוגות
- 📈 גרפי קווים וזמן
- 🔥 מפות חום ופיזור

---

<div align="center">

**💜 נוצר באהבה לאנליטיקת נתונים**

*עשוי עם ❤️ על ידי מפתחים שאוהבים נתונים*

</div>

</div>