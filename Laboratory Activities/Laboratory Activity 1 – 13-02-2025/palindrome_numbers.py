num = input ("Enter a number: ")

reverse = ""
for digit in num:
    reverse = digit + reverse

if num == reverse:
    print ("Palindrome")
else:
    print ("Not a palindrome")
