class Set:
    # Creates an empty set instance.
    def __init__(self, elems):
        self._theElements = list(elems)

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self._theElements:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self._theElements, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if this set is a subset of SetB
    def isSubsetOf(self, setB):
        for element in self._theElements:
            if element not in setB:
                return False
        return True

    def properSubset(self, setB):
        if self._theElements == setB._theElements:
            return False
        for elem in self._theElements:
            if self.isSubsetOf(setB):
                return True
            else:
                return False

    def intersect(self, st):
        x = []
        for ele in self._theElements:
            if ele in st:
                x.append(ele)
        return x

    def difference(self, st):
        x = []
        for ele in self._theElements:
            if ele not in st:
                x.append(ele)
        return x

    def union(self, st):
        x = []
        x = self.difference(st)
        for ele in st._theElements:
            x.append(ele)

        return x
