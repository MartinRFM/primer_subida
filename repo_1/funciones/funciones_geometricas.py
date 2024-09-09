import math

def area_circulo() -> float:
    
    radio = float(input("Cual es el radio del circulo? "))
    
    superficie_circulo = math.pi * radio ** 2
    
    return superficie_circulo

def perimetro_circulo() -> float:
    
    radio = float(input("Cual es el radio del circulo? "))
    
    contorno = 2 * math.pi * radio
    
    return contorno

def area_rectangulo() -> int:
    
    base = int(input("Cual es la base del rectangulo? "))
    altura = int(input("Cual es la altura del rectangulo? "))
    
    superficie = base * altura
    
    return superficie

def perimetro_rectangulo() -> int:
    
    base = int(input("Cual es la base del rectangulo? "))
    altura = int(input("Cual es la altura del rectangulo? "))
    
    contorno = 2 * (base + altura)
    
    return contorno

def area_triangulo() -> int:
    
    base = int(input("Cual es la base del triangulo? "))
    altura = int(input("Cual es la altura del triangulo? "))
    
    superficie = (base * altura) / 2
    
    return superficie

def perimetro_triangulo() -> int:
    
    lado1 = int(input("Cuanto mide el primer lado del triangulo? "))
    lado2 = int(input("Cuanto mide el segundo lado del triangulo? "))
    lado3 = int(input("Cuanto mide el tercer lado del triangulo? "))
    
    contorno = lado1 + lado2 + lado3
    
    return contorno

def area_trapecio() -> float:
    
    base_mayor = float(input("¿Cuál es la base mayor del trapecio? "))
    base_menor = float(input("¿Cuál es la base menor del trapecio? "))
    
    altura = float(input("¿Cuál es la altura del trapecio? "))
    
    superficie = ((base_mayor + base_menor) * altura) / 2
    
    return superficie

def perimetro_trapecio() -> float:
    
    base_mayor = float(input("¿Cuál es la base mayor del trapecio? "))
    base_menor = float(input("¿Cuál es la base menor del trapecio? "))
    
    lado1 = float(input("¿Cuál es el primer lado no paralelo del trapecio? "))
    lado2 = float(input("¿Cuál es el segundo lado no paralelo del trapecio? "))
    
    contorno = base_mayor + base_menor + lado1 + lado2
    
    return contorno

def area_rombo() -> float:
    
    diagonal_mayor = float(input("¿Cuál es la diagonal mayor del rombo? "))
    diagonal_menor = float(input("¿Cuál es la diagonal menor del rombo? "))
    
    superficie = (diagonal_mayor * diagonal_menor) / 2
    
    return superficie

def perimetro_rombo() -> float:
    
    lado = float(input("¿Cuál es el lado del rombo? "))
    
    contorno = 4 * lado
    
    return contorno
