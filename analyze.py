import numpy as np

def sumAlphabet(ls):
    sm = [0] * 26
    for i in range(0,26):
        for j in range(0,len(ls)):
            sm[i] = sm[i] + ls[j][i]
    return sm

def convertToStr(hsh):
    seqArrLetter = np.argsort(hsh)
    seqLetter = ""
    for i in range(0, 26):
        seqLetter = chr(seqArrLetter[i] + ord('A')) + seqLetter
    return seqLetter

'''
LCS (Longest Common Subsequence)
'''

def lcs(sqLetter,type):
    strTemp = "ETAOINSHRDLUCMFWYPVBGKJQXZ" if type == 0 else "ETOINASHRLUYDMWGCBFKPVJXZQ"
    arr = [[0] * 27 for i in range(0,27)]
    for i in range(1,27):
        for j in range(1,27):
            if strTemp[i-1] == sqLetter[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j],arr[i][j-1])
    lcsString = ""
    idxRow = idxCol = 26
    while arr[idxRow][idxCol] != 0:
        if arr[idxRow][idxCol-1] == arr[idxRow][idxCol]:
            idxCol = idxCol - 1
        elif arr[idxRow-1][idxCol] == arr[idxRow][idxCol]:
            idxRow = idxRow - 1
        else:
            lcsString = strTemp[idxRow-1] + lcsString
            idxCol = idxCol - 1
            idxRow = idxRow - 1
    return lcsString
