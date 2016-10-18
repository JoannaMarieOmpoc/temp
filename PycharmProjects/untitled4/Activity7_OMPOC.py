capitalize = list()

def capitalize_nested(capitalize):
    final = []
    for j in capitalize:
        final.append(j.upper())
    return final

while True:
    entry = raw_input("Enter words: ")
    if entry == 'end':
        break
    content = str(entry)
    capitalize.append(content)

print "\nCapitalized inputs: ", capitalize_nested(capitalize)