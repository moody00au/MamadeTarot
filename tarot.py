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

def trim_response_to_words(response, max_words=70):
    words = response.split()
    return ' '.join(words[:max_words])

def get_tarot_reading(spread, question, holistic=False, conversation_history=[]):
    model = "gpt-3.5-turbo"
    if not holistic:
        position, card = list(spread.items())[0]
        new_message = {"role": "user", "content": f"Please provide a concise reading for the card {card} in the position {position}."}
    else:
        new_message = {"role": "user", "content": f"Please provide a relational reading for this spread: {spread}."}
    
    conversation_history.append(new_message)
    response = ChatCompletion.create(model=model, messages=conversation_history)
    conversation_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return 

st.title('🔮 Tarot Habibi - by Hammoud 🔮')
st.write('Welcome to Tarot Habibi! This app provides tarot card readings using the Celtic Cross spread. Simply enter your question and draw the cards to receive insights into various aspects of your life. If you\'re new to tarot, don\'t worry! Each card\'s meaning will be explained in detail. Ready to begin? Please enter your question below:')

# User enters their question
question = st.text_input('What troubles you my child?')

# Initialize spread as an empty dictionary
spread = {}

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a wise and knowledgeable tarot reader. Provide detailed interpretations of the cards, considering relationships between them. Ensure the reading is beginner-friendly."},
    {"role": "user", "content": question}
]

spread_drawn = False

# User clicks to draw cards for the spread
if st.button('Draw Cards 🃏'):
    spread_drawn = True
    deck = tarot_deck.copy()
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)
        st.write(f"{position}: {card}")
        
        # Get tarot reading for the drawn card
        reading = get_tarot_reading({position: card}, question, conversation_history=conversation_history)
        st.write(reading)
    
    # Get a holistic reading of the entire spread
    holistic_reading = get_tarot_reading(spread, question, holistic=True, conversation_history=conversation_history)
    st.write("Holistic Reading of the Spread:")
    st.write(holistic_reading)

# Allow user to ask follow-up questions
if spread_drawn:
    follow_up_question = st.text_input('Do you have any follow-up questions?')
    if follow_up_question:
        conversation_history.append({"role": "user", "content": follow_up_question})
        follow_up_response = get_tarot_reading({}, follow_up_question, conversation_history=conversation_history)
        st.write(follow_up_response)
