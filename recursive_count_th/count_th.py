'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1:
        return 0
    else:
        is_th = 0
        if word[0:2] == 'th':
            is_th = 1
            
        return is_th + count_th(word[1:])
