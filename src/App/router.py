from semantic_router import Route, RouteLayer
from semantic_router.encoders import CohereEncoder  # ✅ this works in v0.0.15
from dotenv import load_dotenv
import os

load_dotenv()  # this loads .env into environment variables


# You must have a Cohere API key set as environment variable:
# export COHERE_API_KEY="your-key"

embedding_model = CohereEncoder()

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
    ]
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        
    ]
)

small_talk = Route(
    name="small-talk",
    utterances=[
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
    ]
)

router = RouteLayer(
    routes=[faq, sql, small_talk],
    encoder=embedding_model  # ✅
)

if __name__ == "__main__":
    result = router("Do I get discount on credit card?")
    print(result.name)
