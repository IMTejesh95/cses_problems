dna_string = input()
n = len(dna_string)
longest_rep = 1
reps = []
for i, dnachar in enumerate(dna_string):
    try:
        if i > 0 and dnachar != dna_string[i-1]:
            longest_rep = 1
        if i < n-1 and dnachar == dna_string[i+1]:
            longest_rep += 1
        reps.append(longest_rep)
    except Exception as e:
        print(e)

# CTCAGGGTCCG
print(max(reps))



