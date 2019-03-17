class The_Location:
    def __init__(self,row=0,column=0,maxValue=0):
        self.row=row
        self.column=column
        self.maxValue=maxValue
    def LocationlocateLargest(self,a):
        self.maxValue=a
        s=""
        list1=[[1, 2, 3], [4, 5, 6], [7,8,9]]

        for i in range(0,len(list1)):
            for j in range(0,len(list1[i])):
                if self.maxValue==list1[i][j]:
                    self.row=i+1
                    self.column=j+1
        s=str(self.row)+","+str(self.column)
        return s
obj=The_Location()
print(obj.LocationlocateLargest(6))
