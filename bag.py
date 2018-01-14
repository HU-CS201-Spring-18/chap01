from uset import USet

# Adapted from Exercise 1.5 in the book.

class Bag:
    def __init__(self):
        '''Initializes member variables.

        >>> bag = Bag()
        '''
        self.uset = USet()  # this is the underlying data structure.

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> bag = Bag()
        >>> print(bag)  # prints bag.__str__()
        '''
        pass

    def add(self, key, val):
        '''Adds the pair (key, val) to the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.size()
        1
        >>> bag.add(1, 10)
        >>> bag.size()
        2
        >>> bag.add(1, 20)
        >>> bag.size()
        3
        >>> bag.add(2, 20)
        >>> bag.size()
        4
        '''
        pass

    def remove(self, key):
        '''Removes a pair with key from the Bag and returns it.
        Returns None if no such pair exsits.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.remove(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.remove(2)
        (2,20)
        >>> bag.remove(20)
        >>>
        '''
        pass

    def find(self, key):
        '''Returns a pair from the Bag that contains key; None if no
        such pair exists.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.find(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.find(2)
        (2,20)
        >>> bag.find(20)
        >>>
        '''
        pass

    def size(self):
        '''Returns the number of pairs currently in the Bag.
        
        >>> bag = Bag()
        >>> bag.size()
        0
        >>> bag.add(1, 10)
        >>> bag.add(2, 20)
        >>> bag.size()
        2
        >>> bag.add(2, 30)
        >>> bag.size()
        3
        '''
        pass

    def keys(self):
        '''Returns a list of keys in the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.keys()
        [1, 2]
        '''
        pass
