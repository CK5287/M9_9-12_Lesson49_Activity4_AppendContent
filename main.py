first_file = input("Enter the name of first file")
second_file = input("enter the name of second file")

f1 = open(first_file,'r')
f2 = open(second_file,'r')

print('content of first file before appending -\n', f1.read())
print('content of second file before appending -\n',f2.read())


f1.close()
f2.close()

f1 = open(first_file, 'a+')
f2 = open(second_file, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)


print('contemt of first file after appending - \n',f1.read())
print('content of second file after -\n',f2.read())

f1.close()
f2.close()