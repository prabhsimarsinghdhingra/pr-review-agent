import asyncio
from app.orchestrator import run_agents_for_diff

class MockLLM:
    async def call(self, prompt: str) -> str:
        return "MOCK REVIEW: This is a mock response for testing."

async def main():
    diff = """diff --git a/example.py b/example.py
@@ -1,3 +1,4 @@
-def foo():
-    pass
+def foo(x):
+    return x
"""
    results = await run_agents_for_diff(MockLLM(), diff)
    print('--- Review Results ---')
    for r in results:
        print(r)

if __name__ == '__main__':
    asyncio.run(main())
