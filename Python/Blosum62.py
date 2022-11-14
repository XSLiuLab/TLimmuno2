import pandas as pd
import numpy as np

Blosum62_matrix = pd.read_csv(r"~/Data/MHCII/BLOSUM62.csv",comment="#")
Protein_alphabet = list("ARNDCQEGHILKMFPSTWYVX")
Blosum62_matrix = Blosum62_matrix[Protein_alphabet]
Blosum62_matrix = Blosum62_matrix.loc[Protein_alphabet]
Blosum62_matrix

def blosum62(peptide,maxlen):
    encoder = np.empty((maxlen,21))
    if len(peptide) <=maxlen:
        peptide = peptide + "X"*(maxlen-len(peptide))
    for i in range(len(peptide)):
        pep = list(peptide)[i]
        coder = Blosum62_matrix[pep]
        encoder[i] = coder
    return encoder.flatten()

if __name__ == "__main__":
    blosum62(peptide,maxlen)