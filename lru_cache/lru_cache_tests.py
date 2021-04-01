from lru_cache import LRU_Cache

# Test Cases


def return_value_error_if_capacity_is_none():
    try:
        our_cache = LRU_Cache(None)
    except ValueError as err:
        print(err)


def return_value_error_if_capacity_is_zero():
    try:
        our_cache = LRU_Cache(0)
    except ValueError as err:
        print(err)


def return_value_error_if_capacity_is_not_integer():
    try:
        our_cache = LRU_Cache('a')
    except ValueError as err:
        print(err)


def remove_proper_value_from_cache():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)       # returns 1
    our_cache.get(2)       # returns 2
    # our_cache.set(3, 3)
    # our_cache.get(3)
    our_cache.get(9)      # returns -1 because 9 is not present in the cache
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    our_cache.get(3)


return_value_error_if_capacity_is_none()
return_value_error_if_capacity_is_zero()
return_value_error_if_capacity_is_not_integer()
remove_proper_value_from_cache()
