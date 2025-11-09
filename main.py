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

def ejecutar_demo_poo():
    """
    Ejecuta la demostración completa de Programación Orientada a Objetos.
    """
    print("""

DEMOSTRACIÓN DE POO EN CONSOLA 
  - Abstracción
  - Encapsulación
  - Herencia
  - Polimorfismo
  - Composición 

""")

trabajador1, estanteria1, supervisor1 = crear_instancias_estudiante_1()
trabajador2, jefe1, estanteria2 = crear_instancias_estudiante_2()

# SECCIÓN 2: ASIGNACIÓN DE TRABAJADORES
    # ======================================
    
    imprimir_separador("ASIGNACIÓN DE TRABAJADORES A SUPERVISOR")
    
    supervisor1.agregar_trabajador_a_cargo(trabajador1)
    supervisor1.agregar_trabajador_a_cargo(trabajador2)
    
    
    # SECCIÓN 3: ASIGNACIÓN Y COMPLETADO DE TAREAS
    # =============================================
    
    imprimir_separador("GESTIÓN DE TAREAS")
    
    print("\nSupervisor asigna tareas:")
    supervisor1.asignar_tarea(trabajador1, "Revisar estantería 0001")
    supervisor1.asignar_tarea(trabajador1, "Inocular tubulares del piso 1")
    supervisor1.asignar_tarea(trabajador2, "Revisar estantería 0002")
    
    print("\nTrabajador completa tareas:")
    trabajador1.completar_tarea(0)
    trabajador1.agregar_horas(4.5)
    
    # SECCIÓN 4: JEFE DE PLANTA CREA PUBLICACIONES
    # ============================================
    
    imprimir_separador(" PUBLICACIONES DEL JEFE DE PLANTA")
    
    jefe1.establecer_metas_produccion(500.0)
    jefe1.crear_publicacion(
        "Meta del mes",
        "La meta de producción para este mes es de 500kg de orellanas de alta calidad."
    )
    jefe1.crear_publicacion(
        "Horarios actualizados",
        "Se actualizan los horarios de turnos. Favor revisar el tablón."
    )

    # SECCIÓN 5: INICIAR PRODUCCIÓN
    # =============================

    imprimir_separador(" INICIANDO PRODUCCIÓN")
    
    print("\nIniciando estantería 0001 (Estudiante 1):")
    estanteria1.iniciar_produccion()
    
    print("\nIniciando estantería 0002 (Estudiante 2):")
    estanteria2.iniciar_produccion()
    
    print("\nCambiando fase de producción:")
    estanteria1.cambiar_fase("fructificación")

