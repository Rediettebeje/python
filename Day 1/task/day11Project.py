import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(nums):
    if 10 in nums and 11 in nums and len(nums) == 2:
        return 0
    if 11 in nums and sum(nums) > 21:
        nums.remove(11)
        nums.append(1)
    return sum(nums)




