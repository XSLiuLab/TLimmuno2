import numpy as np

def NN_Data(data):
    peptide = np.empty((len(data),21,21))
    for i in range(len(data)):
        peptide[i] = data["pep_blosum"][i].reshape((21,21))
    #mhc 
    MHC = np.empty((len(data),34,21))
    for i in range(len(data)):
        MHC[i] = data["MHC_blosum"][i].reshape((34,21))
    #score
    labels = data["score"].values

    return peptide,MHC,labels
