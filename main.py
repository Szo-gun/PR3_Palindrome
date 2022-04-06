def testowanie(tested):
    reversed = tested[::-1]
    if tested == reversed:
        palindrome = 1
    else:
        palindrome = 0
    print(bool(palindrome))

testowanie("kajak")