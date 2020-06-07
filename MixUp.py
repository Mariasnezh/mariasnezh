str1 = input()
str2 = input()
str_result = str1.replace(str1[0:2], str2[0:2]) + ' ' + str2.replace(str2[0:2], str1[0:2])
print(str_result)
