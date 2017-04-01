###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time
import timeit

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1

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
    #Casting dictionary into list
    list_cows = sorted(([w, n] for n, w in cows.items() if w <= limit), reverse = True)


    #trip result list
    total_weight = 0
    trips = []
    trip_results = greedy_helper(list_cows, limit, total_weight, trips)
    return trip_results



# Problem 2


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips




    """

    names = list(cows.keys())
    weights = list(cows.values())
    for partition in get_partitions(cows):
        fits = True
        #Exhausts looking at the partition to see if it is feasible.
        for element in partition:
            total_weight = 0
            for cow in element:
                total_weight += weights[names.index(cow)]
            if total_weight > limit:
                fits = False
        #If partition is still feasible, it'll test as True and go through this.
        if fits == True:
            try:
                if len(partition) < len(minTrips):
                    minTrips = partition.copy()
            except:
        #The first copy that is True will become the minTrips through this.
                minTrips = partition.copy()
    return minTrips




# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows_test = load_cows("ps1_cow_data.txt")
    time0 = time.time()
    greedy = greedy_cow_transport(cows_test)
    time1 = time.time()
    brute = brute_force_cow_transport(cows_test)
    time2 = time.time()
    print ("# of Trips by Greedy Algorithm:", len(greedy))
    print ("# of Trips by Brute Force Algo:", len(brute))
    
    print ("Greedy Algo took time:", time1-time0)
    print ("Brute Force Algo took time:", time2-time1)
    pass


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
