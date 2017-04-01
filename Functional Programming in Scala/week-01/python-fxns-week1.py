#Pascal's triangle

#Not doing as a list of lists.
'''
For reference:

Row 0        1
Row 1       1 1
Row 2      1 2 1
Row 3     1 3 3 1
Row 4    1 4 6 4 1
'''

def pascal(c, r):
    #c is the column, r is the Row
    if (c>r):
        print "Error"
        print (c,r)
    elif (r == 0) | (c == r) | (c == 0):
        print "1"
        print (c,r,1)
        return 1
    else:
        '''#if r is 2, then we know there are three numbers (cols 0 through 2)
        #we know the middle numbers are the sum of the two above...
        #we also know that if we are given c = r, that is 1. And c = 0 is 1, always.

        We want to work recursively from the r and c we know to get the middle numbers

        If r is two, then
        '''

        figure = pascal(c,r-1)+pascal(c-1, r-1)
        #print "Number is %f" % figure
        print (c,r,figure)
        return figure

'''Exercise 2: Parentheses balancing '''

#def balance(chars: List[Char]): Boolean

def balance(chars):
    if len(list(chars))== 0:
        print ("Empty")
    elif list(chars)[0] == ")":
        print "Unbalanced"
        #if ( is the last parenthesis, we know it is unbalanced.
        # if ) is last parenthesis, don't know unless n-1 ( for n ).
        '''How to do recursively?
        recursively, we get the head of the list, and the rest.
        We compare the head to the rest.
        We say "hooray", because programming is fun, when we get a '(' and a ')'.
        And if we get to end of list (where no more of the tail) and we have any parenthesis left,
        then it is unbalanced.
        '''
    elif list(chars):
        head = list(chars)[0]
        tail = list(chars)[1:-1]





#Testing from EdX course
def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

x = [0,1,2,3]

len(get_all_subsets(x))

4**2
10**2
len([1,2,3,4,5,6,7,8,9,10])
len(get_all_subsets([1,2,3,4,5,6,7,8,9,10,100]))

2**10
2**11



# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

y = powerSet([0,1,2,3,4])
y.__next__()

y.next()
