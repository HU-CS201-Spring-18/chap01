from uset import USet

class Bag:
    # Constructor.
    def __init__(self):
        self.uset = USet()  # will store (key, [v1, v2, ... , vn]) pairs

    # String representation of an object for printing.
    def __str__(self):
        d = eval('{}'.format(self.uset))
        pairs = []
        for key, val_list in d.items():
            pairs.extend([(key,val) for val in val_list])
        return '{}'.format(pairs)
        
    def add(self, key, val):
        pair = self.uset.remove(key)
        if pair:
            key, val_list = pair
            val_list.append(val)
        else:
            val_list = [val]
        self.uset.add(key, val_list)

    def remove(self, key):
        pair = self.uset.remove(key)
        if not pair:
            return
        key, val_list = pair
        val = val_list.pop()
        if val_list:
            self.uset.add(key, val_list)
        return (key, val)
    
    def find(self, key):
        pair = self.uset.find(key)
        if not pair:
            return
        key, val_list = pair
        return (key, val_list[0])
    
    def find_all(self, key):
        pair = self.uset.find(key)
        if not pair:
            return []
        key, val_list = pair
        return [(key, val) for val in val_list]

    def keys(self):
        return self.uset.keys()
    
    def size(self):
        keys = self.keys()
        size = 0
        for k in keys:
            _, vals = self.uset.find(k)
            size += len(vals)
        return size

