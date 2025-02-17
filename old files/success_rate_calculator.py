import itertools 

skill_level = 4
strength_tn = 14

enemy_parries = [-1, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4]
feat_results = range(1, 13)
success_results = range(1, 7)
all_results = []
rates_per_parry = []
all_success_rates = []
successes = 0

# generating all possible outcomes
for feat_result in feat_results:
    for item in itertools.product(success_results, repeat=skill_level):
        all_results.append(sum(item) + feat_result)

# calculating success rates
for parry in set(enemy_parries):
    for result in all_results:
        if result >= strength_tn + parry:
            successes += 1
    success_rate = round(successes/len(all_results)*100)
    print(f"parry: {parry} \t success rate: {success_rate}%")
    successes = 0

# calculate overall score
for parry in enemy_parries:
    for result in all_results:
        if result >= strength_tn + parry:
            successes += 1
    success_rate = (successes/len(all_results)*100)
    all_success_rates.append(success_rate)
    successes = 0

total = 0
for rate in all_success_rates:
    total += rate
total /= len(all_success_rates)

print(f"average success rate: {round(total)}%")