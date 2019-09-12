from p2_1 import get_protein_info
import pprint
pp = pprint.PrettyPrinter(depth=6)

protein_count = dict()
protein_count = get_protein_info()

max_count = -1
for protein_info in protein_count[1:]:
    if (len(protein_info[1]) > max_count):
        max_count = len(protein_info[1])
        max_protein = protein_info

# pp.pprint(protein_count)
for protein_info in protein_count:
    for index in range(len(protein_info)):
        if index%2==0:
            print("Organism Name: {}".format(protein_info[index]))
        else:
            print("Count: {}".format(len(protein_info[index])))
