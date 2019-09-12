import pprint
pp = pprint.PrettyPrinter(depth=6)

def all_proteins():
    with open('input.txt','r') as p:
        lines=p.readlines()
        return lines

lines = all_proteins()
organisms = []
proteins_list = [[]]
protein_tuples = [[]]
def get_protein_info():
    for line in lines:
        if line.startswith('AC'):
            proteins = line.split("   ")[1].rstrip().split(';')[:-1]
            proteins_list.append(proteins)
        if line.startswith('OS'):
            organ = line.split("   ")[1].rstrip()[:-1]
            organisms.append(organ)
    for organ, protein in zip(organisms, proteins_list):
        protein_tuples.append([organ, protein])
    return protein_tuples

pp.pprint(get_protein_info())

