import numpy as np
from closeness_matrix import calculate_closeness_matrix 
import time 

start_time = time.time()
#Need to enforce following check
#patch_members = even(patch_members)
patch_members = ['111','112', '121', '211', '212', '311','314','322']
patch_members = ['121', '211', '212', '231', '232', '244', '311','314','322', '411', '431', '432'] # 12
patch_members = ['111','112', '114','122', '121', '211', '212', '231', '232', '244', '311','314','322', '411'] # 14
patch_members = ['111','112', '114','122', '121', '211', '212', '231', '232', '244', '311','314','322', '411', '431', '432'] # 16
patch_members = ['111','112', '114','122', '121', '211', '212', '231', '232', '244', '311','314','322', '411', '413', '414', '431', '432'] # 18

# first number indicates cohort #, second indicates team #, third indicates identifier on team
all_pairwise_combinations = []
cur_pairwise_combination = [None]*(int(len(patch_members)/2))
i = -1

def get_pairs(patch_members, all_pairwise_combinations, cur_pairwise_combination):
    global i
    i += 1
    if len(patch_members) == 2:
        cur_pairwise_combination[i] = (patch_members[0],patch_members[1])
        pair = cur_pairwise_combination.copy()
        all_pairwise_combinations.append(pair)
        i = -1
        return

    for letter in patch_members[1:]:
        cur_pairwise_combination[i] = (patch_members[0], letter)
        #Might be a more efficient way than using .remove()
        remaining_patch_members = patch_members[1:]
        remaining_patch_members.remove(letter)
        get_pairs(remaining_patch_members, all_pairwise_combinations, cur_pairwise_combination)

get_pairs(patch_members, all_pairwise_combinations, cur_pairwise_combination)

def expected_number_of_solutions(patch_members):
    number_of_members = list(range(1,len(patch_members)))
    odd_numbers = number_of_members[::2]
    print(f'Product of odd numbers between 1 and {len(patch_members)} = {np.prod(odd_numbers)}')

# print(all_pairwise_combinations)
# print('Expected length = ', expected_number_of_solutions(patch_members))
# print(len(all_pairwise_combinations))
# print(calculate_closeness_matrix(patch_members))

closeness_matrix = calculate_closeness_matrix(patch_members)
max_closeness_score = 0
min_closeness_score = 10
for pair_combination in all_pairwise_combinations: #iterate over sample combinations to find optimal pairing combo
    closeness_sum = 0
    for pair in pair_combination:
        pair_distance = closeness_matrix[pair[0]][pair[1]]
        closeness_sum += pair_distance

    if closeness_sum > max_closeness_score:
        max_closeness_score = closeness_sum
        max_combo = pair_combination
    
    if closeness_sum < min_closeness_score:
        min_closeness_score = closeness_sum
        min_combo = pair_combination
    
print(f'Pairing with max closeness score = {max_combo} \n with a closeness score of ... {max_closeness_score}')
print(f'Pairing with min closeness score = {min_combo} \n with a closeness score of ... {min_closeness_score}')

print(f'Time taken to pair {len(patch_members)} people was {time.time() - start_time} s')
