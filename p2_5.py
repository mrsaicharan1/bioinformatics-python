from p2_1 import get_protein_info
protein_count = dict()
proteins_info = get_protein_info()

def get_protein_count_info():
    for proteins in proteins_info.values():
        for protein in proteins:
            if protein not in protein_count.keys():
                protein_count[protein] = 0 
            protein_count[protein] = protein_count[protein] + 1
    return protein_count

min_count = 100000
protein_count = get_protein_count_info()
for protein, count in protein_count.items():
    if count < min_count:
        min_count = count
        min_protein = protein
    
print(min_count, min_protein)
print(protein_count)


