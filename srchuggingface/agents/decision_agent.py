import json
from huggingface import client
from config import HF_MODEL

def decision_agent(state):
    query = state.get("query", "")
    budget_info = state.get("answer_budget", {})
    legal_info = state.get("answer_legal", {})
    marketing_info = state.get("answer_marketing", {})

    print("Budget info:", budget_info)
    print("Legal info:", legal_info)
    print("Marketing info:", marketing_info)
    prompt = f"""
You are a DecisionExpert responsible for synthesizing a final recommendation based on expert input.

Original user query:
"{query}"

Expert responses:
- BudgetExpert: {budget_info}
- LegalExpert: {legal_info}
- MarketingExpert: {marketing_info}

Instructions:

1. Analyze only the responses provided. If a section is an empty object ({{}}), it means that expert has not responded. Do NOT fabricate insights for missing experts.
2. Use only the valid (non-empty) expert data to create your final decision.
3. Each insight in the output JSON must briefly summarize that expert's contribution (if available).
4. If an expert did not respond, leave their insight as an empty string ("").
5. Provide up to 3 actionable recommendations based only on the experts who responded.

Return ONLY a valid JSON object in the following format. Do not explain, comment, or print anything else:

{{
  "final_decision": str,  // One of: "Proceed", "Revise", or "Block"
  "insights": {{
    "budget": str,
    "legal": str,
    "marketing": str
  }},
  "recommendations": [str]  // Up to 3 concrete next steps
}}
"""
    completion = client.chat.completions.create(
        model=HF_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    raw_output = completion.choices[0].message.content
    print("API response:", raw_output)
    try:
        final_report = json.loads(raw_output)
    except json.JSONDecodeError:
        final_report = {"error": "Invalid JSON", "raw": raw_output}
    return {
        "final_report": final_report
    }