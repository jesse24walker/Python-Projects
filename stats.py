def mean(numbers):
    # check if numbers is empty
    if numbers == []:
        return 0
    # find sum
    s = sum(numbers)
    # find the count of numbers
    c = len(numbers)

    # mean = sum/count
    mean_res = s / c
    return mean_res


def median(numbers):
    # check if numbers is empty
    if numbers == []:
        return 0
    # sort the array
    numbers.sort()
    # find the count of numbers
    c = len(numbers)

    # check even or odd
    if c % 2 == 0:
        med = numbers[c // 2]
    else:
        med = numbers[c // 2] + numbers[c // 2 + 1] / 2
    return med


def mode(numbers):
    # check if numbers is empty
    if numbers == []:
        return 0

    # find the maximum count
    max_count = 0
    max_num = numbers[0]
    for num in numbers:
        # check if the num has more repetitions
        if numbers.count(num) > max_count:
            # update the max number and count
            max_count = numbers.count(num)
            max_num = num
    return max_num


# test
def main():
    numbers = [1, 5, 2, 8, 0, 1, 6, 9, 3, 7, 1, 5, 0, 5, 2, 5, 5, 5]
    print('Numbers: ', numbers)
    print('Mean : ', mean(numbers))
    print('Median : ', median(numbers))
    print('Mode : ', mode(numbers))

    # test with empty list
    numbers=[]
    print('\nNumbers: ', numbers)
    print('Mean : ', mean(numbers))
    print('Median : ', median(numbers))
    print('Mode : ', mode(numbers))

# call the function
if __name__ == '__main__':
    main()
