import openai
import os

# Set the API key from an environment variable for better security
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the correct model
            messages=[
                {"role": "system", "content": "You are an expert poker player."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please check your plan and billing details.")
        return None
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request: {e}")
        return None

def construct_prompt(game_state):
    prompt = "Current poker game state:\n"
    
    # Check if the 'hand' key exists in the game_state dictionary
    if 'hand' in game_state:
        prompt += f"Hand: {game_state['hand']}\n"
    else:
        prompt += "Hand: None\n"  # If 'hand' key doesn't exist, indicate it's None
    
    prompt += f"Community cards: {game_state.get('community_cards', 'None')}\n"
    # Add other relevant information...
    
    return prompt


def extract_poker_move(response):
    # Extract the poker move from the response
    # This could involve parsing the response text to identify the intended move
    # Adjust this according to your specific poker game implementation
    poker_move = response.choices[0].text.strip()
    return poker_move