<div dir="rtl" lang="he">

# 📊 דאטהבוטיק - עוזר ניתוח נתונים חכם

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Chainlit](https://img.shields.io/badge/chainlit-v1.1.300rc4-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

[![📊 הפעל אפליקציה](https://img.shields.io/badge/🚀_הפעל_אפליקציה-4CAF50?style=for-the-badge&logo=rocket)](.)
[![📁 הורד פרויקט](https://img.shields.io/badge/📁_הורד_פרויקט-2196F3?style=for-the-badge&logo=github)](.)
[![🎯 צפה בדוגמאות](https://img.shields.io/badge/🎯_צפה_בדוגמאות-FF9800?style=for-the-badge&logo=eye)](.)

</div>

## 🌟 תיאור הפרויקט

**דאטהבוטיק** הוא עוזר חכם לניתוח נתונים המבוסס על בינה מלאכותית מתקדמת. האפליקציה מאפשרת לכם לנתח קבצי CSV בצורה אינטראקטיבית, ליצור גרפים מתקדמים ולקבל תובנות עמוקות מהנתונים שלכם.

### ✨ יכולות מתקדמות

<div align="center">

| 🎯 תכונה | 📝 תיאור | 🚀 פעולה |
|----------|---------|---------|
| 📊 ניתוח נתונים | ניתוח מתקדם של קבצי CSV עם AI | [![נתח עכשיו](https://img.shields.io/badge/נתח_עכשיו-4CAF50?style=flat-square)](.) |
| 📈 גרפים אינטראקטיביים | יצירת גרפים דינמיים עם Plotly | [![צור גרף](https://img.shields.io/badge/צור_גרף-2196F3?style=flat-square)](.) |
| 🎤 קלט קולי | העלאת קבצים ושאלות בקול | [![דבר איתי](https://img.shields.io/badge/דבר_איתי-FF5722?style=flat-square)](.) |
| 💬 צ'אט חכם | שיחה טבעית עם העוזר | [![התחל צ'אט](https://img.shields.io/badge/התחל_צ'אט-9C27B0?style=flat-square)](.) |

</div>

## 🛠️ הגדרת הפרויקט

### שלב 1️⃣: הורדת הפרויקט

</div>

```bash
git clone https://github.com/Artisa111/Databotik.git
cd Databotik
```

<div dir="rtl">

### שלב 2️⃣: התקנת חבילות

</div>

```bash
pip install -r requirements.txt
```

<div dir="rtl">

### שלב 3️⃣: הגדרת משתני סביבה

צור קובץ `.env` והוסף את מפתח ה-API שלך:

</div>

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_ASSISTANT_ID=your_assistant_id_here
```

<div dir="rtl">

### שלב 4️⃣: יצירת העוזר

</div>

```bash
python create_assistant.py
```

<div dir="rtl">

### שלב 5️⃣: הפעלת האפליקציה

</div>

```bash
chainlit run app.py -w
```

<div dir="rtl">

## 🎯 איך להשתמש

### 📊 ניתוח נתונים בסיסי
1. העלה קובץ CSV דרך הממשק
2. שאל שאלות על הנתונים בעברית או אנגלית
3. קבל ניתוחים מפורטים וגרפים אינטראקטיביים

### 🎤 שימוש בקלט קולי
1. לחץ על כפתור המיקרופון
2. דבר בבירור על הנתונים שרצית לנתח
3. העוזר יבין אותך ויספק תשובות מדויקות

## 🏗️ מבנה הפרויקט

</div>

```
📦 Databotik/
├── 🐍 app.py                 # קובץ האפליקציה הראשי
├── 🤖 create_assistant.py    # יצירת עוזר OpenAI
├── 📋 requirements.txt       # חבילות Python נדרשות
├── ⚙️ .env                  # משתני סביבה (מוסתר)
├── 📖 README.md             # תיעוד הפרויקט
├── 📄 chainlit.md           # הגדרות Chainlit
├── 🎨 public/               # קבצים סטטיים
│   ├── 💡 idea.svg
│   ├── 📚 learn.svg
│   ├── 💻 terminal.svg
│   └── ✍️ write.svg
└── ⚖️ LICENSE              # רישיון הפרויקט
```

<div dir="rtl">

## 🚀 תכונות מתקדמות

### 📈 סוגי גרפים נתמכים
- 📊 גרפי עמודות ועוגות
- 📈 גרפי קווים וזמן
- 🔥 מפות חום
- 📉 גרפי פיזור
- 🎯 גרפים מותאמים אישית

### 💻 פורמטי קבצים נתמכים
- 📄 CSV (מומלץ)
- 📊 Excel (XLSX)
- 📝 Text files
- 📋 JSON
- 📑 PDF (לקריאה)

## 🎨 התאמה אישית

### 🎭 העמודים הזמינים

</div>

```python
starters = [
    "נתח את קובץ מחירי מניות טסלה",
    "צור ניתוח נתונים לקובץ CSV שאעלה",
    "הראה לי מגמות בנתונים",
    "צור גרף אינטראקטיבי מהנתונים"
]
```

<div dir="rtl">

### 🔧 הגדרות מתקדמות

ניתן לשנות את הגדרות העוזר בקובץ `create_assistant.py`:

</div>

```python
instructions = """אתה עוזר לניתוח נתונים שרץ על קבצי CSV.
תשתמש בCode Interpreter לביצוע הניתוחים.
במקום להציג גרפים כתמונות, תיצור גרפי Plotly ותמיר אותם לJSON."""
```

<div dir="rtl">

## 🛡️ אבטחה ופרטיות

- 🔒 מפתחות API מוסתרים בקובץ `.env`
- 🚫 קבצים רגישים מוחרגים ב-`.gitignore`
- 🔐 הצפנת תעבורת נתונים
- 🛡️ אבטחת הפעלות AI

## 📞 תמיכה ועזרה

### 🐛 דיווח על באגים
</div>

[![דווח על באג](https://img.shields.io/badge/🐛_דווח_על_באג-FF5722?style=for-the-badge&logo=github)](https://github.com/Artisa111/Databotik/issues)

<div dir="rtl">

### 💡 הצעות לשיפור
</div>

[![הצע שיפור](https://img.shields.io/badge/💡_הצע_שיפור-4CAF50?style=for-the-badge&logo=lightbulb)](https://github.com/Artisa111/Databotik/discussions)

<div dir="rtl">

### 📚 תיעוד נוסף
</div>

[![מדריך מפורט](https://img.shields.io/badge/📚_מדריך_מפורט-2196F3?style=for-the-badge&logo=book)](https://github.com/Artisa111/Databotik/wiki)

<div dir="rtl">

## 🌟 תמונות מסך

### 💬 ממשק הצ'אט
![ממשק הצ'אט](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=צ'אט+עוזר+הנתונים)

### 📊 דוגמת ניתוח
![דוגמת ניתוח](https://via.placeholder.com/800x400/2196F3/FFFFFF?text=ניתוח+נתונים+מתקדם)

### 📈 גרפים אינטראקטיביים
![גרפים אינטראקטיביים](https://via.placeholder.com/800x400/FF9800/FFFFFF?text=גרפים+אינטראקטיביים)

## 🎯 דוגמאות שימוש

### דוגמה 1: ניתוח מכירות
</div>

```python
# שאלה: "נתח את נתוני המכירות החודשיים"
# התוצאה: גרף עמודות מפורט + ניתוח סטטיסטי
```

<div dir="rtl">

### דוגמה 2: מגמות זמן
</div>

```python
# שאלה: "הראה מגמות במהלך השנה"
# התוצאה: גרף קווים דינמי + חיזוי מגמות
```

<div dir="rtl">

## 🚀 פיתוח עתידי

### 🔮 תכונות מתוכננות
- 🤖 תמיכה במודלים נוספים של AI
- 📱 אפליקציית מובייל
- 🌐 תמיכה בשפות נוספות
- ☁️ שמירה בענן
- 📧 דיווחים אוטומטיים

### 🛠️ שיפורים טכניים
- ⚡ ביצועים מהירים יותר
- 🎨 עיצוב משודרג
- 🔧 יותר אפשרויות התאמה
- 📊 סוגי ויזואליזציה נוספים

## ❤️ תודות והכרות

תודה מיוחדת לקהילת הקוד הפתוח על:
- 🐍 Python Community
- 🤖 OpenAI Team  
- ⛓️ Chainlit Developers
- 📊 Plotly Team

## 📜 רישיון

הפרויקט זמין תחת רישיון MIT. ראה את קובץ ה-`LICENSE` לפרטים נוספים.

---

<div align="center">

### 💝 נוצר באהבה על ידי Artura

**📅 Date is Love | תאריך הוא אהבה**

[![⭐ תן כוכב](https://img.shields.io/badge/⭐_תן_כוכב-FFD700?style=for-the-badge&logo=github)](https://github.com/Artisa111/Databotik)
[![🍴 עשה Fork](https://img.shields.io/badge/🍴_עשה_Fork-4CAF50?style=for-the-badge&logo=github)](https://github.com/Artisa111/Databotik/fork)
[![📞 צור קשר](https://img.shields.io/badge/📞_צור_קשר-2196F3?style=for-the-badge&logo=github)](https://github.com/Artisa111)

**🚀 בואו ביחד ننתח נתונים ונגלה תובנות!**

</div>

</div>