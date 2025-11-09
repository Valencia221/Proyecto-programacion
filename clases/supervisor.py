"""
Clase Supervisor - Hereda de Usuario
Sistema de Gestión de Producción de Orellanas

Fecha: Noviembre 2025
"""

from clases.usuario import Usuario
from datetime import datetime


class Supervisor(Usuario):
    """
    Clase que representa a un supervisor de área.
    Hereda de Usuario e implementa los métodos abstractos.
    
    Demuestra:
    - Herencia: extends Usuario
    - Polimorfismo: Implementa generarReporte() con información de supervisión
    - Encapsulación: Atributos privados propios
    """
    
    def __init__(self, nombre: str, apellido: str, username: str, 
                 password: str, email: str, area: str):
        """
        Constructor de Supervisor.
        
        Args:
            nombre: Nombre del supervisor
            apellido: Apellido del supervisor
            username: Nombre de usuario
            password: Contraseña
            email: Correo electrónico
            area: Área de supervisión ('Producción', 'Calidad', 'Logística')
        """
        super().__init__(nombre, apellido, username, password, email, "Supervisor")
        
        self.__area = area
        self.__trabajadores_a_cargo = []
        self.__estanterias_supervisadas = []
        self.__reportes_generados = []
    
    def get_area(self) -> str:
        """Retorna el área de supervisión."""
        return self.__area
    
    def get_trabajadores_a_cargo(self) -> list:
        """Retorna la lista de trabajadores a cargo."""
        return self.__trabajadores_a_cargo.copy()
    
    def get_estanterias_supervisadas(self) -> list:
        """Retorna las estanterías supervisadas."""
        return self.__estanterias_supervisadas.copy()
    
    def get_reportes_generados(self) -> list:
        """Retorna los reportes generados."""
        return self.__reportes_generados.copy()
    
    def agregar_trabajador_a_cargo(self, trabajador) -> None:
        """
        Agrega un trabajador a la lista de supervisados.
        
        Args:
            trabajador: Instancia de Trabajador
        """
        if trabajador not in self.__trabajadores_a_cargo:
            self.__trabajadores_a_cargo.append(trabajador)
            print(f"✓ {trabajador.get_nombre_completo()} agregado a cargo de {self.get_nombre_completo()}")
        else:
            print(f" {trabajador.get_nombre_completo()} ya está a cargo de este supervisor")
    
    def asignar_tarea(self, trabajador, tarea: str) -> bool:
        """
        Asigna una tarea a un trabajador específico.
        
        Args:
            trabajador: Instancia de Trabajador
            tarea: Descripción de la tarea
            
        Returns:
            True si se asignó exitosamente, False en caso contrario
        """
        if trabajador in self.__trabajadores_a_cargo:
            trabajador.asignar_tarea(tarea)
            
            registro = {
                "fecha": datetime.now(),
                "supervisor": self.get_nombre_completo(),
                "trabajador": trabajador.get_nombre_completo(),
                "tarea": tarea
            }
            self.__reportes_generados.append(registro)
            return True
        else:
            print(f"✗ {trabajador.get_nombre_completo()} no está a cargo de {self.get_nombre_completo()}")
            return False
    
    def supervisar_estanteria(self, estanteria) -> None:
        """
        Agrega una estantería a la lista de supervisadas.
        
        Args:
            estanteria: Instancia de Estanteria
        """
        if estanteria not in self.__estanterias_supervisadas:
            self.__estanterias_supervisadas.append(estanteria)
            print(f"✓ Estantería {estanteria.get_codigo()} bajo supervisión de {self.get_nombre_completo()}")
        else:
            print(f" Estantería ya está siendo supervisada")
    
    def evaluar_rendimiento_trabajadores(self) -> dict:
        """
        Evalúa el rendimiento de todos los trabajadores a cargo.
        
        Returns:
            Diccionario con evaluación de rendimiento
        """
        evaluacion = {
            "supervisor": self.get_nombre_completo(),
            "fecha": datetime.now(),
            "total_trabajadores": len(self.__trabajadores_a_cargo),
            "trabajadores_evaluados": []
        }
        
        for trabajador in self.__trabajadores_a_cargo:
            datos_trabajador = {
                "nombre": trabajador.get_nombre_completo(),
                "eficiencia": trabajador.calcular_eficiencia(),
                "horas_trabajadas": trabajador.get_horas_trabajadas(),
                "tareas_pendientes": len(trabajador.obtener_tareas_pendientes()),
                "tareas_completadas": len(trabajador.obtener_tareas_completadas())
            }
            evaluacion["trabajadores_evaluados"].append(datos_trabajador)
        
        return evaluacion
    
    def generar_reporte_supervision(self) -> str:
        """
        Genera un reporte completo de supervisión.
        
        Returns:
            String con el reporte de supervisión
        """
        evaluacion = self.evaluar_rendimiento_trabajadores()
        
        reporte = f"""
========================================
REPORTE DE SUPERVISIÓN
========================================
Supervisor: {self.get_nombre_completo()}
Área: {self.__area}
Trabajadores a cargo: {len(self.__trabajadores_a_cargo)}
Estanterías supervisadas: {len(self.__estanterias_supervisadas)}
Reportes generados: {len(self.__reportes_generados)}
========================================
RESUMEN DE RENDIMIENTO:
"""
        for i, trab in enumerate(evaluacion["trabajadores_evaluados"], 1):
            reporte += f"\n{i}. {trab['nombre']}:"
            reporte += f"\n   - Eficiencia: {trab['eficiencia']:.1f}%"
            reporte += f"\n   - Horas: {trab['horas_trabajadas']:.1f}h"
            reporte += f"\n   - Tareas: {trab['tareas_completadas']} completadas, {trab['tareas_pendientes']} pendientes"
        
        if len(evaluacion["trabajadores_evaluados"]) == 0:
            reporte += "\n  No hay trabajadores a cargo"
        
        reporte += "\n========================================"
        return reporte
    
    
    def generar_reporte(self) -> str:
        """
        Genera un reporte de supervisión.
        Implementación del método abstracto de Usuario.
        ESTE MÉTODO TIENE INFORMACIÓN DE SUPERVISIÓN (Polimorfismo)
        
        Returns:
            String con el reporte del supervisor
        """
        evaluacion = self.evaluar_rendimiento_trabajadores()
        eficiencia_promedio = 0
        
        if evaluacion["trabajadores_evaluados"]:
            eficiencia_promedio = sum(t["eficiencia"] for t in evaluacion["trabajadores_evaluados"]) / len(evaluacion["trabajadores_evaluados"])
        
        reporte = f"""
========================================
REPORTE DE SUPERVISIÓN
========================================
Supervisor: {self.get_nombre_completo()}
Username: {self.get_username()}
Área: {self.__area}
Trabajadores a cargo: {len(self.__trabajadores_a_cargo)}
Estanterías supervisadas: {len(self.__estanterias_supervisadas)}
Eficiencia promedio: {eficiencia_promedio:.1f}%
Reportes generados: {len(self.__reportes_generados)}
========================================
Últimas asignaciones:
"""
        ultimas = self.__reportes_generados[-3:] if len(self.__reportes_generados) > 0 else []
        for asig in ultimas:
            reporte += f"  - {asig['trabajador']}: {asig['tarea'][:30]}...\n"
        
        if len(ultimas) == 0:
            reporte += "  No hay asignaciones recientes\n"
        
        reporte += "========================================"
        return reporte
    
    def obtener_permisos(self) -> list:
        """
        Retorna los permisos del supervisor.
        Implementación del método abstracto de Usuario.
        
        Returns:
            Lista con permisos de supervisión
        """
        return [
            "ver_estanterias",
            "registrar_observaciones",
            "completar_tareas",
            "ver_publicaciones",
            "asignar_tareas",
            "supervisar_trabajadores",
            "aprobar_reportes",
            "revisar_estanterias",
            "generar_reportes_supervision"
        ]
    
    def __str__(self) -> str:
        """Representación en string del supervisor."""
        return f"Supervisor({self.get_nombre_completo()}, area={self.__area}, trabajadores={len(self.__trabajadores_a_cargo)})"
