import bisect  # for binary search.
               # https://docs.python.org/3.6/library/bisect.html

class SSet:
    def __init__(self):
        self.dictionary = dict()

    def __str__(self):
        return '{}'.format(self.dictionary)
        
    def add(self, key, val):
        if key in self.dictionary:
            return False
        self.dictionary[key] = val
        return True
    
    def remove(self, key):
        try:
            val = self.dictionary.pop(key)
            return (key, val)
        except:
            pass
    
    def find(self, key):
        pairs = sorted(self.dictionary.items())
        i = bisect.bisect_left(pairs, (key,))
        if i != len(pairs):
            return pairs[i]

    def keys(self):
        return list(self.dictionary)

    def size(self):
        return len(self.dictionary)


