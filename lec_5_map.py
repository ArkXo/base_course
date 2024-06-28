def func(a):
    return (a%3 == 0)

nums = [21,21,32,34,56,87,98]

result = list(map(func, nums))

print(result)

def func_new(a, b):
    return a*b

nums1 = [2,6,8,2,1,2]
nums2 = [2,6,8,2,1,2]

nams_mul = list(map(func_new, nums1, nums2))

print(nams_mul)