

def suma() -> int:
    
    """_summary_

    Args:
        num1 (int): _description_ primer numero a sumar
        num2 (int): _description_ segundo numero a sumar

    Returns:
        int: _description_ La suma de 2 numeros
    """
    
    num1 = int(input("Cual es el  primer sumando? "))
    num2 = int(input("Cual es el segundo sumando? "))
    
    integracion = num1 + num2
    
    return integracion

def resta() -> int:
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    num1 = int(input("Cual es el  minuendo? "))
    num2 = int(input("Cual es el sustraendo? "))
    
    sustraccion = num1 - num2
    
    return sustraccion

def multiplicacion() -> int:
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    num1 = int(input("Cual es el  multiplicando? "))
    num2 = int(input("Cual es el multiplicador? "))
    
    proliferacion = num1 * num2
    
    return proliferacion

def division() -> int:
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    num1 = int(input("Cual es el numero a dividir? "))
    num2 = int(input("Cual es el divisor? "))
    
    if num2 != 0:
        fraccionamiento = num1 / num2
        return fraccionamiento
    else:
        return "Error: No se puede dividir por cero."

def es_primo() -> int:
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    n = int(input("Que numero queres saber si es primo? "))
    
    if n < 2:
        return f"{n} no es un numero primo"
    
    for primo in range(2, int(n**0.5) + 1):
        if n % primo == 0:
            return f"{n} no es un numero primo"
    
    return f"{n} es un numero primo"


