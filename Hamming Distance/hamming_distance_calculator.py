def hamming_distance(s1, s2):
    count = 0
    
    if len(s1)==len(s2):

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count
    
    else:

        return "Error Note: Hamming Distance is only calculated between strings of equal length"

print(hamming_distance('github', 'rubhub'))