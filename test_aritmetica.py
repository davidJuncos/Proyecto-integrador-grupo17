#Iniciando punto 4
#utilizar aserciones nativas
# test_sumar

def test_sumar():
      print("Suma...")
      a = 5
      b = 7
      suma = a + b
      assert suma == 12  
      assert 3 != 2 
      assert -1009,"Error "
      assert -1
      assert not False," Falso "
      print ("test completo")
      
#test_restar
def test_restar():
      print("Resta...")
      a = 10
      b = 9
      resta= a-b 
      assert resta == 1 
      assert resta!=6
      assert a>b
      assert b<a
      assert resta >=1
      assert resta <=5
      print("test completo")
          
#test_dividir
def test_dividir():
     print("Dividir...")
     a= 45
     b= 5
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
 test_sumar()
 test_restar()
 test_dividir()
 