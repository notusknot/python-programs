def factorial(number):
    if number == 0:
        return 1
    return number*factorial(number-1)

def permutation(string, x=0):
    if len(string) == x:
        return None

    return string[x] + permutation(string[x+1:])

print(permutation('cat'))
