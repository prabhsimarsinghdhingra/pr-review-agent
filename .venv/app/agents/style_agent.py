from .base_agent import BaseAgent

class StyleAgent(BaseAgent):
    role = "style"

    async def review_hunk(self, file_path, hunk):
        prompt = f"""You are a STYLE reviewer.

Check for:
- readability
- naming
- formatting
- comments
- clarity

File: {file_path}
Hunk:
{hunk}

Please provide a concise review focusing on style issues, and if applicable, a suggested short code change or example.
"""

        result = await self.llm.call(prompt)
        return {"file": file_path, "hunk": hunk, "raw": result}
