# display the number of objects in the list

color_list = ['Red', 'Green', 'White', 'Black']
print(len(color_list))

# this exercies was to compute the value of n+nn+nnn

n = int(input('value: '))
dbl_n = n * n
trp_n = n ** n

if n > 0:
    print(dbl_n + trp_n)

# Wrong Answer.

# Correction

a = int(input('value: '))
n1= int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1 + n2 + n3)



# exercies to write a name in reverse

Fs = input("First Name:\n ")
Ls = input("Last Name:\n ")
print(f" Hello {Ls} {Fs}")

# Correct



