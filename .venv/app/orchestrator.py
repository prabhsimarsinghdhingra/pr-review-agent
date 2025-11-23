import asyncio
from app.diff_parser import parse_unified_diff
from app.agents.logic_agent import LogicAgent
from app.agents.security_agent import SecurityAgent
from app.agents.perf_agent import PerfAgent
from app.agents.style_agent import StyleAgent

async def run_agents_for_diff(llm_client, diff_text):
    files = parse_unified_diff(diff_text)

    agents = [
        LogicAgent(llm_client),
        SecurityAgent(llm_client),
        PerfAgent(llm_client),
        StyleAgent(llm_client),
    ]

    tasks = []
    for file in files:
        for hunk in file["hunks"]:
            for agent in agents:
                tasks.append(agent.review_hunk(file["file_path"], hunk))

    return await asyncio.gather(*tasks)
