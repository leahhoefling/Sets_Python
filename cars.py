# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom = {"CRV", "Element", "Prius", "HRV"}

# Print the length of your set.
# print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("HRV")

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Insight", "Rover"})
# print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.remove("Rover")
# print(showroom)


# Acquiring more cars

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set()
junkyard = {"Insight", "Yukon", "Oldsmobile", "CRV"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
junkyard_cars_in_showroom = showroom.intersection(junkyard)
print(junkyard_cars_in_showroom)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
union_showroom = showroom.union(junkyard)
print(union_showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you don't want in your showroom.
union_showroom.discard("Oldsmobile")
union_showroom.discard("Insight")

print(union_showroom)
