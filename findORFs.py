###Function for finding open reading frames###

table = "11" #change this number for your relevant NCBI table - 11 is for bacterial DNA
min_pro_len = 100 #set minimum ORF length to 100 amino acids - can change if desired

def find_ORFs(sequence): #defining the function with one argument (the sequence)
    for strand, nuc in [(+1, sequence.seq), (-1, sequence.seq.reverse_complement())]: #creating three reading frames in each direction
        #+1 = forward direction; -1 = reverse direction
        for frame in range(3): #there are three frames for each direction
            length = 3 * ((len(sequence)-frame) // 3) #Defining the length of the open reading frame (3 nucleotides --> 1 amino acid)
            # // 3 means result is rounded to nearest whole number in case the sequence is not divisible by 3
            for protein in nuc[frame:frame+length].translate(table).split("*"): #translate open reading frames according to chosen table
                #splitting at each stop codon (defined as "*") and then looping over the sequence to find the next ORF
                if len(protein) >= min_pro_len: #print the results if the length of the protein is greater than 100 - I found I had to define a variable (min_pro_len) as ">= 100" did not work
                    print("%s...%s - length %i, strand %i, frame %i" \
                    % (protein[:30], protein[-3:], len(protein), strand, frame)) #printing results