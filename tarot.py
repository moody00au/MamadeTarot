import streamlit as st
import openai
from openai import ChatCompletion
import random


# Use the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

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
    model = "gpt-4"
    position, card = list(spread.items())[0]  # Extract the single position and card from the spread
    messages = [
        {"role": "system", "content": "You are a wise and knowledgeable tarot reader. Provide a detailed interpretation of the card, explaining the process of tarot reading and its significance. Ensure the reading is beginner-friendly."},
        {"role": "user", "content": question},
        {"role": "user", "content": f"Please provide a detailed reading for the card {card} in the position {position}."}
    ]
    response = ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']

st.title('🔮 Tarot Habibi - by Hammoud 🔮')
st.write('Welcome to Tarot Habibi! This app provides tarot card readings using the Celtic Cross spread. Simply enter your question and draw the cards to receive insights into various aspects of your life. If you\'re new to tarot, don\'t worry! Each card\'s meaning will be explained in detail. Ready to begin? Please enter your question below:')

# User enters their question
question = st.text_input('What troubles you my child?')

# Initialize spread as an empty dictionary
spread = {}

# User clicks to draw cards for the spread
if st.button('Draw Cards 🃏'):
    deck = tarot_deck.copy()
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)
        st.write(f"{position}: {card}")
        
        # Get tarot reading for the drawn card
        reading = get_tarot_reading({position: card}, question)
        st.write(reading)
