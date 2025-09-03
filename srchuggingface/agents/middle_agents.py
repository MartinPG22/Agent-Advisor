import json
from huggingface import client
from config import HF_MODEL

def budget_agent(state):
    query = state["query"]
    prompt = f"""
You are BudgetExpert, a senior financial strategist at a multinational consulting firm. You evaluate whether plans are financially viable, estimate costs, and assess remaining budgets.

Your task:
- Decide if the plan in the query is financially feasible.
- Estimate the cost and remaining budget.
- Justify your answer clearly.

Return ONLY a valid JSON object with the following format (do not explain or include anything outside the JSON):
{{
  "can_afford": bool,
  "estimated_cost": int,
  "budget_remaining": int,
  "rationale": str
}}

Query: "{query}"
"""
    completion = client.chat.completions.create(
        model=HF_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = completion.choices[0].message.content
    print("API response:", answer)
    try:
        parsed = json.loads(answer)
    except Exception:
        parsed = {"can_afford": False, "estimated_cost": 0, "budget_remaining": 0, "rationale": "Parsing error."}
    return {"answer_budget": parsed}

def legal_agent(state):
    query = state["query"]
    prompt = f"""
You are LegalExpert, a regulatory compliance officer with expertise in GDPR, international law, and product liability.

Your task:
- Analyze the legal feasibility of the plan described in the query.
- Identify potential legal issues or compliance risks.
- Offer a brief recommendation.

Return ONLY a valid JSON object with the following format (do not explain or include anything outside the JSON):
{{
  "compliant": bool,
  "issues": [str],
  "recommendation": str
}}

Query: "{query}"
"""
    completion = client.chat.completions.create(
        model=HF_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = completion.choices[0].message.content
    print("API response:", answer)
    try:
        parsed = json.loads(answer)
    except Exception:
        parsed = {"compliant": False, "issues": ["Parsing error"], "recommendation": "Review input or system."}
    return {"answer_legal": parsed}

def marketing_agent(state):
    query = state["query"]
    prompt = f"""
You are MarketingExpert, a global brand strategist specializing in launch strategy, positioning, and audience fit.

Your task:
- Evaluate the marketing fit of the proposed plan.
- Suggest effective channels and a launch tagline.
- Tailor recommendations to the likely region and target audience.

Return ONLY a valid JSON object with the following format (do not explain or include anything outside the JSON):
{{
  "launch_score": int,
  "channels": [str],
  "tagline": str
}}

Query: "{query}"
"""
    completion = client.chat.completions.create(
        model=HF_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = completion.choices[0].message.content
    print("API response:", answer)
    try:
        parsed = json.loads(answer)
    except Exception:
        parsed = {"launch_score": 0, "channels": [], "tagline": "Parsing error."}
    return {"answer_marketing": parsed}