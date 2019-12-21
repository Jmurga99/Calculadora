class Procesador:

    def Analisis(self,Ecuacion):
        simbolos = ['+','-','/','*']
        nums=[0,0]
        op=''
        x=0

        for i in range(len(Ecuacion)):
            y=Ecuacion[i]
            fin=0

            for j in simbolos:

                if y == j:
                    op=j
                    x=x+1
                    fin=1
            if fin==0:        
        
                if y==0:
                    nums[x]==int(y)

                else:
                    nums[x]=(nums[x]*10)+int(y)

            
        if op=='+':
            x=nums[0]+nums[1]
            
        elif op=='-':
            x=nums[0]-nums[1]

        elif op=='/':
            x=float(nums[0]/nums[1])
            
        elif op=='*':
            x=nums[0]*nums[1]

        return x