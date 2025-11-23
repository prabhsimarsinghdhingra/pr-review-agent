class BaseAgent:
    role = "base"

    def __init__(self, llm_client):
        self.llm = llm_client

    async def review_hunk(self, file_path: str, hunk: str):
        raise NotImplementedError
