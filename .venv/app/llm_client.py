try:
    # New-style OpenAI client (openai>=1.0.0)
    from openai import OpenAI as OpenAIAPI
    _HAS_NEW_OPENAI = True
except Exception:
    _HAS_NEW_OPENAI = False
    import openai as openai_legacy

class OpenAIClient:
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.model = model
        self.api_key = api_key
        if _HAS_NEW_OPENAI:
            self.client = OpenAIAPI(api_key=api_key)
            self._use_new = True
        else:
            openai_legacy.api_key = api_key
            self.client = openai_legacy
            self._use_new = False

    async def call(self, prompt: str) -> str:
        # This method is async to match the agents' usage. The underlying OpenAI client is sync,
        # so this will block the event loop for the duration of the HTTP call. For a production
        # async integration, use an async-compatible HTTP client or run calls in a thread pool.
        if self._use_new:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0
            )
            msg = resp.choices[0].message
            if isinstance(msg, dict):
                return msg.get("content", "")
            return getattr(msg, "content", "")
        else:
            resp = self.client.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0
            )
            msg = resp.choices[0].message
            if isinstance(msg, dict):
                return msg.get("content", "")
            return getattr(msg, "content", "")
