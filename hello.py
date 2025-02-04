def match(a, b):
    if len(a) == 1 or len(b) == 1:
        if a == b: return True
        wild, normal = (a, b) if len(a) == 1 else (b, a)
        if len(normal) != 3: return False
        return any([
            wild in 'RYGB' and wild == normal[0],
            wild in '1234' and wild == normal[1],
            wild in 'XOST' and wild == normal[2]
        ])
    return sum(c1 == c2 for c1, c2 in zip(a, b)) == 2

def printResult(piles, hand, drawPile):
    p = piles.split()
    hand = hand.split()
    draw = drawPile.split()
    current_pile = None

    while True:
        played = False
        for i, card in enumerate(hand):
            for pile_idx in range(2):
                if match(card, p[pile_idx]):
                    p[pile_idx] = hand.pop(i)
                    current_pile = pile_idx
                    played = True
                    break
            if played: break
        
        if not played:
            while len(hand) < 7 and draw:
                hand.append(draw.pop(0))
            if all(not match(c, pile) for c in hand for pile in p):
                break
            continue
        
        while True:
            found = False
            for i, card in enumerate(hand):
                if match(card, p[current_pile]):
                    p[current_pile] = hand.pop(i)
                    found = True
                    break
            if not found: break

        while len(hand) < 7 and draw:
            hand.append(draw.pop(0))

        if not hand and not draw:
            break

    return f"{len(hand)} {p[0]} {p[1]}"

piles = "G4T Y2S"
hand = "B4O G4X B1O G4O R4O R1O 1"
drawPile = "Y2T G3T Y4O G2T Y2O"

print(printResult(piles, hand, drawPile))
