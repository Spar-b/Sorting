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


class InterpolationSearch:
    def __init__(self, arr, low, high, x):
        self.arr = arr
        self.low = low
        self.high = high
        self.x = x

    def search(self):
        return self.interpolation_search(self.arr, self.low, self.high, self.x)

    def interpolation_search(self, arr, low, high, x):
        if low <= high:
            if hash(arr[high].name) - hash(arr[low].name) != 0:
                pos = low + int((float(high - low) / (hash(arr[high].name) - hash(arr[low].name))) * (
                            hash(x) - hash(arr[low].name)))

                if hash(arr[pos].name) == hash(x):
                    return pos

                elif hash(arr[pos].name) < hash(x):
                    return self.interpolation_search(arr, pos + 1, high, x)

                else:
                    return self.interpolation_search(arr, low, pos - 1, x)

            else:
                return -1

        else:
            return -1