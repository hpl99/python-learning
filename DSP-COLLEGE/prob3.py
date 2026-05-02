cricket_players = ["Alice", "Bob", "Charlie", "David"]
football_players = ["Charlie", "David", "Eve", "Frank"]

cricket_set = set(cricket_players)
football_set = set(football_players)

both = cricket_set.intersection(football_set)
print(f"Play both: {both}")
only_cricket = cricket_set.difference(football_set)
print(f"Only Cricket: {only_cricket}")