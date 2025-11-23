from .base_agent import BaseAgent

class LogicAgent(BaseAgent):
    role = "logic"

    async def review_hunk(self, file_path, hunk):
        prompt = f"""You are a senior engineer reviewing code for LOGIC ERRORS.

File: {file_path}
Hunk:
{hunk}

Please provide a concise review describing possible logic errors and suggested fixes.
"""

        result = await self.llm.call(prompt)
        return {"file": file_path, "hunk": hunk, "raw": result}
