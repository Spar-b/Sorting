import json
from Shop import Shop


class SortingAlgorithm:
    def __init__(self):
        self.shop_list = []

    def read_data(self):
        # Read data from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)

        # Create a list of Shop objects
        self.shop_list = [Shop(item["name"], item["overall_sold"]) for item in data]

    def sort_by_name(self):
        n = len(self.shop_list)
        for i in range(n):
            for j in range(n - i - 1):
                current_shop = self.shop_list[j]
                next_shop = self.shop_list[j + 1]

                current_name = current_shop.name.lower()
                next_name = next_shop.name.lower()

                current_sold = int(current_shop.overall_sold)
                next_sold = int(next_shop.overall_sold)

                names_order = current_name > next_name
                sold_order = current_sold > next_sold

                if names_order or (current_name == next_name and sold_order):
                    self.shop_list[j], self.shop_list[j + 1] = next_shop, current_shop


class BubbleSort(SortingAlgorithm):
    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Bubble sort")
        return self.shop_list


class ShakerSort(SortingAlgorithm):
    def sort_by_name(self):
        n = len(self.shop_list)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            # Traverse from left to right
            for i in range(start, end):
                if self.shop_list[i].name.lower() > self.shop_list[i + 1].name.lower():
                    self.shop_list[i], self.shop_list[i + 1] = self.shop_list[i + 1], self.shop_list[i]
                    swapped = True
            end -= 1

            # Traverse from right to left
            for i in range(end - 1, start - 1, -1):
                if self.shop_list[i].name.lower() > self.shop_list[i + 1].name.lower():
                    self.shop_list[i], self.shop_list[i + 1] = self.shop_list[i + 1], self.shop_list[i]
                    swapped = True
            start += 1

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Shaker sort")
        return self.shop_list


class InsertionSort(SortingAlgorithm):
    def sort_by_name(self):
        n = len(self.shop_list)
        for i in range(1, n):
            current_shop = self.shop_list[i]
            j = i - 1
            while j >= 0 and (self.shop_list[j].name.lower() > current_shop.name.lower() or
                              (self.shop_list[j].name.lower() == current_shop.name.lower() and
                               int(self.shop_list[j].overall_sold) > int(current_shop.overall_sold))):
                self.shop_list[j + 1] = self.shop_list[j]
                j -= 1
            self.shop_list[j + 1] = current_shop

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Insertion sort")
        return self.shop_list


class SelectionSort(SortingAlgorithm):
    def sort_by_name(self):
        n = len(self.shop_list)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if (self.shop_list[j].name.lower() < self.shop_list[min_index].name.lower() or
                    (self.shop_list[j].name.lower() == self.shop_list[min_index].name.lower() and
                     int(self.shop_list[j].overall_sold) < int(self.shop_list[min_index].overall_sold))):
                    min_index = j
            if min_index != i:
                self.shop_list[i], self.shop_list[min_index] = self.shop_list[min_index], self.shop_list[i]

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Selection sort")
        return self.shop_list


class ShellSort(SortingAlgorithm):
    def sort_by_name(self, gap_sequence="sedgewick"):
        n = len(self.shop_list)
        if gap_sequence == "sedgewick":
            gap = 1
            while gap < n // 3:
                gap = gap * 3 + 1
        elif gap_sequence == "knuth":
            gap = 1
            while gap < n // 3:
                gap = gap * 3 + 1
            gap = (gap - 1) // 3

        while gap > 0:
            for i in range(gap, n):
                current_shop = self.shop_list[i]
                j = i
                while j >= gap and (self.shop_list[j - gap].name.lower() > current_shop.name.lower() or
                                     (self.shop_list[j - gap].name.lower() == current_shop.name.lower() and
                                      int(self.shop_list[j - gap].overall_sold) > int(current_shop.overall_sold))):
                    self.shop_list[j] = self.shop_list[j - gap]
                    j -= gap
                self.shop_list[j] = current_shop
            gap //= 3

    def sort(self, gap_sequence="sedgewick"):
        self.read_data()
        self.sort_by_name(gap_sequence)
        print("Shell sort with", gap_sequence.capitalize(), "'s formula")
        return self.shop_list


class QuickSort(SortingAlgorithm):
    def sort_by_name(self):
        self.quick_sort(0, len(self.shop_list) - 1)

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.shop_list[(low + high) // 2]
        i = low - 1
        for j in range(low, high):
            if (self.shop_list[j].name.lower() < pivot.name.lower() or
                    (self.shop_list[j].name.lower() == pivot.name.lower() and
                     int(self.shop_list[j].overall_sold) < int(pivot.overall_sold))):
                i += 1
                self.shop_list[i], self.shop_list[j] = self.shop_list[j], self.shop_list[i]
        self.shop_list[i + 1], self.shop_list[high] = self.shop_list[high], self.shop_list[i + 1]
        return i + 1

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Quick sort")
        return self.shop_list


class HeapSortWithFormula1(SortingAlgorithm):
    def sort_by_name(self):
        n = len(self.shop_list)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Heap sort
        for i in range(n - 1, 0, -1):
            self.shop_list[0], self.shop_list[i] = self.shop_list[i], self.shop_list[0]
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and (self.shop_list[left].name.lower() > self.shop_list[largest].name.lower() or
                         (self.shop_list[left].name.lower() == self.shop_list[largest].name.lower() and
                          int(self.shop_list[left].overall_sold) > int(self.shop_list[largest].overall_sold))):
            largest = left

        if right < n and (self.shop_list[right].name.lower() > self.shop_list[largest].name.lower() or
                          (self.shop_list[right].name.lower() == self.shop_list[largest].name.lower() and
                           int(self.shop_list[right].overall_sold) > int(self.shop_list[largest].overall_sold))):
            largest = right

        if largest != i:
            self.shop_list[i], self.shop_list[largest] = self.shop_list[largest], self.shop_list[i]
            self.heapify(n, largest)

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Heap sort with Formula 1")
        return self.shop_list

class HeapSortWithFormula2(SortingAlgorithm):
    def sort_by_name(self):
        n = len(self.shop_list)

        # Build min heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Heap sort
        for i in range(n - 1, 0, -1):
            self.shop_list[0], self.shop_list[i] = self.shop_list[i], self.shop_list[0]
            self.heapify(i, 0)

    def heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and (self.shop_list[left].name.lower() < self.shop_list[smallest].name.lower() or
                         (self.shop_list[left].name.lower() == self.shop_list[smallest].name.lower() and
                          int(self.shop_list[left].overall_sold) < int(self.shop_list[smallest].overall_sold))):
            smallest = left

        if right < n and (self.shop_list[right].name.lower() < self.shop_list[smallest].name.lower() or
                          (self.shop_list[right].name.lower() == self.shop_list[smallest].name.lower() and
                           int(self.shop_list[right].overall_sold) < int(self.shop_list[smallest].overall_sold))):
            smallest = right

        if smallest != i:
            self.shop_list[i], self.shop_list[smallest] = self.shop_list[smallest], self.shop_list[i]
            self.heapify(n, smallest)

    def sort(self):
        self.read_data()
        self.sort_by_name()
        print("Heap sort with Formula 2")
        return self.shop_list
