import streamlit as st
import openai
from openai import ChatCompletion
import random
from RWdeck import tarot_deck

# Define a dictionary of tarot cards
tarot_deck = [
    'The Fool',
    'The Magician',
    'The High Priestess',
    'The Empress',
    'The Emperor',
    'The Hierophant',
    'The Lovers',
    'The Chariot',
    'Strength',
    'The Hermit',
    'Wheel of Fortune',
    'Justice',
    'The Hanged Man',
    'Death',
    'Temperance',
    'The Devil',
    'The Tower',
    'The Star',
    'The Moon',
    'The Sun',
    'Judgement',
    'The World',
    'Ace of Cups',
    'Two of Cups',
    'Three of Cups',
    'Four of Cups',
    'Five of Cups',
    'Six of Cups',
    'Seven of Cups',
    'Eight of Cups',
    'Nine of Cups',
    'Ten of Cups',
    'Page of Cups',
    'Knight of Cups',
    'Queen of Cups',
    'King of Cups',
    'Ace of Pentacles',
    'Two of Pentacles',
    'Three of Pentacles',
    'Four of Pentacles',
    'Five of Pentacles',
    'Six of Pentacles',
    'Seven of Pentacles',
    'Eight of Pentacles',
    'Nine of Pentacles',
    'Ten of Pentacles',
    'Page of Pentacles',
    'Knight of Pentacles',
    'Queen of Pentacles',
    'King of Pentacles',
    'Ace of Swords',
    'Two of Swords',
    'Three of Swords',
    'Four of Swords',
    'Five of Swords',
    'Six of Swords',
    'Seven of Swords',
    'Eight of Swords',
    'Nine of Swords',
    'Ten of Swords',
    'Page of Swords',
    'Knight of Swords',
    'Queen of Swords',
    'King of Swords',
    'Ace of Wands',
    'Two of Wands',
    'Three of Wands',
    'Four of Wands',
    'Five of Wands',
    'Six of Wands',
    'Seven of Wands',
    'Eight of Wands',
    'Nine of Wands',
    'Ten of Wands',
    'Page of Wands',
    'Knight of Wands',
    'Queen of Wands',
    'King of Wands'
]

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
        {"role": "system", "content": "You are a wise and knowledgeable tarot reader with a mystical personality. You understand the associations and constellations of the tarot cards, and you can provide detailed interpretations including 2nd, 3rd, and 4th degree associations."},
        {"role": "user", "content": question},
        {"role": "user", "content": f"Please provide a detailed reading for this Celtic Cross spread: {spread}. I would like a summary of the reading first, followed by a detailed interpretation of each card. Please provide the reading in both English and Arabic, with the English reading first."}
    ]
    response = ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']

st.title('🔮 Madame Tarot Habibi - Made by Hammoud 🔮')

st.write('Welcome, my child. The more detail you provide in your question, the more detail I can provide in your reading. Please enter your question below. 🌟')

# User enters their question
question = st.text_input('What is your question? ما هو سؤالك؟')

# Initialize spread as an empty dictionary
spread = {}

# User clicks to draw cards for the spread
if st.button('Draw Cards 🃏'):
    deck = tarot_deck.copy()  # Make a copy of the deck to draw from
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)  # Remove the card from the deck
        spread[position] = card
        st.write(f"{position}: {card}")

    # Get tarot reading from GPT-3.5 Turbo
    reading = get_tarot_reading(spread, question)
    st.write(reading)
