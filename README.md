# AIge Shopping — AI Shopping Agent

AIge Shopping is an AI-powered shopping assistant that helps users find the best product based on their **budget and preferences**.

## Features

- Search for products using natural language
- Consider user budget and preferences
- Use AI to analyze shopping requirements
- Search products using browser automation
- Compare available products
- Recommend the most suitable product

## How It Works

```text
User Input
    ↓
Gemini AI
    ↓
Playwright Product Search
    ↓
Product Information
    ↓
AI Recommendation
    ↓
Best Product
```

# Workflow
The user enters:
Product requirement
Budget
Preferences
The request is sent from the React frontend to the FastAPI backend.
The Gemini-powered planner analyzes the shopping requirement.
Playwright opens the browser and searches for relevant products.
Product information is extracted from the search results.
The recommendation agent analyzes the available products against the user's requirements.
The final recommendation is returned to the React frontend and displayed to the user.

# Tech Stack
## Frontend
React,
JavaScript,
CSS,
Vite
## Backend
Python,
FastAPI
## AI
Google Gemini API
## Browser Automation
Playwright
## Other Tools
Pydantic,
python-dotenv

# Project Goal

The goal of AIge Shopping is to build an AI agent that can assist users in making better shopping decisions instead of manually searching and comparing products.