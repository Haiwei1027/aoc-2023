import re
cards = ['A', 'K', 'Q','J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards.reverse()
joker_cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
joker_cards.reverse()
FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0
type_patterns = {FIVE_OF_A_KIND:r'5',FOUR_OF_A_KIND:r'41',
                 FULL_HOUSE:r'32',THREE_OF_A_KIND:r'3.*',
                 TWO_PAIR:r'221',ONE_PAIR:r'2.*'}

def check_type(hand,joker_rule=False):
    occurance = {}
    for card in hand:
        if joker_rule and card == 'J':
            continue
        if card not in occurance:
            occurance[card] = 0
        occurance[card] += 1
    pattern = sorted(list(occurance.values()),reverse=True)
    if joker_rule:
        if len(pattern) != 0:
            pattern[0] += hand.count('J')
        else:
            pattern = [5]
    for type in type_patterns:
        if re.match(type_patterns[type],"".join([str(n) for n in pattern])):
            return type
    return HIGH_CARD

def get_hand_power_base(hand,joker_rule=False):
    power = (13**6)*check_type(hand[0],joker_rule=joker_rule)
    for i,card in enumerate(hand[0]):
        unit = 13**(4-i)
        if joker_rule:
            power += joker_cards.index(card) * unit
        else:
            power += cards.index(card) * unit
    return power

def get_hand_power(hand):
    return get_hand_power_base(hand,joker_rule=False)

def get_hand_power_joker(hand):
    return get_hand_power_base(hand,joker_rule=True)

def part1(input_data):
    hands = []
    for line in input_data:
        hand, bid = line.split(" ")
        hands.append((hand,bid))
    hands.sort(key=get_hand_power)
    
    winning = 0
    for i,hand in enumerate(hands):
        bid = int(hand[1])
        rank = i+1
        winning += bid*rank
    return winning

def part2(input_data):
    hands = []
    for line in input_data:
        hand, bid = line.split(" ")
        hands.append((hand,bid))
    hands.sort(key=get_hand_power_joker)
    
    winning = 0
    for i,hand in enumerate(hands):
        bid = int(hand[1])
        rank = i+1
        winning += bid*rank
    return winning
