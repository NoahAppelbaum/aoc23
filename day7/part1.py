nums = "123456789"

card_values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
for n in nums:
    card_values[n] = int(n)

lines = [line.strip() for line in open("in.txt")]

hands = []
for l in lines:
    parts = l.split(" ")
    hands.append((parts[0], parts[1]))


def score_hand(hand):
    freqs = {}
    for card in hand:
        freqs[card] = freqs.get(card,0) + 1

    if len(freqs) == 1:
        return 7
