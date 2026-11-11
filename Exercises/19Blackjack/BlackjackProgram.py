# ==========================================
# Exercise 19: Blackjack (21) Card Game
# ==========================================
#
# Overview:
# Build a terminal-based Blackjack game where the player plays against the dealer (computer).
#
# Requirements & Rules:
# 1. Card Deck & Values:
#    - Represent cards (2-10 count as face value, J, Q, K count as 10, Ace counts as 11 or 1).
#    - Create and shuffle a standard deck of 52 playing cards (or infinite deck using random).
# 2. Initial Deal:
#    - Deal 2 cards to the player and 2 cards to the dealer.
#    - Show both player cards, but hide one of the dealer's cards until their turn.
# 3. Player Turn:
#    - Display player's current hand and score.
#    - Allow the player to choose 'Hit' (draw another card) or 'Stand' (end turn).
#    - If player score exceeds 21 -> Player busts (Dealer wins).
# 4. Dealer Turn:
#    - Reveal the dealer's hidden card.
#    - Dealer must hit if total score is under 17, and stand on 17 or higher.
# 5. Ace Handling:
#    - If total score exceeds 21 and the hand contains an Ace valued at 11, adjust Ace value to 1.
# 6. Determine Winner & Betting (Optional):
#    - Compare scores: higher score <= 21 wins, equal score is a tie/push.
#    - Track player balance and bets across rounds (like Slot Machine / ATM exercises).
#
# Suggested Functions:
# - create_deck()
# - deal_card(deck)
# - calculate_score(hand)
# - display_hands(player_hand, dealer_hand, hide_dealer=True)
# - main()
#
# Write your code below:
