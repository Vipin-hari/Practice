def palindrome(str):
    lower_case=str.lower()
    print("Given string:",str)
    rev = lower_case[::-1]
    print(rev)
    if rev == lower_case:
        print("The string is Palindrome")
    else:
       print("The string is  not a palindrome")
a = input("Enter a string: ")
palindrome(a)