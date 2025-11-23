from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class ReviewRequest(BaseModel):
    github_pr_url: Optional[HttpUrl] = None
    raw_diff: Optional[str] = None

class InlineComment(BaseModel):
    file_path: str
    line_number: Optional[int] = None
    hunk: Optional[str] = None
    message: str
    severity: str
    suggestion: Optional[str] = None

class ReviewResponse(BaseModel):
    pr_url: Optional[str]
    comments: List[InlineComment]
    summary: str
