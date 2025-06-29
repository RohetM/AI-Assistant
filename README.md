# AI-Assistant
🚀 A simple AI Assistant built with FastAPI + OpenAI + Python. Answers questions, summarizes text, generates content — with feedback logging.

```markdown
# 🚀 AI Assistant

A simple, **AI Assistant** built with **FastAPI** and **OpenAI API**.  
It can:
- ✅ Answer factual questions
- ✅ Summarize long text
- ✅ Generate creative content (stories, poems)
- ✅ Collect user feedback for improvement

---

## 📂 Project Structure

```

AI-Assistant/
├── main.py             # FastAPI app
├── .env.example        # Example env file (no secrets!)
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── LICENSE             # License file (MIT)
├── .gitignore          # Files to ignore
├── static/             # (Optional) CSS or images
├── feedback\_log.txt    # Stores user feedback

````

---

## ⚙️ Setup Instructions

1️⃣ **Clone this repo**

```bash
git clone https://github.com/YOUR_USERNAME/AI-Assistant.git
cd AI-Assistant
````

2️⃣ **Create your `.env`**

```bash
cp .env.example .env
```

3️⃣ **Add your OpenAI API key**
Edit `.env`:

```
OPENAI_API_KEY=YOUR_REAL_API_KEY
```

4️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

5️⃣ **Run the app**

```bash
uvicorn main:app --reload
```

6️⃣ **Open in your browser**

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Features

* **FastAPI** backend — simple, modern Python framework
* **OpenAI** integration — GPT-powered prompt handling
* **Three prompt modes** — Q\&A, Summarize, Creative
* **Feedback loop** — logs user feedback to `feedback_log.txt`
* **.env.example** — secure key management
* **Clean UI** — minimal HTML/CSS styling, easy to customize

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE) for details.

---

## ✨ Author

Rohet M
Feel free to ⭐ star the repo or fork for your own experiments!

---

**🚀 Happy Building!**

```

---

## ✅ **How to use it**

1️⃣ Copy this `README.md` to your repo.  
2️⃣ Replace `YOUR_USERNAME` with your GitHub username in the `git clone` link.  
3️⃣ Add your name at the end.  
4️⃣ Done — now your project looks **clean and professional**.  

---
