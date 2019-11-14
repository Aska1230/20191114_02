print('Hello world')

print('464'.isalpha())
print('sdff'.isalpha())
print('464'.isdigit())
print('sddsd'.isdigit())


def p(a):

        if a%2 == 0:
            print('Yes')
        else:
            print('No')
p(2)

(age, size) = "56,345".split(',')
print(age)
print(size)
(2, 4, 5)

print('ssss')

# 20181114

# some more options on files
import os

dir = 'h:\\'
files = os.listdir(dir)
print(files)


for f in files:
    if os.path.isdir(os.path.join(dir, f)):
        print(f)


os.path.