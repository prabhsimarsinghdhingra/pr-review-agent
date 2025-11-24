🚀 Automated GitHub Pull Request Review Agent
AI-powered Multi-Agent Code Reviewer built using FastAPI + LLMs

This project is built as part of a backend engineering assignment to demonstrate the ability to:

Build production-grade Python backends

Integrate LLMs into workflows

Use multi-agent reasoning

Work with GitHub diffs & PR data

Design clean, scalable API endpoints

Deliver in a short 2–3 day engineering sprint

This repository contains a working AI PR Review Backend that automatically analyzes code changes inside GitHub Pull Requests and generates structured, actionable review comments — similar to a human code reviewer.

📌 Features
✅ 1. Pull Request Diff Analysis

Accepts either:

A GitHub Pull Request URL

OR a raw diff string

Uses GitHub API to fetch .diff files when URL is provided.

✅ 2. Multi-Agent Architecture

Your backend runs 4 specialized AI reviewers, each with unique responsibilities:

Agent	Responsibility
Logic Agent	Finds bugs, logical errors, missing conditions
Security Agent	Detects vulnerabilities, unsafe patterns
Performance Agent	Identifies slow patterns, unoptimized code
Style Agent	Improves readability, formatting, clarity

All agents run concurrently using asyncio.

📌 3. Structured JSON Review Output

The output looks like this:

{
  "pr_url": null,
  "summary": "Generated 4 review comments.",
  "comments": [
    {
      "file_path": "a.txt",
      "message": "LOGIC: ...",
      "severity": "SUGGESTION",
      "hunk": "@@ -1 +1 @@\n-old\n+new"
    }
  ]
}


Perfect for frontend integration or PR inline comments.

🏗 Architecture
                ┌──────────────────────────┐
                │        FastAPI API        │
                └─────────────┬────────────┘
                              │
                 Receives PR URL or diff
                              │
                 ┌────────────▼────────────┐
                 │      Diff Parser         │
                 └────────────┬────────────┘
                              │
                     Generates hunks
                              │
              ┌───────────────▼────────────────┐
              │      Multi-Agent Orchestrator   │
              │  (async concurrent execution)   │
              └─────┬──────────┬──────────┬────┘
                    │          │          │
            ┌───────▼───────┐ ┌▼──────────▼─┐ ┌─────────────▼─────┐
            │ Logic Agent   │ │Security Agent│ │Performance Agent   │
            └───────────────┘ └──────────────┘ └───────────────────┘
                           ┌───────────────────────┐
                           │      Style Agent       │
                           └───────────────────────┘
                              │
                              ▼
                    Aggregated PR Review JSON

⚙️ Tech Stack

Python 3.11

FastAPI (Backend Framework)

Uvicorn (ASGI Server)

OpenAI API (LLM engine)

httpx (Async HTTP client)

asyncio (Concurrency)

Pydantic (Data validation)

📁 Project Structure
pr-review-agent/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── llm_client.py
│   ├── diff_parser.py
│   ├── orchestrator.py
│   ├── github_client.py
│   └── agents/
│       ├── base_agent.py
│       ├── logic_agent.py
│       ├── security_agent.py
│       ├── perf_agent.py
│       └── style_agent.py
│
├── requirements.txt
└── README.md

🔧 Setup Instructions (Windows-Friendly)
1️⃣ Clone the repo
git clone <your_repo_url>
cd pr-review-agent

2️⃣ Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

4️⃣ Add your OpenAI API key

In CMD:

setx OPENAI_API_KEY "your_api_key_here"


Restart CMD and activate venv again.

5️⃣ Run the server
uvicorn app.main:app --reload --port 8000


Visit:
👉 http://127.0.0.1:8000

You should see:

{"status":"PR Review Agent Running"}

🧪 How to Test the Agent
OPTION A — Using Swagger UI (Easiest)

Open:
👉 http://127.0.0.1:8000/docs

Click:

POST /review-pr

Try it out

Paste:

{
  "raw_diff": "diff --git a/a.txt b/a.txt\n@@ -1 +1 @@\n-old\n+new"
}


Press Execute → You will see review comments.

📦 Future Enhancements

GitHub Bot for posting inline comments

CI/CD integration

Offline caching of reviews

Advanced ML heuristics for scoring severity

Frontend UI for visual diff review

🏁 Final Notes

This project demonstrates strong backend engineering skills in:

API design

LLM orchestration

Multi-agent systems

Async workflows

Code parsing and analysis

Clean modular architecture
