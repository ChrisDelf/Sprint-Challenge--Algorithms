'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word == 0:
        return 0

    # TBC
    count = 0
    # find() determines if string str occurs in another string.
    f_w = word.find('th')

    # if it does not find the string in the other string it returns a negative value.
    if f_w != -1:
        count += 1
        # since find() gives us the index in which we
        #found the word we want it to shift over 2 letters
        count += count_th(word[f_w + 2:])


    return count

print(count_th("thhtthhtthtthhtth"))
