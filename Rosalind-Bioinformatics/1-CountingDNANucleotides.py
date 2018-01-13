"""
__author__ = "Patrick Doyle"
__license__ = "The Unlicense"
__email__ = "me@pcdoyle.com"

Rosalind Bioinformatics:
    Counting DNA Nucleotides
    http://rosalind.info/problems/dna/

This should be relatively easy with Python.
"""
# The filename with the DNA Strings
DNAFILE = '1-DNANucleotides.txt'

def countDNA():
    '''
    Function to count the DNA letters in a string.
    '''
    # Open the file and read the DNA strings into a list.
    dnaString = open(DNAFILE,'r').read().splitlines() # splitlines() removes the newline character from the file.

    # Loop through the list of strings and print the results to the console.
    for i in range(len(dnaString)):
        print(dnaString[i].count('A'),dnaString[i].count('C'),dnaString[i].count('G'),dnaString[i].count('T'))

if __name__ == "__main__":
    # Start the program.
    countDNA()