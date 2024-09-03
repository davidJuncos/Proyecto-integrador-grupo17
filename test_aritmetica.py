#Iniciando punto 4
#utilizar aserciones nativas
# test_sumar
# input y pasarle los parametro 
def test_sumar(a,b):
   print("Suma...")
   
   suma = a + b
   assert suma == 12  
   assert 3 != 2 
   assert -1009,"Error "
   assert -1
   assert not False," Falso "
   print ("test completo")
      
#test_restar
def test_restar(a,b):
   print("Resta..." ) 
   
   resta= a-b 
   assert resta == 1 
   assert resta!=6
   assert a>b
   assert b<a
   assert resta >=1
   assert resta <=5
   print("test completo")
          
#test_dividir
def test_dividir(a,b):
   
   print("Dividir...")
   dividir = a / b
   try:
      1/0
   except ZeroDivisionError:
    pass
   else:
     assert False
   assert dividir > 0
   assert not (dividir < 0)
   print("test completo")
   
     
if __name__=="__main__":
 test_sumar(5,7)
 test_restar(6,5)
 test_dividir(4,2)
 