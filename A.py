
def soluchan(number):
    digits = list(number) 
    len_digits = len(digits)
    if len_digits < 2 :
        return number
    n = 2
    while n!= len_digits:
        unused_digits = digits[:-n]
        last_n_digits = digits[-n:]
        
        if sorted(last_n_digits,reverse = True) == last_n_digits :
            n+=1
            continue
        else:
            zero_digit = last_n_digits[0]
            rest_of_digits = last_n_digits[1:]
            # swapping max of rest_of_digits with zero_digit and sortign res_of_digits in ascending
            max_rest_of_digits = min(list(filter(lambda x: x > zero_digit,rest_of_digits))) # find the next big int not the max 
            index_max_digit = rest_of_digits.index(max_rest_of_digits)
            rest_of_digits[index_max_digit] = zero_digit
            zero_digit = max_rest_of_digits
            # sort rest_of_digits and combine with unused_string
            next_number = unused_digits + [zero_digit] + sorted(rest_of_digits)
            next_number = "".join(next_number)
            return next_number
    if n == len_digits:
        next_number = [digits[n-1]]+["0"]+sorted(digits[:-1])
        next_number = "".join(next_number)
        return next_number
def print_answer(answer):
    for index,value in enumerate(answer,1):
        print("Case {0}: {1}".format(index,value))




testcases = int(input())
cases = []
for x in range(testcases):
    cases.append(str(input()))


results = []
for x in cases:
    results.append(soluchan(x))
print_answer(results)

