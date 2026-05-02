mon = {101, 102, 103, 104}
tue = {103, 104, 105, 106}

both = mon & tue
print(both)

only_mon = mon - tue
print(only_mon)

at_least_one = mon | tue
print(at_least_one)

exactly_one = mon ^ tue
print(exactly_one)

print("Set is suitable because it avoids duplicates, allows fast membership checks, and supports efficient union/intersection/difference operations.")
