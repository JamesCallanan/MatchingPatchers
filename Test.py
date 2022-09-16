import numpy
#Need to enforce following check
#patch_members = even(patch_members)
patch_members = ['A','B', 'C', 'D', 'E', 'F','G','H']
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
    print(f'Product of odd numbers between 1 and {len(patch_members)} = {numpy.prod(odd_numbers)}')

print(all_pairwise_combinations)
print('Expected length = ', expected_number_of_solutions(patch_members))
print(len(all_pairwise_combinations))

