# prints every possible permutation of the integers in the list 'a' in lexicographical order, as described in Kenneth Rosen's Discrete Mathematics
# and its Applications, 7th edition, chapter 6
def permutate(a, f):
    n = len(a)-1
    p = 0
    if n == 0:
        p = 1
        print(a)
    if n == 1:
        p = 2
        print(a)
        print(f)
    else:
        print(a)
        swapstart = 0
        p = 1
        ps = [a, f]
        while a != f:
            for i in range(n):
                if a[i] < a[i+1]:
                    swapstart = i
            
            print(a)
            p += 1
    print(p, "permutation(s) found. ")
    main()

# requests input from user (integer between 1-9, inclusive), generates a list, and calls the permutate function passing in the
# list and the reverse of the list as its goal state
def main():
    a = []
    f = []
    while a == []:
        ninput = input("Please enter a number between 1-9 or enter quit to exit: ")
        if ninput == "quit":
            print("Goodbye. ")
            return
        elif ninput not in ["1","2","3","4","5","6","7","8","9"]:
            print("Input not recognized. ")
        else:
            n = int(ninput)
            for i in range(n):
                a.append(i+1)
            for i in range(n):
                f.append(i+1)
            f.reverse()
    permutate(a, f)