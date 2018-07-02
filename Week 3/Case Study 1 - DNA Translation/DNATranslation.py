from DNAToAminoAcidTable import dna_to_amino_acid_table

DNA_FILE_NAME = "DNASequence.txt"
PROTEIN_SEQUENCE_FILE_NAME = "ProteinSequence.txt"

def readFile(file_name: str) -> str:
    """
    Opens the file that contains the DNA sequence of characters and returns
    the retrieved string.
    """
    with open(file_name, 'r') as dna_file:
        dna = dna_file.read().replace('\n', '').replace('\r', '')
    return dna

def translateDNAToAminoAcids(dna_string: str) -> str:
    """
    Translate a given sequence of DNA characters into a sequence of amino acids.
    Input is a sequence called the dna_string. Nucleotides are translated in triplets
    using a dictionary.
    """
    amino_acids = ""
    if len(dna_string) % 3 == 0:
        for i in range(0, len(dna_string), 3):
            codon = dna_string[i:i+3]
            amino_acids += dna_to_amino_acid_table[codon]
    return amino_acids

dna_data = readFile(DNA_FILE_NAME)
amino_acids_data = translateDNAToAminoAcids(dna_data[20:938])[:-1]
real_protein_data = readFile(PROTEIN_SEQUENCE_FILE_NAME)

print("DNA_data: " + dna_data)
print("amino_acids_data: " + amino_acids_data)
print("real_protein_data: " + real_protein_data)
print("Both the DNA conversion and protein sequences are the same: " + str(real_protein_data == amino_acids_data))
