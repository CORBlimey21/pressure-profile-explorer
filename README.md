# 🎓 Pressure Profile Explorer

A friendly, interactive tool to help students reflect on their workload, stress, and time commitments — based on real-world data from Cork secondary school students.

---

## 🚀 What It Does

- 🔍 **Estimates your pressure profile** based on weekly extracurricular hours and daily academic study  
- 🎭 **Suggests a student persona** (e.g. *Stretched Achiever*, *Academic Driver*) based on your habits  
- 📘 **Compares pressure from your activities** (like music or sport) to your actual time commitment  
- 📊 **Visualises data** from over 300 second- and fifth-year students using a dynamic pie chart  

👉 **Try it out live**: [scifest.streamlit.app](https://scifest.streamlit.app)  
📝 **Contribute to the dataset**: [Submit your experience](https://docs.google.com/forms/d/e/1FAIpQLSfmZAcxP88l1EO3lNy1reTFSCfOAPsnkc0p_pSOANufOF3uvQ/viewform?usp=dialog)

---

## 🧠 Why It Matters

Too many students feel overwhelmed, but don’t know *why*. This tool helps break down that pressure into understandable profiles using real Irish student data.

It’s designed to:
- Promote reflection and balance  
- Show how different commitments affect stress  
- Be kind, honest, and useful — not judgmental  

---

## 🛠 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/CORBlimey21/pressure-profile-explorer.git
   cd pressure-profile-explorer
Install dependencies:
pip install -r requirements.txt
Launch the app:
streamlit run st_scifest_app.py
📊 Dataset Overview

This project uses anonymised survey data collected from 303 students across three Cork secondary schools.

Each entry includes:

Weekly extracurricular hours
Daily academic hours (outside school)
Self-reported pressure levels (1–5 scale)
The data is used to:

Find students with similar schedules
Estimate average pressure levels
Generate relatable student profiles
🔒 All data is anonymous. No personal info was collected.
📄 See 2and5.csv for full dataset details.
🧩 Profile Types

The app will classify you as one of these pressure profiles:

Profile	Description
🎯 Stretched Achiever	High academic and extracurricular load, high stress risk
⚖️ Well-Rounded Learner	Balanced mix of study and activities
🎨 Activity Adventurer	More focus on extracurriculars than homework
📚 Academic Driver	Strong focus on schoolwork with less outside activity
😌 Take-it-easy Explorer	Minimal pressure, low homework and activity levels
Each profile comes with tailored traits and wellbeing advice.

📂 File Structure

📁 pressure-profile-explorer/
├── 2and5.csv              # Anonymised dataset
├── LICENSE                # MIT license
├── README.md              # This file
├── requirements.txt       # Python package list
├── st_scifest_app.py      # Main Streamlit app
├── .gitignore             # Ignore rules
📄 License

This project is licensed under the MIT License.
Feel free to fork, reuse, or adapt it with credit.

💬 Got Feedback or Ideas?

This started as a side project for a student research fair — but it’s grown into something I’d love to keep improving.
Open an issue, suggest improvements, or just try it and share it around.
