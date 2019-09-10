from p2_1 import get_protein_info
def human_chimpanzee():
    proteins_list = get_protein_info()
    human_proteins = set()
    chimp_proteins = set()
    for key in proteins_list.keys():
        if key == 'Homo sapiens (Human)':
            for protein in proteins_list[key]:
                human_proteins.add(protein)
        elif key == 'Chimpanzee':
            for protein in proteins_list[key]:
                chimp_proteins.add(protein)
    return human_proteins.difference(chimp_proteins)


print(human_chimpanzee())
