import math

def seno() -> float:
    
    angulo = float(input("Cuanto mide el angulo? "))
    
    angulo_seno = math.sin(math.radians(angulo))
    
    return angulo_seno

def coseno() -> float:
    
    angulo = float(input("Cuanto mide el angulo? "))
    
    angulo_coseno = math.cos(math.radians(angulo))
    
    return angulo_coseno

def tangente() -> float:
    
    angulo = float(input("Cuanto mide el angulo? "))
    
    angulo_tangente = math.tan(math.radians(angulo))
    
    return angulo_tangente

def arcoseno() -> float:
    
    valor = float(input("Que valor tiene? "))
    
    valor_arcoseno = math.degrees(math.asin(valor))
    
    return valor_arcoseno

def arcocoseno() -> float:
    
    valor = float(input("Que valor tiene? "))
    
    valor_arcocoseno = math.degrees(math.acos(valor))
    
    return valor_arcocoseno

def arcotangente() -> float:
    
    valor = float(input("Que valor tiene? "))
    
    valor_arcotan = math.degrees(math.atan(valor))
    
    return valor_arcotan