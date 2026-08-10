from services.llm import generate_response
from prompts.shopping_prompt import create_planner_prompt


class ShoppingPlanner:

    def create_plan(self, product, budget, preferences):

        prompt = create_planner_prompt(
            product,
            budget,
            preferences
        )

        plan = generate_response(prompt)

        return plan