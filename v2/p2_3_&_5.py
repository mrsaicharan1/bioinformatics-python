from p2_1 import get_protein_info
import pprint
pp = pprint.PrettyPrinter(depth=6)

protein_count = dict()
protein_count = get_protein_info()

max_count = -1
for protein_info in protein_count[1:]:
    if (len(protein_info[1]) > max_count):
        max_count = len(protein_info[1])
        max_protein = protein_info[0]

print(max_count, max_protein)



min_count = 100000
for protein_info in protein_count[1:]:
    if (len(protein_info[1]) < min_count):
        min_count = len(protein_info[1])
        min_protein = protein_info[0]

print(min_count, min_protein)