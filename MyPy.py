def minimal(lis):
    min_numb = lis[0]
    for el in lis:
        if el < min_numb:
            min_numb = el
    print(min_numb)


nums = [2, 5, 6, 5, 2, 2, 1, 1]
minimal(nums)
