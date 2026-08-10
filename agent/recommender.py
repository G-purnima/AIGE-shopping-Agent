import json

from services.llm import generate_response
from prompts.recom_prompt import create_recommendation_prompt


class RecommendationAgent:

    def recommend(self, products, budget, preferences):

        prompt = create_recommendation_prompt(
            products,
            budget,
            preferences
        )

        response = generate_response(prompt)

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return {
                "error": "Could not parse AI recommendation",
                "raw_response": response
            }