# Check if the input string is a palindrome or not
# madam, malayalam, dad, mom, 11011

# input

s = input("Enter a string: ")

# process

if(s == s[::-1]):
    print(s, ' is a palindrome')
else:
    print(s, ' is not a palindrome')
    
