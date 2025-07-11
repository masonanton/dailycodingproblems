# Card Game Simulation
#
# There are N players, each starting with their own deck of cards (top of deck is first in list).
# Each round, every player with at least one card plays their top card. The player with the highest card wins the round and collects all cards played that round, placing them at the bottom of their deck.
# If two or more players tie for the highest card, a tie-breaker is triggered:
#   - Each tied player must skip their next three cards (place them in a temporary pile).
#   - Then, each tied player plays their next available card to compare again.
#   - If another tie occurs, repeat the tie-breaker process among only the tied players.
#   - When a single player finally wins the tie-breaker, they collect all cards played and all skipped cards from all tie-break rounds.
# If a tied player does not have enough cards to skip or play, they use as many as possible; if they run out of cards during a tie-break, they are eliminated from the game.
# The game continues until only one player has cards. That player is the winner.
#
# Input:
#   - N: integer, number of players
#   - decks: List[List[int]], where decks[i] is player i's starting deck (top card first)
#
# Output:
#   - winner: integer, index (0-based) of the winning player
#
# Example:
# Input:
#   N = 3
#   decks = [
#     [10, 7, 3],
#     [8, 9, 2],
#     [10, 4, 6]
#   ]
# Output:
#   0
#
# Implement the function below:


from collections import deque

def card_game_winner(N, decks):
    still_in = set(i for i in range(N))
    decks = [deque(deck) for deck in decks]

    def play_round(table_cards):
        max_card = -1
        winners = []
        for i in list(still_in):
            if decks[i]:
                card_to_play = decks[i].popleft()
                table_cards.append(card_to_play)
                if card_to_play > max_card:
                    max_card = card_to_play
                    winners = [i]
                elif card_to_play == max_card:
                    winners.append(i)
            else:
                still_in.discard(i)
        return winners

    def tie_break(tied_players, table_cards):
        max_card = -1
        next_winners = []
        eliminated = []
        for winner in tied_players:
            # Skip next 3 cards or as many as possible
            skips = min(3, len(decks[winner]))
            for _ in range(skips):
                table_cards.append(decks[winner].popleft())
            # If player still has a card, play it; otherwise, eliminate them
            if decks[winner]:
                card_to_play = decks[winner].popleft()
                table_cards.append(card_to_play)
                if card_to_play > max_card:
                    max_card = card_to_play
                    next_winners = [winner]
                elif card_to_play == max_card:
                    next_winners.append(winner)
            else:
                eliminated.append(winner)
        # Remove eliminated players
        for p in eliminated:
            still_in.discard(p)
        # If tie remains, recurse; else, return winner(s)
        if len(next_winners) > 1:
            return tie_break(next_winners, table_cards)
        else:
            return next_winners

    while sum(1 for i in still_in if decks[i]) > 1:
        table_cards = []
        winners = play_round(table_cards)
        if len(winners) > 1:
            winners = tie_break(winners, table_cards)
        decks[winners[0]].extend(table_cards)
        # Remove eliminated players who have empty decks
        for i in list(still_in):
            if not decks[i]:
                still_in.discard(i)

    for i in range(N):
        if decks[i]:
            return i

N = 3
decks = [
    [10, 7, 3],  # Player 0
    [8, 9, 2],   # Player 1
    [10, 4, 6]   # Player 2
]

# expected winner = 0
print(card_game_winner(N, decks))




