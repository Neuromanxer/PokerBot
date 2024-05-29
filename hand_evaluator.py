# poker_bot/game_engine/hand_evaluator.py

from collections import Counter

def evaluate_hand(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    if len(set(suits)) == 1:  # All cards of the same suit
        if ranks == ['10', 'J', 'Q', 'K', 'A']:
            return 'Royal Flush'
        return 'Flush'
    
    if 4 in rank_counts.values():
        return 'Four of a Kind'
    
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return 'Full House'

    # Continue with other hand evaluations...

    return 'High Card'

# Add more evaluation logic as needed.
