mor = {1, 2, 3, 4, 5}
eve = {4, 5, 6, 7}
all_reg = {1, 2, 3, 4, 5, 6, 7, 8, 9}
both = mor & eve
print(both)
only_one = mor ^ eve
print(only_one)
missed = all_reg - (mor | eve)
print(missed)
print("Set is preferred because it removes duplicates, allows fast union/intersection/difference, and membership checking is faster.")
