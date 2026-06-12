# -*- coding: utf-8 -*-
"""
Configuration settings for Claude Fable 5 and Mythos 5 deployment.
"""
import os

# Model IDs as per June 2026 Anthropic Specifications
CLAUDE_FABLE_5 = "claude-fable-5"
CLAUDE_OPUS_48 = "claude-opus-4.8"

# Pricing Specs ($10/M input, $50/M output)
PRICE_PER_M_INPUT = 10.0
PRICE_PER_M_OUTPUT = 50.0

DEFAULT_CONTEXT_WINDOW = 1000000 # 1M tokens default
MAX_OUTPUT_TOKENS = 128000       # Up to 128k output tokens

def get_api_key():
    return os.getenv("ANTHROPIC_API_KEY", "mock_fable_5_key_for_testing")
