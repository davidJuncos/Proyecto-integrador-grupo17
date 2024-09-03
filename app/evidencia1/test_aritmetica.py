import aritmetica

def test_multiplicar():
    assert aritmetica.multiplicar(3, 4.567) == 13.70
    assert aritmetica.multiplicar(0, 10) == 0.00
    assert aritmetica.multiplicar(-2, 3) == -6.00

def test_sumar_n():
    assert aritmetica.sumar_n(1, 2, 3) == 6.00
    assert aritmetica.sumar_n(1.5, 2.5, 3.5) == 7.50
    assert aritmetica.sumar_n(-1, -2, -3) == -6.00

def test_promedio_n():
    assert aritmetica.promedio_n(1, 2, 3) == 2.00
    assert aritmetica.promedio_n(1.5, 2.5, 3.5) == 2.50
    assert aritmetica.promedio_n(-1, -2, -3) == -2.00

if __name__ == "__main__":
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todos los tests pasaron exitosamente.")