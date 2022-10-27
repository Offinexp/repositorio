def soma(n1,n2):
    return print('a soma de ' ,n1,'e',n2,' = ',n1+n2)

def mult(n1,n2):
    return print('a multiplicacao de ' ,n1,'e',n2,' = ',n1*n2)
        

def sub(n1,n2):
     return print('a subtração de ' ,n1,'e',n2,' = ',n1-n2)
   

def div(n1,n2):
    if(n1 != 0 and n2 != 0):
         return print('a divisão de ' ,n1,'e',n2,' = ',n1/n2)        
    return 'algum dos valores e zero e nao pode ser dividido'    

soma(10,5)
mult(10,5)
div(10,5)
sub(10,5)


