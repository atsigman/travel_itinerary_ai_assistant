from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config.config import GROQ_API_KEY

# Init LLM:
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
)

# Prompt for LLM:
itinerary_prompt = ChatPromptTemplate([
    ("system", "You are a helpful travel assistant. \
Create a {n_days}-day trip itinerary for {city} based upon the user's interests: {interests} \
Provide a brief, bulleted itinerary for each day of the trip."),
    ("human", "Create an itinerary for my trip.")
])


def generate_itinerary(
    n_days: int,
    city: str,
    interests: list[str],
    ) -> str:
    """
    Given input values for duration, city, and interests,
    returns an LLM response.
    """
    response = llm.invoke(
        itinerary_prompt.format_messages(
            n_days=n_days,
            city=city,
            interests=", ".join(interests)
        )
    )

    return response.content