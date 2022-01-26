

def deal_hands(deck, per_hand_amount=5):
    """deals to each player hand"""
    player_hand = [deck[i] for i in range(per_hand_amount)]
    cpu_hand = [deck[i + 5] for i in range(per_hand_amount)]
    for i in range(10):
        deck.pop(0)
    return player_hand, cpu_hand
