

class Heap:
    def __init__(self,data):
        self.data = data
        self.len = len(self.data)
        print(self.len)
        self.buildHeap()

    #下沉
    def shiftDown(self,e,i):
        j = 2*i + 1
        while j < self.len:
            #print(j+1," ",print(self.len))
            if j+1<self.len and self.data[j] > self.data[j+1]:
                j += 1
            if e < self.data[j]:
                break
            self.data[i] = self.data[j]
            i,j = j,2*j+1
        self.data[i] = e

    #上滑
    def shiftUp(self,e,j):
        i = (j-1) // 2
        while i >= 0 and e < self.data[i]:
            self.data[j] = self.data[i]
            j,i = i,(i-1) // 2
        self.data[j] = e

    def buildHeap(self):
        for i in range((self.len-2)//2,-1,-1):
            self.shiftDown(self.data[i],i)

    def push(self,e):
        self.data.append(None)
        self.len += 1
        self.shiftUp(e,self.len-1)

    def pop(self):
        if self.len == 0:
            raise RuntimeError("堆为空")
        e0 = self.data[0]
        e = self.data.pop()
        self.len -= 1
        self.shiftDown(e,0)
        return e0



    def show1(self,k):
        if k < self.len:
            print(self.data[k],end='')
            self.show1(2*k+1)
            self.show1(2*k+2)
    def show2(self,k):
        if k < self.len:
            self.show2(2*k+1)
            print(self.data[k],end='')
            self.show2(2*k+2)

if __name__ == '__main__':
    data = [9,7,3,5,6,4,8,2]
    heap = Heap(data)
    heap.show1(0)
    print()
    heap.show2(0)
    heap.push(0)
    print()
    print("push:")
    heap.show1(0)
    print()
    heap.show2(0)
    print()
    res = heap.pop()
    print("pop:")
    print(res)
    heap.show1(0)
    print()
    heap.show2(0)





