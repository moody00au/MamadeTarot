import streamlit as st
import openai
from openai import ChatCompletion
import random
from RWdeck import tarot_deck

# Use the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Define the positions in the Celtic Cross spread
celtic_cross_positions = [
    'The Present',
    'The Challenge',
    'The Past',
    'The Future',
    'Above',
    'Below',
    'Advice',
    'External Influences',
    'Hopes and Fears',
    'Outcome'
]

def get_tarot_reading(spread, question):
    model = "gpt-3.5-turbo"
    messages = [
        {"role": "system", "content": "You are a wise and knowledgeable tarot reader. You understand the associations and constellations of the tarot cards, and you can provide detailed interpretations including 2nd, 3rd, and 4th degree associations."},
        {"role": "user", "content": question},
        {"role": "user", "content": f"Please provide a detailed reading for this Celtic Cross spread: {spread}. I would like a summary of the reading first, followed by a detailed interpretation of each card."}
    ]
    response = ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']

st.title('Tarot Reading App')

# User enters their question
question = st.text_input('What is your question?')

# Initialize spread as an empty dictionary
spread = {}

# User clicks to draw cards for the spread
if st.button('Draw Cards'):
    deck = tarot_deck.copy()  # Make a copy of the deck to draw from
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)  # Remove the card from the deck
        spread[position] = card
        st.write(f"{position}: {card}")

    # Get tarot reading from GPT-3.5 Turbo
    reading = get_tarot_reading(spread, question)
    st.write(reading)
