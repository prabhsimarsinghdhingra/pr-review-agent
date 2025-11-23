from .base_agent import BaseAgent

class SecurityAgent(BaseAgent):
    role = "security"

    async def review_hunk(self, file_path, hunk):
        prompt = f"""You are a SECURITY code reviewer.

Check for:
- injections
- unsafe inputs
- secrets
- vulnerabilities
- missing validation

File: {file_path}
Hunk:
{hunk}

Please provide a concise review identifying any security issues and suggest mitigations.
"""

        result = await self.llm.call(prompt)
        return {"file": file_path, "hunk": hunk, "raw": result}
