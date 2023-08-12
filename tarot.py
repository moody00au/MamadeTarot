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

def get_tarot_reading(spread, question, holistic=False, conversation_history=[]):
    model = "gpt-3.5-turbo"
    if not holistic and spread:
        position, card = list(spread.items())[0]
        new_message = {"role": "user", "content": f"Please provide a concise - one line reading for the card {card} in the position {position}."}
    elif holistic:
        new_message = {"role": "user", "content": f"Please provide a relational reading for this spread: {spread}."}
    else:  # This handles the follow-up questions
        new_message = {"role": "user", "content": question}
    
    conversation_history.append(new_message)
    response = ChatCompletion.create(model=model, messages=conversation_history)
    conversation_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content']

st.title('🔮 Tarot Habibi - by Hammoud 🔮')
st.write('Welcome to Tarot Habibi! This app provides tarot card readings using the Celtic Cross spread. Simply enter your question and draw the cards to receive insights into various aspects of your life. If you\'re new to tarot, don\'t worry! Each card\'s meaning will be explained in detail. Ready to begin? Please enter your question below:')

# Initialize session state variables if they don't exist
if 'spread' not in st.session_state:
    st.session_state.spread = {}
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = [
        {"role": "system", "content": "You are a wise and knowledgeable tarot reader. Provide detailed interpretations of the cards, considering relationships between them. Ensure the reading is beginner-friendly."},
    ]
if 'spread_drawn' not in st.session_state:
    st.session_state.spread_drawn = False

# Display the entire conversation history
for message in st.session_state.conversation_history:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Assistant: {message['content']}")

# User enters their question
question = st.text_input('What troubles you my child?')

# User clicks to draw cards for the spread
if st.button('Draw Cards 🃏') and question:
    st.session_state.spread_drawn = True
    st.session_state.conversation_history.append({"role": "user", "content": question})
    deck = tarot_deck.copy()
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)
        st.session_state.spread[position] = card
        st.write(f"{position}: {card}")
        
        # Get tarot reading for the drawn card
        reading = get_tarot_reading({position: card}, question, conversation_history=st.session_state.conversation_history)
        st.session_state.conversation_history.append({"role": "assistant", "content": reading})
        st.write(reading)
    
    # Get a holistic reading of the entire spread
    holistic_reading = get_tarot_reading(st.session_state.spread, question, holistic=True, conversation_history=st.session_state.conversation_history)
    st.session_state.conversation_history.append({"role": "assistant", "content": holistic_reading})
    st.write("Holistic Reading of the Spread:")
    st.write(holistic_reading)

# Allow user to ask follow-up questions
if st.session_state.spread_drawn:
    follow_up_question = st.text_input('Do you have any follow-up questions?')
    if st.button('Submit Follow-up'):
        st.session_state.conversation_history.append({"role": "user", "content": follow_up_question})
        follow_up_response = get_tarot_reading({}, follow_up_question, conversation_history=st.session_state.conversation_history)
        st.session_state.conversation_history.append({"role": "assistant", "content": follow_up_response})
        st.write(follow_up_response)
