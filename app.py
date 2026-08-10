from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import ShoppingRequest
from agent.planner import ShoppingPlanner
from agent.recommender import RecommendationAgent
from services.browser import BrowserService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://aige-shopping.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Shopping Agent is running!"
    }


@app.post("/recommend")
def recommend(request: ShoppingRequest):

    # Step 1: Create shopping plan
    planner = ShoppingPlanner()

    plan = planner.create_plan(
        request.product,
        request.budget,
        request.preferences
    )

    # Step 2: Search products
    browser = BrowserService()

    products = browser.search_amazon(
        request.product
    )

    # Step 3: Generate recommendation
    recommender = RecommendationAgent()

    recommendation = recommender.recommend(
        products,
        request.budget,
        request.preferences
    )

    # Step 4: Return everything
    return {
        "product": request.product,
        "budget": request.budget,
        "preferences": request.preferences,
        "plan": plan,
        "products": products,
        "recommendation": recommendation
    }