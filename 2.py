def my_min(l):  # O(n)
    answer = l[0]
    for item in l:
        if answer > item:
            answer = item
    return answer
print(my_min([4,2,3]))

def my_min2(l):  # O(n^2)
    answer = l[0]
    i = 1
    while i < len(l) - 1:
        temp = [l[i], l[i - 1]]
        j = 0
        while j < len(temp):
            if temp[j] < answer:
                answer = temp[j]
            j += 1
        i += 1
    return answer

print(my_min2([4,2,3]))