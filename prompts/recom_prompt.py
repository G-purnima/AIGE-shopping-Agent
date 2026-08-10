import json


def create_recommendation_prompt(products, budget, preferences):

    return f"""
You are an expert AI shopping advisor.

The user wants:
Product: {products}
Budget: ₹{budget}
Preferences: {preferences}

Analyze the available products carefully.

Choose the SINGLE best product based on:
1. Budget
2. User preferences
3. Product rating
4. Value for money

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not add any explanation outside the JSON.

Use exactly this structure:

{{
    "best_product": {{
        "name": "Product name",
        "price": "Product price",
        "rating": "Product rating"
    }},
    "score": 9.2,
    "reason": "Short explanation of why this is the best choice.",
    "pros": [
        "Advantage 1",
        "Advantage 2",
        "Advantage 3"
    ],
    "cons": [
        "Disadvantage 1",
        "Disadvantage 2"
    ]
}}

Available products:

{json.dumps(products, indent=2)}
"""