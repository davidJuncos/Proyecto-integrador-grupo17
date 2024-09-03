import aritmetica

def test_sumar(a,b):
   print("Suma...")
   
   suma = a + b
   assert suma == 12  
   assert 3 != 2 
   assert -1009,"Error "
   assert -1
   assert not False," Falso "
   print ("test completo")
      
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
   
def test_multiplicar():
    assert aritmetica.multiplicar(3, 4.567) == 13.70
    assert aritmetica.multiplicar(0, 12323) == 0.00
    assert aritmetica.multiplicar(-2, 3) == -6.00

def test_sumar_n():
    assert aritmetica.sumar_n(1, 2, 1, 1, 5) == 10.00
    assert aritmetica.sumar_n(1.5, 2.5, 3.5) == 7.50
    assert aritmetica.sumar_n(-1, -2, -3) == -6.00

def test_promedio_n():
    assert aritmetica.promedio_n(1, 2, 3) == 2.00
    assert aritmetica.promedio_n(1.5, 2.5, 3.5) == 2.50
    assert aritmetica.promedio_n(-1, -2, -3) == -2.00
    assert aritmetica.promedio_n(10, 1, 10, -3) == 4.50

if __name__ == "__main__":
    test_sumar(5,7)
    test_restar(6,5)
    test_dividir(4,2)
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los tests pasaron exitosamente.")