import random

class BinarySearchTestDataFactory:

    def __init__(self, random_seed=None):
        if random_seed:
            random.seed(random_seed)

    def generate_sorted_list(self, size, start=0, step=1):
        return list(range(start, start + size * step, step))

    def generate_sorted_list_with_duplicates(self, size, num_duplicates):
        base_list = self.generate_sorted_list(size - num_duplicates)
        duplicates = random.choices(base_list, k=num_duplicates)
        
        return sorted(base_list + duplicates)

    def generate_nearly_sorted_list(self, size, num_swaps):
        sorted_list = self.generate_sorted_list(size)
        for _ in range(num_swaps):
            i, j = random.sample(range(size), 2)
            sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        
        return sorted_list

