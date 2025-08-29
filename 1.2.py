def solve():
    s = input("Enter a word: ").upper()
    word = {'L', 'U', 'M', 'O', 'S'}
    for letter in s:
        print(letter)
        if letter in word:
            word.discard(letter)
    
    
    
    if len(word) == 0:
        print("Hermoinee can go")
    else:
        print("Hermoinee can't go now")


solve()