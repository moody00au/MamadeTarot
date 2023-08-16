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

# User enters their question or chooses a general reading
reading_type = st.radio('What type of reading do you want?', ('Ask a question', 'General reading'))

if reading_type == 'Ask a question':
    # User enters their question
    question = st.text_input('What troubles you my child?')
    # If user inputs a question, proceed with spread
    if question:
        if st.button('Draw Cards 🃏'):
            deck = tarot_deck.copy()
            drawn_spread = {}  # To save the drawn spread for holistic reading
            for position in celtic_cross_positions:
                card = random.choice(deck)
                deck.remove(card)

                # Save the drawn card to the spread
                drawn_spread[position] = card

                # Display card name, position, and description
                st.write(f"**{position}: {card}** - {position_descriptions[position]}")

                # Get tarot reading for the drawn card
                if position == 'Outcome':
                    reading = get_tarot_reading(drawn_spread, question, holistic=True)
                else:
                    reading = get_tarot_reading({position: card}, question)
                st.write(reading)

elif reading_type == 'General reading':
    # User selects an area for a general reading
    area = st.selectbox('Select an area:', ('Professional', 'Love', 'Emotional', 'Friends'))
    if st.button('Get General Reading 🃏'):
        st.write(get_general_reading(area))
