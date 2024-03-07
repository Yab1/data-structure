"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""


# Solution using Linear Search
def linear_search(cards, target):
    for index in range(len(cards)):
        if cards[index] == target:
            return index
    return -1


# Solution using Binary Search
def binary_search(cards, target):
    lower_bound, upper_bound = 0, len(cards) - 1

    while lower_bound <= upper_bound:
        middle = (upper_bound + lower_bound) // 2
        if cards[middle] == target:
            return middle
        elif cards[middle] < target:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return -1


# Solutin using Recursive Binary Search
def recursive_binary_search(cards, target):
    lower_bound, upper_bound = 0, len(cards) - 1
    if not len(cards) == 0:
        middle = (upper_bound + lower_bound) // 2
        if cards[middle] == target:
            return True
        else:
            if cards[middle] < target:
                recursive_binary_search(cards[: middle - 1], target)
            else:
                recursive_binary_search(cards[middle + 1 : len(cards)], target)
    else:
        return False


tests = []

tests.append({"input": {"cards": [13, 12, 11, 10, 9, 8, 7], "target": 7}, "output": 6})
tests.append({"input": {"cards": [8, 7, 6, 5, 4, 3, 2, 1], "target": 1}, "output": 7})

print(
    "Linear Search: ",
    linear_search(**tests[1]["input"]) == tests[1]["output"],
)
print("Binary Search: ", binary_search(**tests[1]["input"]) == tests[1]["output"])
print("Recursive Binary Search :", recursive_binary_search([8, 7, 6, 5, 4, 3, 2, 1], 1))
