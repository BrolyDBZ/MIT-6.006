class Heap:
    def __init__(self):
        self.table=[None]
        self.key={}
    def swap(self,i,j):
        self.table[i], self.table[j] = self.table[j], self.table[i]
        self.key[self.table[i][0]], self.key[self.table[j][0]]=self.key[self.table[j][0]],self.key[self.table[i][0]]
    def Minheapify(self,i):
        length=len(self.table)
        left=2*i
        right=2*i+1
        smaller=i
        if left< length and self.table[left][1]<self.table[i][1]:
            smaller=left
        if right<length and self.table[right][1]<self.table[smaller][1]:
            smaller=right
        if smaller!=i:
            self.swap(i,smaller)
            self.Minheapify(smaller)

    def insert(self,i):
        self.table.append(i)
        self.key[i[0]]=len(self.table)-1
        self.decrease(len(self.table)-1)


    def decrease(self,index):
        while index>1:
            indx=index//2
            if self.table[indx][1]>self.table[index][1]:
                self.swap(indx,index)
                index=indx
            else:
                break

    def delete(self,i=1):
        length=len(self.table)-1
        self.swap(i,length)
        deleted=self.table[length]
        del(self.key[self.table[length][0]])
        del(self.table[length])
        self.Minheapify(i)
        return deleted

