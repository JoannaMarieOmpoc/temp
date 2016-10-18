integerList = list()
mandnList = list()

def zeroCheck(x, y, z):
    if x==0 or y==0 or z==0:
        return True
    else:
        return False

def ordered3(x, y, z):
    if x < y < z:
        return True
    else:
        return False

def modCount(first, second):
    if second <= first :
        n = first
        m = second
    else:
        n = second
        m = first

    return n/m


while True:
    integer = raw_input("Enter three integers: ")
    if integer == 'end':
        break
    content = int(integer)
    integerList.append(content)

print "\n", "zeroCheck: ", zeroCheck(*integerList)
print "ordered3: ", ordered3(*integerList)

print("\n")
while True:
    mandn= raw_input("Enter two positive integers: ")
    if mandn == 'end':
        break
    posintegers = int(mandn)
    mandnList.append(posintegers)

print "\n","modCount: ",modCount(*mandnList)

