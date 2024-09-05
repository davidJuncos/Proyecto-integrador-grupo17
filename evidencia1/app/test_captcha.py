import pytest
from unittest.mock import patch
import aritmetica
import captcha

def test_generar_captcha_tipos_correctos():
    operacion, argumentos, resultado = captcha.generar_captcha()
    assert callable(operacion)
    assert isinstance(argumentos, list)
    assert isinstance(resultado, float)

def test_generar_captcha_rangos_esperados():
    operacion, argumentos, resultado = captcha.generar_captcha()
    for arg in argumentos:
        assert 1.5 <= arg <= 30.0

def test_formatear_operacion_sumar_n():
    resultado = captcha.formatear_operacion(aritmetica.sumar_n, [2.5, 3.14])
    assert resultado == "2.50 + 3.14"

def test_formatear_operacion_multiplicar():
    resultado = captcha.formatear_operacion(aritmetica.multiplicar,[5.0, 2.5])
    assert resultado == "5.00 * 2.50"

def test_formatear_operacion_promedio():
    resultado = captcha.formatear_operacion(aritmetica.promedio_n, [3.45, 10.5, 5.0])
    assert resultado == "(3.45 + 10.50 + 5.00) / 3"

def test_formatear_operacion_suma_numeros():
    resultado = captcha.formatear_operacion(aritmetica.suma_numeros, [6.54, 4.56])
    assert resultado == "6.54 + 4.56"

def test_formatear_operacion_restar_numeros():
    resultado = captcha.formatear_operacion(aritmetica.restar_numeros, [7.0, 5.7])
    assert resultado == "7.00 - 5.70"

def test_formatear_operacion_dividir_numeros():
    resultado = captcha.formatear_operacion(aritmetica.dividir_numeros, [3.9, 5.81])
    assert resultado == "3.90 / 5.81"

def test_main():
    def mock_generar_captcha():
        return aritmetica.promedio_n, [1.5, 2.5, 3.5], 2.5

    with patch('captcha.generar_captcha', mock_generar_captcha):
        with patch('builtins.print') as mock_print:
            captcha.main(resultado_usuario = 2.5)
    
    mock_print.assert_any_call("Usuario Registrado")

def test_main_input_invalido():
    with patch('builtins.input', side_effect = ['invalid', '2.5']):
        def mock_generar_captcha():
            return aritmetica.promedio_n, [1.5, 2.5, 3.5], 2.5
        
        with patch('captcha.generar_captcha', mock_generar_captcha):
            with patch('builtins.print') as mock_print:
                captcha.main()
                
                mock_print.assert_any_call("Por favor, ingresa un número válido.")
                mock_print.assert_any_call("Usuario Registrado")
