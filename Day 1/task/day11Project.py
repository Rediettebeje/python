import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# random.sample() function select unique two random numbers
# randomComputerNo = random.sample(cards, 2)

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

is_game_over = False
while  not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(user_score)
    print(computer_score)
    # print(user_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        ask_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if ask_user == "y":
            user_cards.append(deal_card())
            print(user_cards)
        else:
            is_game_over = True

    print(user_score)



