class BinarySearch:
    def __init__(self, arr, low, high, x):
        self.arr = arr
        self.low = low
        self.high = high
        self.x = x

    def search(self):
        return self.binary_search(self.arr, self.low, self.high, self.x)

    def binary_search(self, arr, low, high, x):

        print(f"High, low: {high} {low}")
        if high >= low:

            mid = (high + low) // 2

            print(f"x, element: {x} {arr[mid].name}")

            if arr[mid].name.lower() == x.lower():
                return mid

            elif arr[mid].name.lower() > x.lower():
                print("Up")
                return self.binary_search(arr, low, mid - 1, x)

            else:
                print("Down")
                return self.binary_search(arr, mid + 1, high, x)

        else:
            return -1