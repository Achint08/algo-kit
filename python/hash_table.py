# Can be implemented using set() or dict() depending on the use-case
# If you want to store metadata, use dict()
# else, use set()

# Hash table as a dict,
hash_table = {}

m = int(input())
for _ in range(m):
    key, val = [int(i) for i in input().split(' ')]
    # Single value, but chances of updation
    # hash_table[key] = val

    # Just like adjacency list
    hash_table[key] = hash_table.get(key, []) + [val]


# To remove element
hash_table.pop(1)

print(hash_table)

# Hash table as a set
hash_set = set()
for _ in range(m):
    key = int(input())
    # Keys only get added once
    hash_set.add(key)

hash_set.remove(1)

print(hash_set)
