class Matrix():
    result=[]
    def Multi(self,m1,m2):
        if(len(m1[0]) != len(m2)):
            print("这两个不可以向乘")
            return "wrong"
        else:
            for i in range(0,len(m1)):
                self.result.append([])
                for j in range(0,len(m2[0])):
                    temp=0
                    for x in range(0,len(m1[0])):
                        temp=temp+m1[i][x]*m2[x][j]
                    self.result[i].append(temp)
                    #self.result.append(temp)
        #print()
        return self.result
if __name__ =="__main__":
    m1=[
        [1,2,4],
        [1,2,4],
    ]
    m2=[
        [1,2],
        [1,2],
        [1,2]
    ]
    M1=Matrix()
    print(M1.Multi(m1,m2))

