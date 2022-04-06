def testowanie(tested):
    """
    Print True/False depending on whether the word is a palindrome or not.
    Arguments:
    Tested - string
    """
    reversed = tested[::-1]
    if tested == reversed:
        palindrome = 1
    else:
        palindrome = 0
    print(bool(palindrome))

testowanie("kajak")