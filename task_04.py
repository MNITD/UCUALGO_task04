

class Median:
    def __init__(self):
        self.H_high = []
        self.H_low = []

    def max_heapify(self, x):
        left = x * 2 + 1
        right = x * 2 + 2
        largest = x
        if left < len(self.H_low) and self.H_low[left] > self.H_low[x]:
            largest = left
        if right < len(self.H_low) and self.H_low[right] > self.H_low[largest]:
            largest = right
        if largest != x:
            temp = self.H_low[x]
            self.H_low[x] = self.H_low[largest]
            self.H_low[largest] = temp
            self.max_heapify(largest)

    def min_heapify(self, x):
        left = x * 2 + 1
        right = x * 2 + 2
        least = x
        if left < len(self.H_high) and self.H_high[left] < self.H_high[x]:
            least = left
        if right < len(self.H_high) and self.H_high[right] < self.H_high[least]:
            least = right
        if least != x:
            temp = self.H_high[x]
            self.H_high[x] = self.H_high[least]
            self.H_high[least] = temp
            self.min_heapify(least)

    def extract_max(self):
        temp = self.H_low[0]
        self.H_low[0] = self.H_low[len(self.H_low) - 1]
        self.H_low.pop(len(self.H_low) - 1)
        self.max_heapify(0)
        return temp

    def extract_min(self):
        temp = self.H_high[0]
        self.H_high[0] = self.H_high[len(self.H_high) - 1]
        self.H_high.pop(len(self.H_high) - 1)
        self.min_heapify(0)
        return temp

    def maxheap_insert(self, value):
        self.H_low.append(value)
        # self.max_heapify(len(self.H_low)/2 - 1)
        i = len(self.H_low) - 1
        while i > 0:
            p = int(i / 2)
            if i % 2 == 0:
                p -= 1
            if self.H_low[i] > self.H_low[p]:
                temp = self.H_low[p]
                self.H_low[p] = self.H_low[i]
                self.H_low[i] = temp
            else:
                break
            i = p

    def minheap_insert(self, value):
        self.H_high.append(value)
        i = len(self.H_high) - 1
        while i > 0:
            p = int(i / 2)
            if i % 2 == 0:
                p -= 1
            if self.H_high[i] < self.H_high[p]:
                temp = self.H_high[p]
                self.H_high[p] = self.H_high[i]
                self.H_high[i] = temp
            else:
                break
            i = p

    def add_element(self, value):
        if len(self.H_low) == 0 or value < self.H_low[0]:
            self.maxheap_insert(value)
            if len(self.H_low) - len(self.H_high) > 1:
                self.minheap_insert(self.extract_max())
        else:
            self.minheap_insert(value)
            if len(self.H_high) - len(self.H_low) > 1:
                self.maxheap_insert(self.extract_min())

    def get_median(self):
        if len(self.H_low) > len(self.H_high):
            return self.H_low[0]
        elif len(self.H_low) < len(self.H_high):
            return self.H_high[0]
        else:
            return (self.H_low[0], self.H_high[0])

    def get_maxheap_elements(self):
        return self.H_low

    def get_minheap_elements(self):
        return self.H_high


# ar1 = [1,2,3,4,5,6,7,8,9,10]
# ar2 = [10,9,8,7,6,5,4,3,2,1]
# ar3 = [1,5,3,9,2,8,10,4,7,6]
#
# m = Median()
# for i in ar1:
#     m.add_element(i)
# print(m.get_median())
# print(m.get_minheap_elements())
# print(m.get_maxheap_elements())
#
# m2 =  Median()
# for i in ar2:
#     m2.add_element(i)
# print(m2.get_median())
# print(m2.get_minheap_elements())
# print(m2.get_maxheap_elements())
#
# m3 = Median()
# for i in ar3:
#     m3.add_element(i)
# print(m3.get_median())
# print(m3.get_minheap_elements())
# print(m3.get_maxheap_elements())