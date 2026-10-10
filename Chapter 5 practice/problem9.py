s = {8, 7, 12, "Harry", [1,2]}

# No, you cannot change the values inside a list contained in a set in Python. In fact, you cannot even have a list as an element in a set because sets in Python require all their elements to be immutable and hashable. Lists are mutable and not hashable, so they cannot be added to a set.