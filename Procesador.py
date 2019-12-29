class Procesador:

    def Operador(self,operacion):
        simbolos = ['+','-','/','*']
        nums=[0]
        ops=['']
        x=0

        for i in range(len(operacion)):
            y=operacion[i]
            fin=0

            for j in simbolos:

                if y == j:
                    ops[x]=j
                    ops.append('')
                    x=x+1
                    fin=1
                    nums.append(0)
            if fin==0:        
        
                if y==0:
                    nums[x]==float(y)

                else:
                    nums[x]=(nums[x]*10)+float(y)
        i = 0
        for op in ops: 
                       
            if op=='+':
                x=nums[i]+nums[i+1]
                
            elif op=='-':
                x=nums[i]-nums[i+1]

            elif op=='/':
                x=float(nums[i]/nums[i+1])
                
            elif op=='*':
                x=nums[i]*nums[i+1]
            
            i+=1
            if len(nums)-1>=i:
                nums[i]=x

        return x


    def Parentesis(self,Ecuacion):
        resul=0
        paren=[]

        for i in range(len(Ecuacion)):

            if Ecuacion[i]=='(':
                paren.append(i)
            elif Ecuacion[i]==')':
                paren.append(i)

        x=0
        y=len(paren)-1
        Pares=[]

        for i in range(int(len(paren)/2)):
            par=[paren[x],paren[y]]
            Pares.append(par)
            x=x+1
            y=y-1
        return Pares


    def Analisis(self,Expresion):
        Ecuacion=list(Expresion)
        Pares=self.Parentesis(Ecuacion)
        Pares2=Pares

        for z in reversed(range(len(Pares))):
            exp=[]
            i=Pares2[z]

            for j in range(i[0]+1,i[1]):
                exp.append(Ecuacion[j])

            resul=self.Operador(exp)
            del Ecuacion[i[0]:i[1]+1]
            if len(Ecuacion)>0:
                temp=Ecuacion

                temp.append(temp[len(temp)-1])

                for j in reversed(range(i[0],len(Ecuacion))):
                    temp[j]=temp[j-1]

                Ecuacion=temp
                Ecuacion[i[0]]=str(resul)
                Pares2=self.Parentesis(Ecuacion)

        return resul