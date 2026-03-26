#!/usr/bin/env python3
"""
Imagen 4 — Google's photorealistic image generation model
Batch Processing Example — Process multiple inputs efficiently

Installation:
    pip install nexa-ai

Get your API key:
    https://rapidapi.com/nexaquency/imagen-4/pricing

Model: imagen-4
"""

import time
from nexa_ai import NexaAI

# ── Setup ──────────────────────────────────────────────────────────────────────
API_KEY = "your-api-key"

client = NexaAI(api_key=API_KEY)

# ── Batch Inputs ───────────────────────────────────────────────────────────────
inputs = [
    "a cyberpunk city at night, neon lights, rain, 8k",
    "a serene Japanese garden in autumn, soft light",
    "an astronaut riding a horse on Mars, photorealistic",
    "a magical forest with glowing mushrooms, fantasy art",
    "a futuristic underwater city, bioluminescent, cinematic",
]

# ── Batch Processing ───────────────────────────────────────────────────────────
print(f"Processing {len(inputs)} images with imagen-4...")
print("-" * 60)

results = []
for i, input_text in enumerate(inputs, 1):
    print(f"[{i}/{len(inputs)}] Generating: {input_text[:50]}...")
    
    result = client.images.generate(
        model="imagen-4",
        prompt=input_text,
        width=1024,
        height=1024,
    )
    
    results.append({
        "input": input_text,
        "url": result.url,
        "job_id": result.job_id,
    })
    print(f"  ✅ Done → {result.url}")
    
    # Small delay to respect rate limits
    if i < len(inputs):
        time.sleep(0.5)

# ── Summary ────────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"✅ Batch complete! Generated {len(results)} images")
print("\nResults:")
for r in results:
    print(f"  • {r['input'][:40]}...")
    print(f"    URL: {r['url']}")
