from p2_1_dict import get_protein_info
difference_list = []
def human_chimpanzee():
    proteins_list = get_protein_info()
    human_proteins = list()
    chimp_proteins = list()
    for key in proteins_list.keys():
        if key == 'Homo sapiens (Human)':
            for protein in proteins_list[key]:
                difference_list.append(protein)
        elif key == 'Chimpanzee':
            for protein in proteins_list[key]:
                if protein in difference_list:
                    difference_list.remove(protein)
                else:
                    difference_list.append(protein)
    return difference_list


print(human_chimpanzee())
