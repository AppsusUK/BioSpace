def open_and_parse_fasta(filepath):
    FASTA_file = open(f"{filepath}", "r")
    FASTA_dict = {} 
    FASTA_label = ""
    for line in FASTA_file: 
        line = line.rstrip()
        if line.startswith(">"): 
            FASTA_label = line[1:]
            FASTA_dict[FASTA_label] = "" 
        else: 
            FASTA_dict[FASTA_label] += line 
    return FASTA_dict


def reverse_complement_DNA():
    FASTA = open_and_parse_fasta("dna-replication-and-reverse-complements/GCF_000010365.1_ASM1036v1_genomic.fna")
    carsonella_ruddi = FASTA.get('NC_008512.1 Candidatus Carsonella ruddii PV DNA, complete genome')
    reverse_complement = carsonella_ruddi.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    print(reverse_complement)
    
    
if __name__ == "__main__":
    reverse_complement_DNA()