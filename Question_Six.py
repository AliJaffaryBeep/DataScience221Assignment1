def distributionAnalysis(numbers):
    n = len(numbers)
    result = {}

    for i in sorted(set(numbers)):  # unique keys, sorted
        count = 0
        for j in numbers:
            if j <= i:
                count += 1
        result[i] = (count / n) * 100

    return result


numbers = [3,1,2,3,4,2]

print(distributionAnalysis(numbers))
