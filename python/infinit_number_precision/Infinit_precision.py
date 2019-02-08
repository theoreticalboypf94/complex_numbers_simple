class Infinit:

    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.len = front + back
        self.arr = [0] * (front + back)

    # @classmethod
    # def from_string(cls,txt):
    #     return cls.set_value(txt)

    def set_value(self, text : str):
        front, back = text.split(',')
        k = 0
        for i in back:
            self.arr[self.front + k] = int(i)
            k += 1

        k=0
        for i in front:
            self.arr[self.front - len(front) + k] = int(i)
            k += 1

    def __str__(self):
        result = ""
        start = 0
        for i in range(self.front):
            if self.arr[i] != 0:
                start = i
                break

        for i in range(start,self.front):
            result += str(self.arr[i])
        result += ","
        for i in range(self.back):
            result +=str(self.arr[self.front + i])
        return result

    def positive_overflow(self):
        for i in range(self.len-1, 1, -1):
            if self.arr[i] > 9:
                self.arr[i+1] += 1
                self.arr[i] -= 10

    def negative_overflow(self):
        pass

    def __add__(self, other):
        result = Infinit(self.front, self.end)
        for i in range(self.len):
            self.arr[i] += other.arr[i]
            self.positive_overflow()

a = Infinit(5,5)
a.set_value("434,343")
b = Infinit(5,5)
b.set_value("666,666")
print(a+b)
print(a)