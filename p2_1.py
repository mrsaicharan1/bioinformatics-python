import pprint
pp = pprint.PrettyPrinter(indent=4)
def all_proteins():
    with open('input.txt','r') as p:
        lines=p.readlines()
        return lines

lines = all_proteins()
protein_info = dict()
def get_protein_info():
    for line in lines:
        if line.startswith('AC'):
            proteins = line.split("   ")[1].rstrip().split(';')[:-1]
        if line.startswith('OS'):
            organ = line.split("   ")[1].rstrip()[:-1]
            protein_info[organ] = proteins
    return protein_info


