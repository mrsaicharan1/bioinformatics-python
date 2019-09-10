from p2_1 import get_protein_info
protein_count = dict()
proteins_info = get_protein_info()

for proteins in proteins_info.values():
    for protein in proteins:
        if protein not in protein_count.keys():
            protein_count[protein] = 0 
        protein_count[protein] = protein_count[protein] + 1

max_count = -1
for protein, count in protein_count.items():
    if count > max_count:
        max_count = count
        max_protein = protein
    
print(max_count, max_protein)


