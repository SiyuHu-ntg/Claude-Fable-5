# -*- coding: utf-8 -*-
import asyncio
from config import CLAUDE_FABLE_5, CLAUDE_OPUS_48

class FableClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        print(f"[System] Initializing Mythos-Class Claude Fable 5 Client...")

    async def generate_completion(self, prompt: str, system_instruction: str = None):
        """
        Simulates request to Claude Fable 5 with automatic fallback to Opus 4.8
        if safety classifiers detect restricted domains (cybersecurity, biology).
        """
        print(f"[Request] Sending tokens to {CLAUDE_FABLE_5} with Adaptive Thinking...")
        
        # Mocking the 2026 client behavior
        await asyncio.sleep(1) 
        
        # Sensitive topic check simulation
        sensitive_keywords = ["malware", "exploit", "bio-weapon", "cyberattack"]
        if any(keyword in prompt.lower() for keyword in sensitive_keywords):
            print(f"[Classifier Triggered] Safety filter activated. Routing to {CLAUDE_OPUS_48}.")
            return f"Fallback Response [Opus 4.8]: I cannot assist with high-risk requests."
            
        return f"Fable 5 Response: [Adaptive Thinking Output] Task completed successfully."
