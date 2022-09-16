import numpy as np
# patch_members = ['111','112', '121', '211', '212', '311','314','322']

def get_closeness_metric(personA, personB):
    if personA[0] == personB[0]: # part of the same cohort
        if personA[1] == personB[1]: #on the same team
            if personA[2] == personB[2]: #same person
                return 100
            else:
                return 0.9  
        else:
            return 0.3
    else: #diff cohort, diff team
        return 0

def calculate_closeness_matrix(patch_members):
    patch_member_closeness_matrix = dict((patch_member, dict((patch_member,0) for patch_member in patch_members)) for patch_member in patch_members)
    np.zeros((len(patch_members),len(patch_members)-1))
    for patch_member_row in patch_members:
        for patch_member_col in patch_members:
            patch_member_closeness_matrix[patch_member_row][patch_member_col] = get_closeness_metric(patch_member_row, patch_member_col)
    return patch_member_closeness_matrix
