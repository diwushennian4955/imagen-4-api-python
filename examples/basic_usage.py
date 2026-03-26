#!/usr/bin/env python3
"""
Imagen 4 — Google's photorealistic image generation model

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/imagen-4/pricing

Model: imagen-4
"""

from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
# Replace with your actual API key from https://nexa-api.com
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

# ── Basic Usage ────────────────────────────────────────────────────────────────
print("Starting imagen-4 generation...")

result = client.images.generate(
    model="imagen-4",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
)

print(f"✅ Generation complete!")
print(f"   Image url: {result.url}")
print(f"   Job ID: {result.job_id}")
print(f"   Status: {result.status}")
