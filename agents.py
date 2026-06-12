# -*- coding: utf-8 -*-
import asyncio

class OrchestratorAgent:
    def __init__(self, client):
        self.client = client

    async def run_parallel_workflow(self, main_task: str):
        print(f"[Orchestrator] Scoping long-horizon task: {main_task}")
        print("[Orchestrator] Dispatching asynchronous parallel subagents...")
        
        # Fable 5 is highly dependable at dispatching parallel subagents
        task1 = self.dispatch_subagent("Subagent_Coder", "Write refactoring script.")
        task2 = self.dispatch_subagent("Subagent_Verifier", "Verify code correctness against specs.")
        
        results = await asyncio.gather(task1, task2)
        print("[Orchestrator] Merging subagent execution results.")
        return results

    async def dispatch_subagent(self, name: str, assignment: str):
        await asyncio.sleep(0.5)
        print(f"  └─ [{name}] Executing task: {assignment}")
        return f"{name}_success"
