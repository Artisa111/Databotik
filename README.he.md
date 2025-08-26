# ‎Databotik — מדריך התחלה מהירה‎

<div dir="rtl">

## 🚀 התחלה מהירה

1) שכפול הפרויקט וכניסה לתיקייה

```bash
git clone https://github.com/Artisa111/Databotik.git
cd Databotik
```

2) יצירת סביבה וירטואלית והתקנת תלויות
- Windows (PowerShell):
```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
- Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3) יצירת קובץ ‎.env‎ עם המפתחות שלך

```dotenv
OPENAI_API_KEY=sk-...המפתח-שלך...
OPENAI_ASSISTANT_ID=asst_...assistant_id שלך...
# רשות: קובץ CSV לדוגמה ליצירת עוזר
SAMPLE_CSV_PATH=
```

4) הפעלה מקומית

```bash
python -m chainlit run app.py --host 127.0.0.1 --port 8006
```

פתח/י: `http://127.0.0.1:8006`

### הערות
- אם הפורט תפוס, אפשר להחליף ל־8007/8008.
- אם אין לך עדיין Assistant, ניתן ליצור אחד ע"י:
```bash
python create_assistant.py
```
ולעדכן את ה־`OPENAI_ASSISTANT_ID` ב־`.env`.

</div>
