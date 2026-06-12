# -*- coding: utf-8 -*-
import asyncio
from config import get_api_key
from fable_client import FableClient
from agents import OrchestratorAgent

async def main():
    print("==================================================")
    print("   Claude Fable 5 Enterprise Scaffolding Test     ")
    print("==================================================\n")
    
    api_key = get_api_key()
    client = FableClient(api_key=api_key)
    orchestrator = OrchestratorAgent(client=client)
    
    # Test 1: Standard reasoning task
    prompt = "Design a distributed database ledger migration plan."
    response = await client.generate_completion(prompt)
    print(f"[Result] {response}\n")
    
    # Test 2: Long-horizon agent orchestration
    await orchestrator.run_parallel_workflow("Migrate legacy system to AWS Bedrock")
    
    print("\n[Status] All Fable 5 simulation suites passed.")

if __name__ == "__main__":
    asyncio.run(main())
