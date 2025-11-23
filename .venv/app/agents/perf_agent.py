from .base_agent import BaseAgent

class PerfAgent(BaseAgent):
    role = "performance"

    async def review_hunk(self, file_path, hunk):
        prompt = f"""You are a PERFORMANCE reviewer.

Look for:
- slow loops
- unnecessary operations
- expensive API calls
- O(n^2) patterns

File: {file_path}
Hunk:
{hunk}

Please provide a concise review highlighting potential performance issues and possible improvements.
"""

        result = await self.llm.call(prompt)
        return {"file": file_path, "hunk": hunk, "raw": result}
