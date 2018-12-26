def value(hand):
    ranks = []
    suits = []
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank.isdigit():
            ranks.append(int(rank))
        else:
            ranks.append({'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}[rank])
        suits.append(suit)
    ranks.sort()
    
    flush = len(set(suits)) == 1
    
    straight = True
    for i in range(1, 5):
        if ranks[i] != ranks[i-1] + 1:
            straight = False

    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    counts = sorted(rank_counts.values(), reverse=True)
    
    if flush and straight: combo = 8
    elif 4 in counts: combo = 7
    elif [3, 2] == counts: combo = 6
    elif flush: combo = 5
    elif straight: combo = 4
    elif 3 in counts: combo = 3
    elif counts == [2, 2, 1]: combo = 2
    elif 2 in counts: combo = 1
    else: combo = 0

    high_cards = []
    rank_counts_copy = dict(rank_counts)
    for high_count in counts:
        high_card = 0
        for rank, count in rank_counts_copy.items():
            if count == high_count and rank > high_card:
                high_card = rank
        high_cards.append(high_card)
        del rank_counts_copy[high_card]

    return [combo] + high_cards

count = 0
with open('054.txt') as text:
    for line in text:
        l = line.split()
        p1 = [l[i] for i in range(5)]
        p2 = [l[i] for i in range(5, 10)]
        if value(p1) > value(p2):
            count += 1
print(count)
