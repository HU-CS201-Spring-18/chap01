class USet:
    # Constructor.
    def __init__(self):
        self.dictionary = dict()  # dict offers O(1) lookup

    # String representation of an object for printing.
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
        val = self.dictionary.get(key)
        if val:
            return (key, val)

    def keys(self):
        return list(self.dictionary)

    def size(self):
        return len(self.dictionary)


