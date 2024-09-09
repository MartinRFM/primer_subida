def fibonacci() -> int:
    
    n = int(input("Ingrese el numero"))
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci_final = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci_final

def factorial() -> int:
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    n = int(input("Que numero queres factorizar? "))
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def potencia() ->int:
    
    base = int(input("Cual es la base de la potencia? "))
    exponente = int(input("Cual es el exponente? "))
    
    if exponente == 0:
        return 1
    else:
        potenciacion = base * potencia(base, exponente-1)
        return potenciacion