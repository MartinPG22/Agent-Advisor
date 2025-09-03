import json
from huggingface import client
from config import HF_MODEL

def classify_query(state):
    query = state['query']

    system_prompt = """
You are a classification agent for a multi-agent AI system.

Your task is to analyze the user's query and identify which areas of expertise are required to answer it.

You must choose one or more of the following categories, based on these definitions:

- budget: Questions about financial feasibility, costs, pricing, ROI, funding, allocations, or affordability.
- marketing: Questions about product promotion, customer acquisition, launch strategy, messaging, positioning, market research, or branding.
- legal: Questions about laws, regulations, compliance, data protection, contracts, intellectual property, or regional legal constraints.

Return ONLY a comma-separated list of the relevant categories in lowercase (e.g., "budget, legal"). Do not include explanations or any extra words.

You may return more than one category, ONLY if the query clearly spans distinct responsibilities. Be conservative.
"""

    completion = client.chat.completions.create(
        model=HF_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )

    category = completion.choices[0].message.content.strip().lower()
    print(category)
    return {"query": query, "category": category}