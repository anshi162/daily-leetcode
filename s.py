class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        def grid(m,n,b):
            l=[]
            if m<3 :
                if n<3:
                    for i in range(3):
                        for j in range(3):
                            l.append(b[i][j])
                    return l
                elif (n>2 and n<6):
                    for i in range(3):
                        for j in range(3,6):
                            l.append(b[i][j])
                    return l
                else:
                    for i in range(3):
                        for j in range(6,9):
                            l.append(b[i][j])
                    return l
            elif m>2 and m<6:
                if n<3:
                    for i in range(3,6):
                        for j in range(3):
                            l.append(b[i][j])
                    return l
                elif (n>2 and n<6):
                    for i in range(3,6):
                        for j in range(3,6):
                            l.append(b[i][j])
                    return l
                else:
                    for i in range(3,6):
                        for j in range(6,9):
                            l.append(b[i][j])
                    return l
            else:
                if n<3:
                    for i in range(6,9):
                        for j in range(3):
                            l.append(b[i][j])
                    return l
                elif (n>2 and n<6):
                    for i in range(6,9):
                        for j in range(3,6):
                            l.append(b[i][j])
                    return l
                else:
                    for i in range(6,9):
                        for j in range(6,9):
                            l.append(b[i][j])
                    return l
                
                    
                    
        
        m=len(b)
        n=len(b[0])
        for i in range(m):
            for j in range(n):
                l1=[b[k][j] for k in range(m)]
                l2=grid(i,j,b)
                if b[i][j].isdigit():
                    '''if b[i][j]=='3':
                        print(i,j)
                        print(l1)
                        print(l2)'''
                    if l1.count(b[i][j])>1 or l2.count(b[i][j])>1 or b[i].count(b[i][j])>1:
                        #print(i,j,b[i][j])
                        #print(l1)
                        #print(l2)
                        return False
        return True
