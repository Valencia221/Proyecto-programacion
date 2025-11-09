"""
MAIN.PY - Script Principal
Sistema de Gestión de Producción de Orellanas

Este script ofrece DOS opciones:
1. Demostración de POO en consola
2. Sistema completo con interfaz gráfica

Autores: [Nombres de integrantes]
Códigos: [Códigos de integrantes]
Fecha: Noviembre 2024
"""

import sys
import os

# Agregar la carpeta clases al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'clases'))

from clases.usuario import Usuario
from clases.trabajador import Trabajador
from clases.supervisor import Supervisor
from clases.jefe_planta import JefePlanta
from clases.administrador import Administrador
from clases.tubular import Tubular
from clases.piso import Piso
from clases.estanteria import Estanteria
from clases.publicacion import Publicacion
from clases.reporte import Reporte
from clases.registro_tiempo import RegistroTiempo
from clases.alerta import Alerta


def imprimir_separador(titulo=""):
    """Imprime un separador visual."""
    print("\n" + "="*60)
    if titulo:
        print(f"  {titulo}")
        print("="*60)


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    print("""
SISTEMA DE GESTIÓN DE PRODUCCIÓN DE ORELLANAS
          
Selecciona una opción:
1.  Demostración de POO (Consola)
2.  Sistema con Interfaz Gráfica  
3. Salir
""")


def crear_instancias_estudiante_1():
   
    imprimir_separador("INSTANCIAS DEL ESTUDIANTE 1")
    
    print("\n1️ Creando Trabajador...")
    trabajador1 = Trabajador(
        nombre="Juan",
        apellido="Pérez",
        username="jperez",
        password="segura123",
        email="juan.perez@orellanas.com",
        turno="mañana"
    )
    print(f"  {trabajador1}")
    
    print("\n2️ Creando Estantería...")
    estanteria1 = Estanteria("0001")
    print(f"  {estanteria1}")
    print(f"   - Pisos creados: {Estanteria.NUMERO_PISOS}")
    print(f"   - Tubulares totales: {estanteria1.contar_tubulares_total()}")
    
    print("\n3️ Creando Supervisor...")
    supervisor1 = Supervisor(
        nombre="Carlos",
        apellido="Ramírez",
        username="cramirez",
        password="super123",
        email="carlos.ramirez@orellanas.com",
        area="Producción"
    )
    print(f" {supervisor1}")
    
    return trabajador1, estanteria1, supervisor1

def crear_instancias_estudiante_2():
    imprimir_separador("INSTANCIAS DEL ESTUDIANTE 2")
    print("\n4️ Creando Trabajador...")
    trabajador2 = Trabajador(
        nombre="María",
        apellido="González",
        username="mgonzalez",
        password="segura456",
        email="maria.gonzalez@orellanas.com",
        turno="tarde"
    )
    print(f"  {trabajador2}")
    
    print("\n5️⃣ Creando Jefe de Planta...")
    jefe1 = JefePlanta(
        nombre="Ana",
        apellido="Martínez",
        username="amartinez",
        password="jefe456",
        email="ana.martinez@orellanas.com"
    )
    print(f"  {jefe1}")
    
    print("\n6️⃣ Creando Estantería...")
    estanteria2 = Estanteria("0002")
    print(f" {estanteria2}")
    print(f" - Pisos creados: {Estanteria.NUMERO_PISOS}")
    print(f" - Tubulares totales: {estanteria2.contar_tubulares_total()}")
    
    return trabajador2, jefe1, estanteria2


