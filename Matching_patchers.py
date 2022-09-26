#To Build
# patchers = ['Tom', 'Darren', 'Will', 'Alice']
# #patchers = ['Tom', 'Darren', 'Diane', 'Will', 'Alice']
# #remove duplicates
# #check for actual patchers?

# #dumb patch pairing algorithm
# even_patchers = patchers[::2] #Patchers at indexes 0,2,4,6,...
# odd_patchers = patchers[1::2] #Patchers at indexes 1,3,5,7,...

# groupings = [[i, list(tup)] for i, tup in enumerate(zip(even_patchers, odd_patchers))]

# #If odd number of patchers registered - we need a group of 3
# if len(even_patchers) > len(odd_patchers): 
# 	# don't want to add them to any group - group where they haven't met people
#     groupings[-1][-1].append(even_patchers[-1])

# return dict(groupings)
# # sample output format ...
# # {0: ['Tom', 'Darren'], 1: ['Will', 'Alice']}
# # {0: ['Tom', 'Darren'], 1: ['Diane', 'Will', 'Alice']}

# # Test what the combinations are like

import numpy
one_to_twenty = list(range(1,20))
odd_numbers = one_to_twenty[::2]
print(f'Odd numbers between one and 20 = {odd_numbers}')
print(f'Product of odd numbers between one and 20 = {numpy.prod(odd_numbers)}')

# # result if 20 people - 654_729_075 pairwise matchings
# # result if 30 people - 6_190_283_353_629_375 pairwise matchings

print(max(a))
# this took 10 seconds ...
# import time
# start_time = time.time()
# for i in range(353_629_375):
#     a = 1 + 1

# print('Time taken = ', time.time() - start_time)