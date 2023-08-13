import streamlit as st
import openai
from openai import ChatCompletion
import random
import requests
from bs4 import BeautifulSoup

# Use the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]


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
    position, card = list(spread.items())[0]
    
    if holistic:
        prompt_content = "You are a wise and knowledgeable tarot reader. Provide a 3-paragraph holistic interpretation without referring to the cards directly. Instead, focus on the positions and the influences and advice they represent."
    else:
        prompt_content = "You are a wise and knowledgeable tarot reader. Provide a one-paragraph interpretation of the card, explaining its significance without referring to the card directly. Ensure the reading is beginner-friendly."
    
    messages = [
        {"role": "system", "content": prompt_content},
        {"role": "user", "content": question},
        {"role": "user", "content": f"Please provide a reading for the card {card} in the position {position}."}
    ]
    response = ChatCompletion.create(model=model, messages=messages)
    return response['choices'][0]['message']['content']

def get_card_image_url(card_name):
    search_url = f"https://www.google.com/search?q=Rider+Waite+Original+{card_name}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find("img", attrs={"class": "t0fcAb"})  # Adjusted to target the correct image class
    if img_tag and 'src' in img_tag.attrs:
        return img_tag['src']
    return None

st.title('🔮 Tarot Habibi - by Hammoud 🔮')
st.write('Welcome to Tarot Habibi! This app provides tarot card readings using the Celtic Cross spread. Simply enter your question and draw the cards to receive insights into various aspects of your life. If you\'re new to tarot, don\'t worry! Each card\'s meaning will be explained in detail. Ready to begin? Please enter your question below:')

# User enters their question
question = st.text_input('What troubles you my child?')

# Initialize spread as an empty dictionary
spread = {}
holistic_reading = ""

# Descriptions for each position
position_descriptions = {
    'The Present': 'Represents your current situation.',
    'The Challenge': 'Indicates the immediate challenge or problem facing you.',
    'The Past': 'Denotes past events that are affecting the current situation.',
    'The Future': 'Predicts the likely outcome if things continue as they are.',
    'Above': 'Represents your goal or best outcome in this situation.',
    'Below': 'Reflects your subconscious influences, fears, and desires.',
    'Advice': 'Offers guidance on how to navigate the current challenges.',
    'External Influences': 'Represents external factors affecting the situation.',
    'Hopes and Fears': 'Indicates your hopes, fears, and expectations.',
    'Outcome': 'Predicts the final outcome of the situation.'
}

# User clicks to draw cards for the spread
if st.button('Draw Cards 🃏'):
    deck = tarot_deck.copy()
    for position in celtic_cross_positions:
        card = random.choice(deck)
        deck.remove(card)
        
        # Display card name, position, and description
        st.write(f"**{position}: {card}** - {position_descriptions[position]}")
        
        # Display card image
        image_url = get_card_image_url(card)
        if image_url:
            st.image(image_url, use_column_width=True)
        
        # Get tarot reading for the drawn card
        reading = get_tarot_reading({position: card}, question)
        st.write(reading)
        
        # Accumulate readings for holistic interpretation
        holistic_reading += f"For the position of {position}, {reading} "

    # Display holistic reading
    holistic_interpretation = get_tarot_reading({}, question, holistic=True)
    st.write(holistic_interpretation)
