# main.py

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import os
from dotenv import load_dotenv  # ✅ Load the .env file

load_dotenv()  # ✅ This line actually loads your .env

app = FastAPI()

# Initialize OpenAI client with your API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Serve static files if needed (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML form page
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>FAANG-Level AI Assistant</title>
</head>
<body>
    <h2>Welcome to FAANG-Level AI Assistant</h2>
    <form action="/process" method="post">
        <label for="task">Choose a task:</label><br>
        <select name="task">
            <option value="qa">Answer a Question</option>
            <option value="summarize">Summarize Text</option>
            <option value="creative">Generate Creative Content</option>
        </select><br><br>

        <label for="input_text">Your Input:</label><br>
        <textarea name="input_text" rows="6" cols="60"></textarea><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def index():
    return html_form

@app.post("/process", response_class=HTMLResponse)
async def process(task: str = Form(...), input_text: str = Form(...)):
    if task == "qa":
        prompt = f"You are a helpful assistant. Answer this factual question clearly:\nQ: {input_text}\nA:"
    elif task == "summarize":
        prompt = f"Summarize this text in 3-4 bullet points:\n{input_text}\nSummary:"
    elif task == "creative":
        prompt = f"Write a short creative story or poem about:\n{input_text}\nOutput:"
    else:
        return HTMLResponse(content="Invalid Task", status_code=400)

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an advanced AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    # Feedback form
    feedback_form = f"""
    <h3>AI Assistant Response:</h3>
    <p>{answer}</p>
    <form action="/feedback" method="post">
        <input type="hidden" name="task" value="{task}">
        <input type="hidden" name="input_text" value="{input_text}">
        <input type="hidden" name="answer" value="{answer}">
        <label>Was this helpful?</label><br>
        <input type="radio" name="helpful" value="yes"> Yes
        <input type="radio" name="helpful" value="no"> No<br><br>
        <input type="submit" value="Submit Feedback">
    </form>
    <br><a href="/">Try Another</a>
    """

    return HTMLResponse(content=feedback_form)

@app.post("/feedback", response_class=HTMLResponse)
async def feedback(task: str = Form(...), input_text: str = Form(...), answer: str = Form(...), helpful: str = Form(...)):
    # Append feedback to local file
    with open("feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(f"TASK: {task}\nINPUT: {input_text}\nANSWER: {answer}\nHELPFUL: {helpful}\n---\n")
    return HTMLResponse(content="<h3>Thank you for your feedback!</h3><a href='/'>Back to Home</a>")
load_dotenv()
print("LOADED API KEY:", os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print("LOADED API KEY:", os.getenv("OPENAI_API_KEY"))
