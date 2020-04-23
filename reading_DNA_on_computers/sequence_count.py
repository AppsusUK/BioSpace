from collections import Counter



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

def count_bases():
  FASTA = open_and_parse_fasta("./GCF_000010365.1_ASM1036v1_genomic.fna")
  carsonella_ruddi = FASTA.get('NC_008512.1 Candidatus Carsonella ruddii PV DNA, complete genome')
  print(Counter(carsonella_ruddi))


if __name__ == "__main__":
    count_bases()