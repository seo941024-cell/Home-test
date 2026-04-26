'''def solution(num_list):
    odd = ""
    even = ""
    for i in num_list :
        if i % 2 == 0 :
            even += str(i)
        else :
            odd += str(i)

    answer = int(odd) + int(even)
    return answer'''

def solution(num_list):
    answer = 0

    sum_result = sum(num_list)
    mul_result = 1

    for i in num_list :
        mul_result *= i

    if mul_result > sum_result ** 2 :
        answer = 0

    else :
        answer = 1
    return answer