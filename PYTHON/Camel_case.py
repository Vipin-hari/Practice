def Camelcase(str):
    words = str.split()
    cc = ' '.join(word.capitalize() for word in words)
    return cc
a = input("Enter the string")
print(Camelcase(a))