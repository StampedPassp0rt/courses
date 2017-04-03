cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/float(cars_driven)

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print ("There will be %i empty cars today." % cars_not_driven)
print ("We can transport %i people today." % carpool_capacity)
print ("We have %i passengers to carpool today." % passengers)
print ("We need to put about %.2f passengers in each car today." % average_passengers_per_car)
