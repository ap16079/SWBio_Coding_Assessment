from Bio import SeqIO #importing relevant modules for code to function
from Bio.Seq import Seq
from findORFs import find_ORFs

BatE_pOPINE = SeqIO.read("BatE_insert.fna", "fasta") #using SeqIO module to read fasta file - can put your own fasta file in place of "BatE_insert.fna" and rename the variable

find_ORFs(BatE_pOPINE) #using find_ORFs function from findORFs.py to find ORFs as well as their frame and location - the first two lines of the output are a result of this function

###Translating frame 0 of BatE_pOPINE DNA sequence from the first methionine amino acid for comparison to the expected amino acid sequence###

BatE_seq = Seq("ATGAACAGATCTGACGTCGTTCAGTTTTCGGAAGTCGAGCCCGGCATCATTCAAATCACGATGCAGGATCGCGAGAACAAGAACACGTTTTCCAGAGAACTGGTCAAGGGGCTGATAAATGCCTTTCGTCATATCCGGGAGAGCGAACGATATCGGGTCGTTGTCTTGACAGGCTATGACACTTACTTTTGCTCCGGCGGTACAAAAGAGGGACTGCTGATGCTGCATGAAGGGCAGGGCAAGTTTACTGACATGAATATCTATAGTGTTCCGCTGGAGTGCGAAATCCCGGTGATTTCGGCGATGCAGGGTCATGGCATTGGCGGGGGATTTGTATTCGGTCTGTTTGCTGATTGTGTGGTGTTGAGTCGAGAGAGCGTTTACACGACCAATTTCATGAAGTACGGCTTTACACCCGGCATGGGGGCGACCTATGTACTACCCGAGAAGCTGGGACTTGGACTCGCTGAGGAAATGCTGCTGAGCGCACGCACTTATCGCGGAGCTGATCTTGAGAAACGCGGTGTCCCATTTCCGGTTCTGCCACGGGCAGAAGTACTGGAATATGCCCTGCAACTGGCACGTGATCTGGCCGAGAAACCACGTATTTCGCTGGTGACGCTCAAGAGCCATCTTGTTGCCGAAATGCGCGCCCGGTTACCGACTATCGTAGAGCAGGAAATCGCGATGCATGACAAGACATTCCATCAGCCTGAGGTAAAGGCGCGTATTGAAAATGTGTTCGGGTTTAAACATCACCATCACCATCACTAA") # this is the gene sequence within the vector from the start to stop codon

trans_BatE = BatE_seq.translate(table=11, to_stop=True,) #translating the BatE DNA sequence; to_stop means stop translating when the stop codon is reached (and do not include the corresponding amino acid). Again, the table number can be changed based on the NCBI table required for your work.

print(f"Your translated sequence is: {trans_BatE}") #printing the translated protein sequence - the second part of the output
            
###Comparing the translated gene to the expected amino acid sequence###

expected_BatE = Seq("MNRSDVVQFSEVEPGIIQITMQDRENKNTFSRELVKGLINAFRHIRESERYRVVVLTGYDTYFCSGGTKEGLLMLHEGQGKFTDMNIYSVPLECEIPVISAMQGHGIGGGFVFGLFADCVVLSRESVYTTNFMKYGFTPGMGATYVLPEKLGLGLAEEMLLSARTYRGADLEKRGVPFPVLPRAEVLEYALQLARDLAEKPRISLVTLKSHLVAEMRARLPTIVEQEIAMHDKTFHQPEVKARIENVFGFKHHHHHH") #reading in the BatE protein sequence that is required

print(f"Your expected sequence is: {expected_BatE}") #printing the expected protein sequence - the third part of the output

if expected_BatE == trans_BatE: # an if statement to see whether the two sequences are the same - the final part of the output
    print(f"The expected and translated sequences are the same")
else:
    print(f"The expected and translated sequences are not the same")