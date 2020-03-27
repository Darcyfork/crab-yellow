import functools
def example_cached_property():
    try:
        from functools import cached_property
    except ImportError:
        print('need python version higher than 3.8.0')        
        return 
    
    class DataSet:
        def __init__(self, sequence_of_numbers):
            self._data = sequence_of_numbers
            self.hsum_count = 0

        @functools.cached_property
        def dsum(self):
            return self.hsum(self._data)

        def hsum(self,nums):
            self.hsum_count += 1
            return sum(nums)

    d = DataSet([1,2,3])
    d.dsum , d.dsum
    assert d.hsum_count == 1

def example_lru_cache():
    @functools.lru_cache(maxsize=None, typed=False)
    def fib(n):
        if n == 0 or n == 1:
            return 1
        return fib(n-1) + fib(n-2)
    [fib(n) for n in range(16)]
    assert fib.cache_info().misses == 16 == fib.cache_info().currsize

if __name__ == '__main__':
    example_lru_cache()
    