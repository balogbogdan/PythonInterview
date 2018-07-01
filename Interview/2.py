def multipliers():
    return [lambda x: i * x for i in range(3)]


print ([m(2)for m in multipliers()])