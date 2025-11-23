import sys, asyncio
from fastapi.testclient import TestClient

# Make sure Python can import the 'app' package located in the .venv/app folder
sys.path.insert(0, r'c:\Windows\System32\pr-review-agent\\.venv\\app')
import app.main as app_module

# Provide a fake async run_agents_for_diff to avoid calling real LLMs
async def fake_run_agents_for_diff(llm, diff):
    return [{"file": "example.py", "hunk": diff, "raw": "MOCK_AGENT_OUTPUT"}]

# Monkeypatch the imported function in the main module so the endpoint uses this instead
app_module.run_agents_for_diff = fake_run_agents_for_diff

client = TestClient(app_module.app)

# GET /
resp = client.get("/")
print('GET / ->', resp.status_code, resp.json())

# POST /review-pr with a raw_diff
payload = {"raw_diff": "diff --git a/example.py b/example.py\n@@ -1 +1 @@\n-def foo():\n-    pass\n+def foo(x):\n+    return x\n"}
resp2 = client.post('/review-pr', json=payload)
print('POST /review-pr ->', resp2.status_code)
print(resp2.json())
