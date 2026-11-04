# AI Travel Planner Agent

An AI-powered travel planning application built using Python, Streamlit, and Google Gemini API.

## Overview

The AI Travel Planner helps users generate personalized travel plans based on their destination and travel requirements.

It uses a large language model to understand user inputs and generate structured travel recommendations.

## Problem Statement

Planning a trip involves researching destinations, organizing activities, and preparing a suitable itinerary.

This project aims to simplify the planning process through an AI-powered conversational application.

## Key Features

- AI-powered travel recommendations.
- Natural-language user input.
- Personalized itinerary generation.
- Interactive Streamlit interface.
- Google Gemini API integration.

## Technology Stack

- Programming Language: Python
- Frontend: Streamlit
- LLM: Google Gemini API
- API Integration: Gemini API

## How It Works

1. The user enters their travel requirements.
2. The application collects the input.
3. The input is passed to the Gemini API.
4. The model processes the request.
5. The application receives the generated travel plan.
6. The itinerary is displayed through the Streamlit interface.

## Project Structure

```text
travel-planner-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/savuniharika/travel-planner-agent.git
cd travel-planner-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gemini API key using an environment variable or Streamlit secrets, according to the application configuration.

Run the application:

```bash
streamlit run app.py
```

## Future Improvements

- Add budget-based travel recommendations.
- Integrate real-time weather information.
- Add hotel and transportation APIs.
- Generate day-wise travel schedules.
- Add conversational memory.
- Validate recommendations using external sources.
