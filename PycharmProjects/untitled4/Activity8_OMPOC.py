integerList = list()

def cumulative_sum(integerList):
    cmltvsum = []
    sum = 0
    for i in integerList:
        sum = sum + i
        summ = float(sum)
        cmltvsum.append(summ)
    return cmltvsum

while True:
    entry = raw_input("Enter integers: ")
    if entry == 'end':
        break
    content = float(entry)
    integerList.append(content)

print "\nThe cumulative sum is: ", cumulative_sum(integerList)