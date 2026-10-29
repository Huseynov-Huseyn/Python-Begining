import time
import tracemalloc


def find_element(iterable):
    """Find an element in range 0-4999 (included) in an iterable and pass."""
    for i in range(50000):
        if i in iterable:
            pass


def create_and_measure(factory):
    """Create a collection and return it with the RAM it uses (in MB)."""
    tracemalloc.start()
    collection = factory()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return collection, current / 1024 / 1024


def report(name, factory):
    """Create a collection, then print its RAM usage and search time together."""
    collection, ram = create_and_measure(factory)
    start_time = time.time()
    find_element(collection)
    elapsed = time.time() - start_time
    print(f"{name}: RAM = {ram:.2f} MB, time = {elapsed:.4f} seconds.")


report("List", lambda: list(range(10000000)))
report("Tuple", lambda: tuple(range(10000000)))
report("Set", lambda: set(range(10000000)))
