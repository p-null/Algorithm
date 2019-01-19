import numpy as np

#solution 2: dynamic programming

def longest_common_sub(str_1, str_2):
    len_1 = len(str_1)
    len_2 = len(str_2)
    lengths = np.zeros((len_1,len_2), dtype=int)
    max_len = 0
    i_max = j_max = 0
    substring = ''
    for i in range(0,len_1):
        for j in range(0,len_2):
            if str_1[i] == str_2[j]:
                if i == 0 or j == 0:
                    lengths[i,j] = 1
                    max_len = 1    
                else:
                    lengths[i,j] = 1 + lengths[i-1,j-1]
                    if max_len < lengths[i,j]:
                        max_len = lengths[i,j]
                        i_max = i
                        j_max = j
    if(max_len > 0):      
        for i in range(1,max_len + 1):
            substring = substring + str_1[i_max - max_len + i]

    return max_len, substring
str_1 = input('input first string:\n')
str_2 = input('input second string:\n')
max_len, substring = longest_common_sub(str_1, str_2)
print('The longest common substring is\n{0} \nwith length of\n{1}'.format(substring, max_len))
