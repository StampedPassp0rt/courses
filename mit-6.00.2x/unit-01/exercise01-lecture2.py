Good # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.

      For each item, decide whether it goes into bag 1, bag 2, or none.
    """
    #Need to know the # of items
    N = len(items)
    bag1 = True
    #for two bags, 3**N combinations
    for i in range(3**N):
        combo_1 = []
        combo_2 = []
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                combo_1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                combo_2.append(items[j])

        yield (combo_1, combo_2)



'''Testing code from Problem Set 1'''

def greedy_recursion(i, sorted_cows_list, weight_limit, temp_list):
    #stop if already gone through list
    total_weight = 0
    if [temp_list] != [[]]:
        cow_list = [temp_list]
    else:
        cow_list = []

    N = len(sorted_cows_list)
    #start by going from biggest cow
    if i == N:
        return cow_list
    for cow in range(i, N):
        if (total_weight + sorted_cows_list[i][1]) <= weight_limit:
            cow_list.append(sorted_cows_list[i][0])
            total_weight = total_weight + sorted_cows_list[i][1]
        else:
            cow_list = greedy_recursion(i+1, sorted_cows_list, weight_limit, cow_list)

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    I.e. [[Maggie, Herman, Betsy], [Oreo, Moo Moo, Milkshake],...]

    """
    #Casting dictionary into list of tuples.
    list_cows= []
    for key in cows:
        list_cows.append([key, cow[key]])

    #Sorting the list
    sorted_cows = sorted(list_tuples, key = lambda x: x[1], reverse = True)

    #trip result list
    trip_result = []
    total_trip_weight = 0

    trip_result = greedy_recursion(0, sorted_cows, limit, trip_result)
    return trip_result

cow_dict = {}
f = open("pset1/ps1_cow_data.txt", 'r')
for line in f:
    line_data = line.split(',')
    cow_dict[line_data[0]] = int(line_data[1])
return cow_dict

cow_dict

list_cows = []
list_cows = sorted(([w, n] for n, w in cow_dict.items() if w <= 10), reverse = True)

['Herman']+['Henrietta']
N = len(list_cows)
trips = []
total_weight = 0

current = []
for cow in list_cows:
    print cow
    if (total_weight + cow[0]) <= 10:
        print cow
        current.append(cow[1])
        total_weight = cow[0]+total_weight
        print "New Total Weight after adding %s is %i" % (cow[1], total_weight)
    elif (total_weight + cow[0]) > 10:
        trips.append(current)
        length_current = len(current)
        print "Length current:", length_current
        list_cows = list_cows[length_current:]
        print list_cows
        current = []
        total_weight = 0
        print "Total Weight Reset to ", total_weight
        print ""
        print ""
        break


def greedy_helper(sorted_cows, weight_limit, total_weight, trips):
    #stop if already gone through list
    current_trip = []
    if len(sorted_cows) == 0:
        return trips
    for cow in sorted_cows:
        if (total_weight + cow[0]) < 10:
            #Append the cow to the current trip
            current_trip.append(cow[1])
            #Adjust weight
            total_weight = cow[0]+total_weight
        elif (total_weight+ cow[0]) == 10:
            current_trip.append(cow[1])
            trips.append(current_trip)
            total_weight = 0
            length_current = len(current_trip)
            greedy_helper(sorted_cows[length_current:], 10, 0, trips)
            break
        elif (total_weight + cow[0]) > 10:
            trips.append(current_trip)

            length_current = len(current_trip)
            current_trip = []
            total_weight = 0
            greedy_helper(sorted_cows[length_current:], 10, 0, trips)
            break
    if len(current_trip) != 0:
        trips.append(current_trip)
    return trips
            #list_cows = list_cows[length_current:]

            #current = []
            #total_weight = 0



trips = greedy_helper(list_cows, 10, 0, [])
trips
while len(list_cows)>0:
    x, trips = greedy_helper(list_cows, 10, 0, [])
    greedy_helper(list_cows[x:], 10, 0, trips)

'''


        if (total_weight + sorted_cows_list[i][1]) <= weight_limit:
            cow_list.append(sorted_cows_list[i][0])
            total_weight = total_weight + sorted_cows_list[i][1]
        else:
            '''
