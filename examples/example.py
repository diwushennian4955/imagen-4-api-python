#!/usr/bin/env python3
"""
Imagen 4 — Image Generation Example
Using NexaAPI Python SDK

Get your API key at: https://nexa-api.com
"""

from nexa_ai import NexaAI

# Initialize client
client = NexaAI(api_key="your-api-key")

# Generate an image
print("Generating image with Imagen 4...")
result = client.images.generate(
    model="imagen-4",
    prompt="a beautiful sunset over mountains, photorealistic, 8k",
    width=1024,
    height=1024,
)

print(f"✅ Image generated!")
print(f"   URL: {result.url}")
print(f"   Job ID: {result.job_id}")
print(f"   Status: {result.status}")


# Batch generation
prompts = [
    "a cyberpunk city at night, neon lights, rain",
    "a serene Japanese garden in autumn",
    "an astronaut riding a horse on Mars",
]

print("\nBatch generating images...")
for prompt in prompts:
    result = client.images.generate(model="imagen-4", prompt=prompt)
    print(f"  ✅ {prompt[:40]}... → {result.url}")