# SECCIÓN 6: MARCAR TUBULARES DEFECTUOSOS
    # =======================================

    imprimir_separador("MARCANDO TUBULARES DEFECTUOSOS")
    
    piso1 = estanteria1.get_piso(1)
    tubular_5 = piso1.get_tubular_por_numero(5)
    tubular_5.marcar_defectuoso()
    tubular_5.agregar_observacion("No presenta crecimiento de micelio")
    
    tubular_23 = piso1.get_tubular_por_numero(23)
    tubular_23.marcar_defectuoso()
    tubular_23.agregar_observacion("Contaminación detectada")

    # SECCIÓN 7: RESUMEN DE ESTANTERÍAS
    # =================================

    imprimir_separador("RESUMEN DE ESTANTERÍAS")
    
    print("\nEstantería 0001 (Estudiante 1):")
    print(estanteria1.generar_resumen())
    
    print("\nEstantería 0002 (Estudiante 2):")
    print(estanteria2.generar_resumen())

    # SECCIÓN 8:  DEMOSTRACIÓN DE POLIMORFISMO 
    # ============================================
    
    def demostrar_polimorfismo(usuarios: list):
        """
        Demuestra el polimorfismo en acción.
        """
        imprimir_separador("DEMOSTRACIÓN DE POLIMORFISMO")
        print("\nInvocando el MISMO método 'generarReporte()' en diferentes objetos:\n")
        
        for usuario in usuarios:
            print(f"\n► Tipo de objeto: {type(usuario).__name__}")
            print(usuario.generar_reporte())
            print("-" * 60)
        
        print("\nPOLIMORFISMO DEMOSTRADO:")
        print("  - Mismo método: generarReporte()")
        print("  - Diferentes comportamientos según el tipo de objeto")
    
    lista_usuarios = [trabajador1, trabajador2, supervisor1, jefe1]
    demostrar_polimorfismo(lista_usuarios)

    # SECCIÓN 9: COMPARACIÓN DE PERMISOS (Polimorfismo)
    # =================================================

    imprimir_separador("COMPARACIÓN DE PERMISOS (Polimorfismo)")
    
    print("\nInvocando el MISMO método 'obtenerPermisos()' en diferentes objetos:\n")
    
    for usuario in lista_usuarios:
        permisos = usuario.obtener_permisos()
        print(f"► {type(usuario).__name__}: {len(permisos)} permisos")
        print(f"   Primeros 3: {', '.join(permisos[:3])}")
        print()
    
    print("Mismo método, diferentes resultados según el ROL del usuario")
    

    # SECCIÓN 10: RESUMEN FINAL
    # ==========================

    imprimir_separador("📈 RESUMEN FINAL DEL SISTEMA")
    
    print(f"""

Tubulares totales: {estanteria1.contar_tubulares_total() + estanteria2.contar_tubulares_total()}
  - En producción: {estanteria1.obtener_estado_general()['tubulares_totales'] + estanteria2.obtener_estado_general()['tubulares_totales']}
  - Defectuosos: {estanteria1.contar_defectuosos_total() + estanteria2.contar_defectuosos_total()}

Tareas asignadas: 3
Tareas completadas: 1

Publicaciones creadas: 2
Meta de producción: 500kg

CONCEPTOS DE POO APLICADOS:
  - Abstracción (Usuario abstracta)
  - Encapsulación (atributos privados)
  - Herencia (Trabajador, Supervisor, JefePlanta → Usuario)
  - Polimorfismo (generarReporte(), obtenerPermisos())
  - Composición (Estantería → Piso → Tubular)
""")
    
    imprimir_separador("🎉 DEMOSTRACIÓN DE POO FINALIZADA")
    input("\nPresiona Enter para volver al menú principal...")


def ejecutar_interfaz_grafica():
    """
    Ejecuta el sistema con interfaz gráfica.
    """
    try:
        from sistema_gui import SistemaOrellanas
        print("\n  Iniciando sistema con interfaz gráfica...")
        app = SistemaOrellanas()
        app.ejecutar()
    except ImportError as e:
        print(f" Error: No se pudo cargar la interfaz gráfica")
        print(f"   Detalles: {e}")
        print("   Asegúrate de tener el archivo 'sistema_gui.py' en la misma carpeta")
        input("\nPresiona Enter para continuar...")
    except Exception as e:
        print(f" Error inesperado: {e}")
        input("\nPresiona Enter para continuar...")


def main():
    """Función principal con menú interactivo."""
    while True:
        # Limpiar pantalla (funciona en Windows y Linux/Mac)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        mostrar_menu_principal()
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            if opcion == "1":
                ejecutar_demo_poo()
            elif opcion == "2":
                ejecutar_interfaz_grafica()
            elif opcion == "3":
                print("\n¡Gracias por usar el Sistema de Gestión de Orellanas!")
                break
            else:
                print("\n Opción inválida. Por favor, selecciona 1, 2 o 3.")
                input("Presiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n Programa interrumpido por el usuario. ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"\n Error inesperado: {e}")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    """
    Punto de entrada principal del sistema.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Programa finalizado. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n Error crítico: {e}")
        import traceback
        traceback.print_exc()
