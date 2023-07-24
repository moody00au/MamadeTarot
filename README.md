# MamadeTarot
Silly (or deep and mysterious) tarot readings using GPT4

# Tarot Reading App

This is a Streamlit app that uses OpenAI's GPT-4 model to provide tarot readings. The user can draw cards for a Celtic Cross spread, and the app will provide a detailed interpretation of the spread, including 2nd, 3rd, and 4th degree associations and constellations.

## How to run the app

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.

## How to deploy the app on Streamlit sharing

1. Push your repository to GitHub.
2. Go to the [Streamlit sharing dashboard](https://share.streamlit.io/) and log in.
3. Select your app from the list of your GitHub repos.
4. Click on the 'Edit Secrets' button.
5. Add your OpenAI API key in the following format:

[openai]
api_key = 'your-openai-api-key'
