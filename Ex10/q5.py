import math

# ---------------------------- 5.a ----------------------------

def compute_budget(total_budget: float, citizen_votes: list[list]) -> list[float]:
    return find_t(0, 1, total_budget, citizen_votes)


# Find t by using binary search algorithm
def find_t(low, high, total_budget, citizen_votes) -> list[float]:
    if high >= low:
        mid = (high + low) / 2
        result = Budget_division(mid, total_budget, citizen_votes)
        # If sum of the budget = total_budget
        if sum(result) == total_budget:
            return result
        # If sum of the budget > total_budget
        elif sum(result) > total_budget:
            return find_t(low, mid, total_budget, citizen_votes)
        # Else the sum of the budget > total_budget
        else:
            return find_t(mid, high, total_budget, citizen_votes)
    else:
        # Error
        return -1


def Budget_division(t, total_budget, citizen_votes) -> list[float]:
    fixed_votes = []
    budget_div = []
    topics = list(map(list, zip(*citizen_votes)))

    # Create fixed votes list
    for i in range(1, len(citizen_votes)):
        fixed_votes.append(total_budget*min(1, i*t))

    # Add fixed votes to each topic and take the median to the budget
    for topic in topics:
        topic.extend(fixed_votes)
        topic.sort()
        budget = round(topic[math.ceil(len(topic)/2)-1], 1)
        budget_div.append(budget)

    return budget_div

# ---------------------------- 5.b ----------------------------

def Fair_to_groups(total_budget: float, citizen_votes: list[list]) -> bool:
    budget_div = compute_budget(total_budget, citizen_votes)
    Ks_groups = [0] * len(budget_div)
    # Calculates the size of Ks groups for each topic
    for element in citizen_votes:
        for index, i in enumerate(element):
            if i == total_budget:
                Ks_groups[index] += 1
    # Checks whether the budget is fair to groups for each of the topics
    for index, k in enumerate(Ks_groups):
        if (k * total_budget/len(citizen_votes)) != budget_div[index]:
            return False
    return True


if __name__ == '__main__':
    print("# ------------------ Tests 5.a ------------------")
    budget1 = compute_budget(100, [[100, 0, 0], [0, 0, 100]])
    print(f"The budget is: {budget1}\n")
    budget2 = compute_budget(30, [[0, 0, 6, 0, 0, 6, 6, 6, 6],
                                  [0, 6, 0, 6, 6, 6, 6, 0, 0], [6, 0, 0, 6, 6, 0, 0, 6, 6]])
    print(f"The budget is: {budget2}\n")

    print("# ------------------ Tests 5.b ------------------")
    ks = [[1, 2, 7], [1, 3, 6], [1, 4, 5], [0, 2, 8], [1, 0, 9], [10, 0, 0]]
    for triple in ks:
        k1, k2, k3 = triple[0], triple[1], triple[2]
        test_list = []
        test_list.extend([[30, 0, 0]]*k1)
        test_list.extend([[0, 30, 0]]*k2)
        test_list.extend([[0, 0, 30]]*k3)
        print(f"The budget is: {compute_budget(30, test_list)},\
        \nFair for groups of sizes {[k1, k2, k3]}? {Fair_to_groups(30, test_list)}\n")
