from fastapi import FastAPI, HTTPException
from app.schemas import ReviewRequest, ReviewResponse, InlineComment
from app.github_client import fetch_pr_diff
from app.orchestrator import run_agents_for_diff
from app.llm_client import OpenAIClient
import os

app = FastAPI()

# Load API key from environment variable
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize LLM client
llm = OpenAIClient(OPENAI_KEY)

@app.get("/")
def home():
    return {"status": "PR Review Agent Running"}

@app.post("/review-pr", response_model=ReviewResponse)
async def review_pr(req: ReviewRequest):
    if not req.github_pr_url and not req.raw_diff:
        raise HTTPException(400, "Provide either a GitHub PR URL or raw diff")

    # Fetch diff from GitHub if URL provided
    if req.github_pr_url:
        diff = await fetch_pr_diff(req.github_pr_url, GITHUB_TOKEN)
        pr_url = req.github_pr_url
    else:
        diff = req.raw_diff
        pr_url = None

    # Run all review agents
    raw_results = await run_agents_for_diff(llm, diff)

    # Convert raw results to structured InlineComment objects
    comments = [
        InlineComment(
            file_path=r.get("file", "unknown"),
            line_number=None,
            hunk=r.get("hunk", ""),
            message=r.get("raw", "").strip(),
            severity="SUGGESTION"
        ) for r in raw_results
    ]

    return ReviewResponse(
        pr_url=pr_url,
        comments=comments,
        summary=f"Generated {len(comments)} review comments."
    )
