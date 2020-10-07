class Stack:
  def __init__(self):
    self.__datos=[]

  def is_empty(self):
    return len(self.__datos) == 0
  
  def get_top(self):
    return self.__datos[-1]#regresa el ultimo elemento

  def pop(self):
    return self.__datos.pop()
  
  def push(self,valor):
        self.__datos.append(valor)

  def get_length(self):#numero de elementos 
    return len(self.__datos)

  def to_string(self): #imprimir datos 
    print("---------------")
    for ele in self.__datos[-1::-1]:
      print(f"{ele}")
    print("----------------")



    

    
        
        




 
        
    
    
        
    
    
  
  
  
