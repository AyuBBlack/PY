def minimal(lis):
    min_numb = lis[0]
    for el in lis:
        if el < min_numb:
            min_numb = el
    return min_numb


nums = [2, 5, 6, 5, 2, 7]
min_nums = minimal(nums)
nums_2 = [1.2, 5.5, 6, 43]
min_nums_2 = minimal(nums_2)


if min_nums < min_nums_2:
    print(min_nums)
else:
    print(min_nums_2)
