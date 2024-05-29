from poker_bot.game_engine.deck import Deck
from poker_bot.game_engine.hand_evaluator import evaluate_hand

class PokerGame:
    def __init__(self):
        self.players = []
        self.deck = Deck()  # Initialize a Deck object
        self.rounds_played = 0  # Initialize rounds_played attribute
        self.max_rounds = 10  # Set the maximum number of rounds here
        self.community_cards = []  # Initialize an empty list for community cards

    def add_player(self, player_name):
        self.players.append({'name': player_name, 'hand': []})

    def deal_hands(self):
        for player in self.players:
            player['hand'] = self.deck.deal(2)

    def deal_community_cards(self, num_cards):
        self.community_cards.extend(self.deck.deal(num_cards))

    def evaluate_players(self):
        for player in self.players:
            combined_hand = player['hand'] + self.community_cards
            player['best_hand'] = evaluate_hand(combined_hand)

    def get_game_state(self):
        game_state = {
            'players': self.players,
            'community_cards': self.community_cards,
            # Add 'hand' information for each player
            'hands': {player['name']: player['hand'] for player in self.players}
        }
        return game_state

    def show_winner(self):
        winners = []
        best_hand = None
        for player in self.players:
            if best_hand is None or player['best_hand'] > best_hand:
                winners = [player['name']]
                best_hand = player['best_hand']
            elif player['best_hand'] == best_hand:
                winners.append(player['name'])

        if len(winners) == 1:
            print(f"The winner is: {winners[0]} with {best_hand}")
        elif len(winners) > 1:
            print(f"It's a tie between: {', '.join(winners)} with {best_hand}")
        else:
            print("No winner. It's a draw.")

    def is_game_over(self):
        # Check if the game is over based on certain conditions
        # For example, if there's only one player left or if the maximum number of rounds is reached
        if len(self.players) == 1:
            return True  # Game is over if there's only one player left
        elif self.rounds_played >= self.max_rounds:
            return True  # Game is over if the maximum number of rounds is reached
        else:
            return False  # Game is not over yet

    # Continue adding other game logic methods...
    def make_move(self, player_name, move):
        # Find the player making the move
        current_player = None
        for player in self.players:
            if player['name'] == player_name:
                current_player = player
                break
        
        # Check if the player exists
        if current_player is None:
            print(f"Player {player_name} not found.")
            return
        
        # Implement logic based on the move
        if move == "check":
            print(f"{player_name} checks.")
            # Implement check logic here
        elif move == "bet":
            print(f"{player_name} bets.")
            # Implement bet logic here
        elif move == "fold":
            print(f"{player_name} folds.")
            # Implement fold logic here
        else:
            print(f"Invalid move '{move}'.")

# Example usage
if __name__ == "__main__":
    main()
