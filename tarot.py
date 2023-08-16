import streamlit as st
import openai
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

def get_tarot_reading(spread, question, holistic=False):
    model = "gpt-3.5-turbo"
    prompt_content = f"You are a wise and knowledgeable tarot reader. Given the spread: {spread}, provide a holistic interpretation."
    chat_log = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': prompt_content}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=chat_log,
        max_tokens=200
    )
    return response['choices'][0]['message']['content'].strip()

# An option to either ask a question or get a general reading
st.title('🔮 Tarot Habibi - by Hammoud 🔮')
st.write('Welcome to Tarot Habibi! Choose to either ask a question and draw the cards for a detailed reading, or select an area for a general reading.')

reading_type = st.radio('What type of reading do you want?', ('Ask a question', 'General reading'))

if reading_type == 'Ask a question':
    if st.button('Ask a question about my love life'):
        question = "What will happen in my love life?"
    elif st.button('Ask a question about my professional life'):
        question = "What will happen in my professional life?"
    elif st.button('Ask a question about my emotional life'):
        question = "What will happen in my emotional life?"
    elif st.button('Ask a question about my friendships'):
        question = "What will happen in my friendships?"
    
    if question:
        spread = random.sample(tarot_deck, 10)  # Draw 10 cards for the spread
        reading = get_tarot_reading(spread, question, holistic=True)
        st.write(reading)
elif reading_type == 'General reading':
    if st.button('Get a general reading about my love life'):
        area = "love life"
    elif st.button('Get a general reading about my professional life'):
        area = "professional life"
    elif st.button('Get a general reading about my emotional life'):
        area = "emotional life"
    elif st.button('Get a general reading about my friendships'):
        area = "friendships"
    
    if area:
        reading = get_general_reading(area)
        st.write(reading)
