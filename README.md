# 🩺 MediSphere AI

> **AI-Powered Multi-Agent Healthcare Assistant built with LangGraph, Gemini, Streamlit, and OCR**

MediSphere AI is an intelligent healthcare assistant that helps users understand medical reports, generate medication schedules, compare laboratory reports, and interact with an AI assistant using natural language.

> **Disclaimer:** This project is intended for educational and portfolio purposes only. It does **not** provide medical diagnosis or professional medical advice.

---

# 📸 Screenshots

> *(Add screenshots after deployment)*

| Dashboard | Report Parser |
|-----------|---------------|
| Screenshot | Screenshot |

| Medication Manager | AI Assistant |
|-------------------|--------------|
| Screenshot | Screenshot |

---

# ✨ Features

## 🩺 Medical Report Parser

- Upload blood/laboratory reports
- OCR + Gemini Vision powered extraction
- Structured JSON generation
- Human-readable report summaries
- Professional PDF export

---

## 💊 Medication Manager

- Paste prescriptions
- Generate medication schedules
- Medicine explanation
- Usage instructions
- Safe AI responses

---

## 🤖 AI Healthcare Assistant

Context-aware chatbot capable of answering questions about:

- Uploaded medical reports
- Laboratory parameters
- Medication schedules

The assistant follows strict safety rules and avoids diagnosis or treatment recommendations.

---

## 📊 Report Comparison

Compare two laboratory reports.

Highlights:

- Test value changes
- Status changes
- Structured comparison
- Summary generation

---

## 📈 Analytics Dashboard

Application analytics including:

- Reports parsed
- Medication schedules generated
- Success/Failure rate
- Average processing time
- Agent usage
- Recent activity

---

## 📜 History

Stores previous interactions using SQLite.

Includes:

- Agent
- Timestamp
- Status
- Execution time
- User input
- AI response

---

## 📄 Professional PDF Export

Generate downloadable PDF reports containing:

- Report summary
- Laboratory explanations
- Professional formatting

---

# 🏗 Architecture

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
          LangGraph Supervisor
                  │
     ┌────────────┴────────────┐
     ▼                         ▼
Medical Report Agent    Medication Agent
     │                         │
     └────────────┬────────────┘
                  ▼
           Gemini AI Services
                  │
        OCR + Vision + LLM
                  │
                  ▼
             SQLite Database
```

---

# 🧠 Multi-Agent Workflow

```
User Request
      │
      ▼
Supervisor Agent
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Report   Medication
Parser   Manager
 │          │
 └────┬─────┘
      ▼
Final Response
```

---

# 🛠 Technology Stack

### Frontend

- Streamlit

### AI

- Google Gemini
- LangChain
- LangGraph

### OCR

- Tesseract OCR
- Pillow

### Backend

- Python

### Database

- SQLite
- SQLAlchemy

### PDF Generation

- ReportLab

### Environment

- Python Dotenv

---

# 📂 Project Structure

```
MediSphere-AI/

├── agents/
├── config/
├── database/
├── graph/
├── models/
├── services/
├── ui/
├── utils/
├── uploads/
├── generated_reports/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/MediSphere-AI.git

cd MediSphere-AI
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY

DATABASE_URL=sqlite:///database/medisphere.db
```

---

## Install Tesseract OCR

### Windows

Download:

https://github.com/UB-Mannheim/tesseract/wiki

Update `.env` if necessary.

```
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

### Linux

```bash
sudo apt install tesseract-ocr
```

---

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📦 Docker

*(Coming Soon)*

```bash
docker compose up --build
```

---

# 📊 Current Capabilities

| Feature | Status |
|----------|---------|
| Report Parsing | ✅ |
| OCR | ✅ |
| Gemini Vision | ✅ |
| Medication Manager | ✅ |
| AI Assistant | ✅ |
| Report Comparison | ✅ |
| Analytics | ✅ |
| PDF Export | ✅ |
| History | ✅ |
| Session Management | ✅ |
| Docker | 🚧 |

---

# 🔒 Safety

MediSphere AI intentionally avoids:

- Medical diagnosis
- Disease prediction
- Medication dosage changes
- Emergency advice
- Treatment recommendations

The system only explains information already present in uploaded reports and medication schedules.

---

# 🎯 Future Improvements

- Voice Assistant
- Multi-language Support
- User Authentication
- Cloud Deployment
- Report Timeline
- Health Trend Charts
- Medication Reminders
- Doctor Dashboard
- FHIR Integration
- Electronic Health Record Support

---

# 👨‍💻 Developer

**Vedant Paste**

Bachelor of Engineering (Computer Science)

Yashwantrao Bhonsale Institute of Technology

Mumbai University

---

# ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub.