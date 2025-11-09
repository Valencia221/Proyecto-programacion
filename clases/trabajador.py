"""
Clase Trabajador - Hereda de Usuario
Sistema de Gestión de Producción de Orellanas


Fecha: Noviembre 2025
"""

from clases.usuario import Usuario
from datetime import datetime


class Trabajador(Usuario):
    """
    Clase que representa a un trabajador de la planta.
    Hereda de Usuario e implementa los métodos abstractos.
    
    Demuestra:
    - Herencia: extends Usuario
    - Polimorfismo: Implementa generarReporte() con información operativa
    - Encapsulación: Atributos privados propios
    """
    
    def __init__(self, nombre: str, apellido: str, username: str, 
                 password: str, email: str, turno: str):
        """
        Constructor de Trabajador.
        
        Args:
            nombre: Nombre del trabajador
            apellido: Apellido del trabajador
            username: Nombre de usuario
            password: Contraseña
            email: Correo electrónico
            turno: Turno de trabajo ('mañana', 'tarde', 'noche')
        """
        super().__init__(nombre, apellido, username, password, email, "Trabajador")
        
        self.__turno = turno
        self.__tareas_asignadas = []
        self.__horas_trabajadas = 0.0
        self.__estanterias_asignadas = []
        self.__registros_tiempo = []
    
    def get_turno(self) -> str:
        """Retorna el turno del trabajador."""
        return self.__turno
    
    def get_tareas_asignadas(self) -> list:
        """Retorna la lista de tareas asignadas."""
        return self.__tareas_asignadas.copy()
    
    def get_horas_trabajadas(self) -> float:
        """Retorna las horas trabajadas acumuladas."""
        return self.__horas_trabajadas
    
    def get_estanterias_asignadas(self) -> list:
        """Retorna las estanterías asignadas."""
        return self.__estanterias_asignadas.copy()
    
    def agregar_horas(self, horas: float) -> None:
        """
        Agrega horas trabajadas al acumulador.
        
        Args:
            horas: Horas trabajadas a agregar
        """
        if horas > 0:
            self.__horas_trabajadas += horas
            print(f"✓ {horas}h agregadas a {self.get_nombre_completo()}. Total: {self.__horas_trabajadas}h")
        else:
            print("✗ Las horas deben ser mayores a 0")
    
    def asignar_tarea(self, tarea: str) -> None:
        """
        Asigna una nueva tarea al trabajador.
        
        Args:
            tarea: Descripción de la tarea
        """
        tarea_con_fecha = {
            "descripcion": tarea,
            "fecha_asignacion": datetime.now(),
            "completada": False,
            "fecha_completada": None
        }
        self.__tareas_asignadas.append(tarea_con_fecha)
        print(f"✓ Tarea asignada a {self.get_nombre_completo()}: {tarea}")
    
    def completar_tarea(self, indice: int) -> bool:
        """
        Marca una tarea como completada.
        
        Args:
            indice: Índice de la tarea en la lista
            
        Returns:
            True si se completó exitosamente, False en caso contrario
        """
        if 0 <= indice < len(self.__tareas_asignadas):
            self.__tareas_asignadas[indice]["completada"] = True
            self.__tareas_asignadas[indice]["fecha_completada"] = datetime.now()
            tarea = self.__tareas_asignadas[indice]["descripcion"]
            print(f"✓ Tarea completada por {self.get_nombre_completo()}: {tarea}")
            return True
        print(f"✗ Índice de tarea inválido: {indice}")
        return False
    
    def asignar_estanteria(self, estanteria) -> None:
        """
        Asigna una estantería al trabajador.
        
        Args:
            estanteria: Instancia de Estanteria
        """
        if estanteria not in self.__estanterias_asignadas:
            self.__estanterias_asignadas.append(estanteria)
            print(f"✓ Estantería {estanteria.get_codigo()} asignada a {self.get_nombre_completo()}")
        else:
            print(f"ℹ️ Estantería ya asignada a {self.get_nombre_completo()}")
    
    def obtener_tareas_pendientes(self) -> list:
        """
        Obtiene las tareas pendientes del trabajador.
        
        Returns:
            Lista de tareas pendientes
        """
        return [tarea for tarea in self.__tareas_asignadas if not tarea["completada"]]
    
    def obtener_tareas_completadas(self) -> list:
        """
        Obtiene las tareas completadas del trabajador.
        
        Returns:
            Lista de tareas completadas
        """
        return [tarea for tarea in self.__tareas_asignadas if tarea["completada"]]
    
    def calcular_eficiencia(self) -> float:
        """
        Calcula la eficiencia del trabajador basada en tareas completadas.
        
        Returns:
            Porcentaje de eficiencia (0-100)
        """
        if len(self.__tareas_asignadas) == 0:
            return 100.0  
        
        completadas = len(self.obtener_tareas_completadas())
        total = len(self.__tareas_asignadas)
        return (completadas / total) * 100
    
    def generar_reporte_diario(self) -> str:
        """
        Genera un reporte diario del trabajador.
        
        Returns:
            String con el reporte diario
        """
        tareas_pendientes = self.obtener_tareas_pendientes()
        tareas_completadas = self.obtener_tareas_completadas()
        eficiencia = self.calcular_eficiencia()
        
        reporte = f"""
========================================
REPORTE DIARIO - TRABAJADOR
========================================
Trabajador: {self.get_nombre_completo()}
Turno: {self.__turno}
Horas trabajadas: {self.__horas_trabajadas:.2f}h
Eficiencia: {eficiencia:.1f}%
Estanterías asignadas: {len(self.__estanterias_asignadas)}
========================================
Tareas completadas: {len(tareas_completadas)}
Tareas pendientes: {len(tareas_pendientes)}
========================================"""
        return reporte
    
    
    
    def generar_reporte(self) -> str:
        """
        Genera un reporte operativo del trabajador.
        Implementación del método abstracto de Usuario.
        ESTE MÉTODO TIENE INFORMACIÓN OPERATIVA (Polimorfismo)
        
        Returns:
            String con el reporte del trabajador
        """
        tareas_pendientes = len(self.obtener_tareas_pendientes())
        tareas_completadas = len(self.obtener_tareas_completadas())
        eficiencia = self.calcular_eficiencia()
        
        reporte = f"""
========================================
REPORTE OPERATIVO - TRABAJADOR
========================================
Trabajador: {self.get_nombre_completo()}
Username: {self.get_username()}
Turno: {self.__turno}
Horas trabajadas: {self.__horas_trabajadas:.2f}h
Tareas completadas: {tareas_completadas}
Tareas pendientes: {tareas_pendientes}
Eficiencia: {eficiencia:.1f}%
Estanterías asignadas: {len(self.__estanterias_asignadas)}
========================================"""
        return reporte
    
    def obtener_permisos(self) -> list:
        """
        Retorna los permisos del trabajador.
        Implementación del método abstracto de Usuario.
        
        Returns:
            Lista con permisos básicos del trabajador
        """
        return [
            "ver_estanterias",
            "registrar_observaciones", 
            "completar_tareas",
            "ver_publicaciones",
            "registrar_entrada_salida",
            "reportar_problemas"
        ]
    
    def __str__(self) -> str:
        """Representación en string del trabajador."""
        return f"Trabajador({self.get_nombre_completo()}, turno={self.__turno})"

