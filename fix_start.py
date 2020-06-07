str = input()
result = str[0] + str[1:].replace(str[0], '*')
print(result)
