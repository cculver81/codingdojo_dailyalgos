# Given: 'racecar' and 12344321

def isPalindrome(test_pal):
    if type(test_pal) != int and type(test_pal) != str:         # could also add array/list data type support
        print('Invalid data type for test_pal argument')
    elif type(test_pal) is int:
        test_pal = str(test_pal)
        for i in range(0,(len(test_pal)//2), 1):
            if test_pal[i] != test_pal[len(test_pal)-1-i]:
                print(f'{test_pal} is not a palindrome.')
                return False
    else:
        for i in range(0,(len(test_pal)//2), 1):
            if test_pal[i] != test_pal[len(test_pal)-1-i]:
                print(f'{test_pal} is not a palindrome.')
                return False
    print(f'{test_pal} is a palindrome.')
    return True

isPalindrome('racecar')
isPalindrome(12344321)
isPalindrome(1234547321)

