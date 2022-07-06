'''
steps:
1. Take any three digit number. All the three digits must NOT be identical
2. Arrange the digits in ascending order
3. Arrange the digits in descending order
4. Subtract the smaller number from the bigger number
5. If the answer is 495, stop
   Else, repeat steps 2, 3 and 4 until the result is 495
   
The catch is, the result is always 495. This is called the Kaprekar constant after the mathematician who discovered this pattern.

- If the difference is a 2 digit number, pad a zero. For example, 110 - 011 = 99. The next step would be, 990 - 099...
'''


def get_no_in_ascending(num):
    l = list(str(num))
    l.sort()
    str_l = "".join(l)
    return(int(str_l))


def get_no_in_descending(num):
    ## zero padding
    if num < 100:
        l = list(str(num)) + ['0']
    else:
        l = list(str(num))
        
    l.sort(reverse=True)
    str_l = "".join(l)
    return(int(str_l))


no_of_iterations = []
for i in range(100,1000,1): ## range(start,stop,step) ... (start, stop]
    if i % 111 != 0: ## ensuring that the digits are not identical
        big_num = get_no_in_descending(i)
        small_num = get_no_in_ascending(i)
        
        diff = big_num - small_num
        count = 1
        while(diff != 495): ## while(condition == true), the loop is executed
            big_num = get_no_in_descending(diff)
            small_num = get_no_in_ascending(diff)
            
            diff = big_num - small_num
            
            count = count + 1
        print('number:', i, 'count:', count)
        no_of_iterations.append(count)
        

### Uncomment the following two lines if you are interested in finding out how many numbers took how many iterations.
# import numpy as np
# print(np.unique(no_of_iterations, return_counts=True))

### 246 numbers take 3 iterations and just 51 numbers take 6 iterations to reach 495
