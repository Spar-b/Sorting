class InterpolationSearch:
    def __init__(self, arr, low, high, x):
        self.arr = sorted(arr, key=lambda p: p.name)  # Ensure it's sorted
        self.low = 0  # Always start from the beginning
        self.high = len(arr) - 1  # Always go to the end
        self.x = x

    def search(self):
        indices = []
        self.interpolation_search(self.arr, self.low, self.high, self.x, indices)
        return indices

    def interpolation_search(self, arr, low, high, x, indices):
        if low <= high and low < len(arr) and high < len(arr):
            if arr[high].name > arr[low].name:
                def string_to_number(s, max_chars=5):
                    return sum(ord(c) * (256 ** i) for i, c in enumerate(s[:max_chars]))

                pos = low + int(
                    (float(high - low) / (string_to_number(arr[high].name) - string_to_number(arr[low].name))) * (
                            string_to_number(x) - string_to_number(arr[low].name)))
                pos = max(low, min(pos, high))  # Ensure pos is within [low, high]

                if arr[pos].name == x:
                    indices.append(pos)
                    # Search for duplicates on the left
                    left = pos - 1
                    while left >= 0 and arr[left].name == x:
                        indices.append(left)
                        left -= 1
                    # Search for duplicates on the right
                    right = pos + 1
                    while right < len(arr) and arr[right].name == x:
                        indices.append(right)
                        right += 1

                elif arr[pos].name < x:
                    self.interpolation_search(arr, pos + 1, high, x, indices)

                else:
                    self.interpolation_search(arr, low, pos - 1, x, indices)

            else:
                # If names at low and high are the same, do linear search
                for i in range(low, high + 1):
                    if arr[i].name == x:
                        indices.append(i)

        return indices

class BinarySearch:
    def __init__(self, arr, low, high, x):
        self.arr = sorted(arr, key=lambda p: p.name)  # Ensure it's sorted
        self.low = low
        self.high = high
        self.x = x

    def search(self):
        indices = []
        self.binary_search(self.arr, self.low, self.high, self.x, indices)
        return indices

    def binary_search(self, arr, low, high, x, indices):
        if low <= high:
            mid = low + (high - low) // 2
            if arr[mid].name == x:
                indices.append(mid)
                # Search for duplicates on the left
                left = mid - 1
                while left >= 0 and arr[left].name == x:
                    indices.append(left)
                    left -= 1
                # Search for duplicates on the right
                right = mid + 1
                while right < len(arr) and arr[right].name == x:
                    indices.append(right)
                    right += 1
            elif arr[mid].name < x:
                self.binary_search(arr, mid + 1, high, x, indices)
            else:
                self.binary_search(arr, low, mid - 1, x, indices)
        return indices