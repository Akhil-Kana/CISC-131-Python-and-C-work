"""
CISC 131 Problem 3 - Akhil Kanayinkal (kana9520) and Amelia Berry (berr8662)
"""

def molecularWeight(weight_dict, weight_lst):
    """
    This function returns the molecular weight of a molecule
    """
    weight = 0.0
    for i in weight_lst:
        for j in weight_dict:
            if i == j:
                weight += weight_dict[j]
    return weight

water_weight = molecularWeight({"H": 1.008, "O": 15.999}, ["H", "H", "O"])
print(water_weight)
