import openai
from poker_bot.game_engine.game_logic import PokerGame
from poker_bot.chat.ChatGPT_integration import chat_with_gpt,construct_prompt
# Define the number of players including ChatGPT
NUM_PLAYERS = 3

openai.api_key = "OPEN-AI-KEY"
def main():
    game = PokerGame()
    game.add_player('Alice')
    game.add_player('Bob')
    game.add_player('ChatGPT')  # Add ChatGPT as a player
    game.deal_hands()
    game.deal_community_cards(3)  # Flop
    game.deal_community_cards(1)  # Turn
    game.deal_community_cards(1)  # River
    game.evaluate_players()

    while not game.is_game_over():
        # Get ChatGPT's move
        user_input = construct_prompt(game.get_game_state())
        chatgpt_move = chat_with_gpt(user_input)
        
        # Make ChatGPT's move
        game.make_move('ChatGPT', chatgpt_move)

        # Make moves for Alice and Bob
        # Implement your logic here for Alice and Bob's moves
        
        # Deal community cards
        game.deal_community_cards(1)  # Deal one community card
        game.evaluate_players()  # Evaluate player hands
        
    print("Game over!")
    game.show_winner()

def construct_prompt(game_state):
    # Construct the prompt based on the current game state
    # This could involve providing information about the current hand, community cards, player actions, etc.
    # Adjust this according to your specific poker game implementation
    prompt = "Current poker game state:\n"
    for player_name, hand in game_state['hands'].items():
        prompt += f"{player_name}'s Hand: {hand}\n"
    prompt += f"Community cards: {game_state['community_cards']}\n"
    # Add other relevant information as needed
    return prompt

if __name__ == "__main__":
    main()