from p2_1 import get_protein_info
import pprint
import itertools
pp = pprint.PrettyPrinter(depth=6)
list_all_proteins = set()
protein_info = get_protein_info()
final_proteins = []
# pp.pprint(protein_info.values())

pairwise_present = 1

proteins = protein_info.values()
for protein_list in proteins:
    for protein in protein_list:
        list_all_proteins.add(protein)
print(list_all_proteins)
pairwise_proteins = list(itertools.permutations(list_all_proteins, 2))
for pairs in pairwise_proteins:
    for protein_list in protein_info.values():
        if not ((pairs[0] in protein_list and pairs[1] in protein_list) or\
               (pairs[0] not in protein_list and pairs[1] not in protein_list)):
            pairwise_present = 0
    if pairwise_present == 1:
        final_proteins.append(pairs)

print(final_proteins)
        
