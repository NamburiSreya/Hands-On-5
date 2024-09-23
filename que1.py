class MinHeap:
    def __init__(self):
        self.elements = []

    @staticmethod
    def get_parent_index(child_index):
        """Return the parent index using bit manipulation."""
        return (child_index - 1) >> 1

    @staticmethod
    def get_left_child_index(parent_index):
        """Return the left child index using bit manipulation."""
        return (parent_index << 1) + 1

    @staticmethod
    def get_right_child_index(parent_index):
        """Return the right child index using bit manipulation."""
        return (parent_index << 1) + 2

    def sift_down(self, start_index):
        """Move an element down the heap to maintain the min-heap property."""
        smallest = start_index
        left = self.get_left_child_index(start_index)
        right = self.get_right_child_index(start_index)

        if left < len(self.elements) and self.elements[left] < self.elements[smallest]:
            smallest = left

        if right < len(self.elements) and self.elements[right] < self.elements[smallest]:
            smallest = right

        if smallest != start_index:
            self.elements[start_index], self.elements[smallest] = self.elements[smallest], self.elements[start_index]
            self.sift_down(smallest)

    def build_min_heap(self, input_array):
        """Build a min heap from an input array."""
        self.elements = input_array[:]
        for i in range(len(input_array) // 2, -1, -1):
            self.sift_down(i)

    def extract_min(self):
        """Remove and return the minimum element from the heap."""
        if not self.elements:
            return None
        if len(self.elements) == 1:
            return self.elements.pop()

        min_element = self.elements[0]
        self.elements[0] = self.elements.pop()
        self.sift_down(0)
        return min_element

    def insert(self, value):
        """Insert a new element into the heap."""
        self.elements.append(value)
        self.sift_up(len(self.elements) - 1)

    def sift_up(self, index):
        """Move an element up the heap to maintain the min-heap property."""
        while index > 0 and self.elements[self.get_parent_index(index)] > self.elements[index]:
            parent_index = self.get_parent_index(index)
            self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
            index = parent_index

# Example usage
def demonstrate_min_heap():
    min_heap = MinHeap()
    
    # Build heap
    initial_data = [4, 10, 3, 5, 1]
    min_heap.build_min_heap(initial_data)
    print("Initial Heap:", min_heap.elements)

    # Insert element
    min_heap.insert(2)
    print("After inserting 2:", min_heap.elements)

    # Extract minimum
    min_element = min_heap.extract_min()
    print("Extracted minimum:", min_element)
    print("Heap after extracting minimum:", min_heap.elements)

    # Example with custom data structure
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __lt__(self, other):
            return self.age < other.age

        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    person_heap = MinHeap()
    persons = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
    person_heap.build_min_heap(persons)
    print("Person Heap:", person_heap.elements)

if __name__ == "__main__":
    demonstrate_min_heap()