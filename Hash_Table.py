class HashTable:
    def __init__(self):
        self.hash_tab = [[]] * 10

    def insert(self, element):
        if not self.search(element):
            cell = element % 10
            self.hash_tab[cell].append(element)
        return

    def search(self, element):
        cell = element % 10
        for i in self.hash_tab[cell]:
            if i == element:
                return True
        return False

    def delete(self, element):
        if self.search(element):
            cell = element % 10
            for i in self.hash_tab[cell]:
                if i == element:
                    self.hash_tab[cell].remove(i)
                    return


def run_tests():
    hash_table = HashTable()

    # Test 1: Insert and Search
    hash_table.insert(5)
    assert hash_table.search(5) is True
    assert hash_table.search(10) is False

    # Test 2: Delete
    hash_table.delete(5)
    assert hash_table.search(5) is False

    # Test 3: Collision Handling
    hash_table.insert(5)
    hash_table.insert(15)  # Collides with 5 at index 5
    assert hash_table.search(5) is True
    assert hash_table.search(15) is True

    # Test 4: Inserting the same element twice
    hash_table.insert(5)
    assert hash_table.search(5) is True

    # Test 5: Deleting a non-existing element
    hash_table.insert(5)
    assert hash_table.search(5) is True
    hash_table.delete(10)  # 10 wasn't inserted
    assert hash_table.search(5) is True

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
