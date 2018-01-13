"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Rosalind Bioinformatics:
    Transcribing DNA into RNA
    http://rosalind.info/problems/rna/

This should be relatively easy with Python.
"""
def countDNA(dnaString):
    '''
    Return RNA code with the DNA T swapped with U.
    '''
    return dnaString.replace('T','U')

if __name__ == "__main__":
    # Start the program with the DNA string to swap to an RNA string.
    print(countDNA('TATCACTATTTCGACAGCTTACTCTATTGCCCGTCAATGCGAAAGTTTTGAAAGAGGATCTTACTGTCATATCGCTACCAACTTCCGCAATTACCAGCGGAAGCAGGGTATTAGTCGAATCACTGTACATCCACGCCTCAATCATTGTTTCTGAAGGGGCCGACCTGTATCTTACGTGAGAGCAGCTTGTTGTCAACGAGATTACGTTCGGTAGACTCCGGTAGTAAGATCCGCTACTGGCATCGCGTGCGCGAACGCAATCTCTCGCGTTCTTAAATTAACTTGTATGACTCATCTCATGTGGCCATCCCCCAACAAGGAACATCATTTGGACTCGCCAAGTATACCATTAAATGACTCCCACCTTGCGGACTGCGAGCCTTTTCCGTAGCTCAGATGCGTATGTAAGGACCAGGTAATCATGCGATCTCATGATCGTTACCTAGACATAGATCAATTACCATTAACCAGTCACAATTTACTTTTCGCCTCTGTTCGCGCCACGTTTGTTCAGAAATCCTCCGCTCAAACGTTTGCCGAATGACGGCTGCGATTTGCAGCCAAGAACTGAAGGTGAGGGCCATGGGTAAGCTCGATTAAGTATACAAAGGAAGCAATTCTAGGTTCTTTACAGTCAGGCTGTGACAACGATCGAAATCATGAATCCACACCGATGGGATAGGTACATAGGACCCAGTGGTAGCTCAGGGCCGGCTCCCACTAAGCGCCGATAGTACCTATTAATGTAGTATAATGAGGAAACACTGCAGTCCACATCGAGAGTCATTGAATTTGCTAGCTACCACGTACAATATCAACAAAACTGCATAATATACTCCGACAGACACGACATGATCCATCGATACGTACAATATTAGTCGGGATCACTTTAAAAGAAGTTAAATTCTTGATGGACGGACCATTAA'))