def create_planner_prompt(product, budget, preferences):

    return f"""
You are an AI shopping planning assistant.

The user is looking for:
Product: {product}

Budget: {budget}

Preferences:
{preferences}

Create a simple shopping plan for finding the most suitable product.

Consider:
- User's budget
- User's preferences
- Important features to look for
- What type of products should be compared

Return a clear and practical shopping plan.
"""