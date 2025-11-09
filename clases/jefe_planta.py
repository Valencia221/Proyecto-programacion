"""
Clase JefePlanta - Hereda de Usuario
Sistema de Gestión de Producción de Orellanas

Autor: [Juan David Valencia Vera]
Fecha: Noviembre 2025
"""

from clases.usuario import Usuario


class JefePlanta(Usuario):
    """
    Clase que representa al jefe de planta.
    Hereda de Usuario e implementa los métodos abstractos.
    
    Demuestra:
    - Herencia: extends Usuario
    - Polimorfismo: Implementa generarReporte() con información gerencial
    - Encapsulación: Atributos privados propios
    """
    
    def __init__(self, nombre: str, apellido: str, username: str, 
                 password: str, email: str):
        """
        Constructor de JefePlanta.
        
        Args:
            nombre: Nombre del jefe de planta
            apellido: Apellido del jefe de planta
            username: Nombre de usuario
            password: Contraseña
            email: Correo electrónico
        """
        super().__init__(nombre, apellido, username, password, email, "Jefe de Planta")
        
        self.__area_responsabilidad = "Toda la planta"
        self.__metas_produccion = 0.0
        self.__publicaciones_creadas = []
    
    def get_area_responsabilidad(self) -> str:
        """Retorna el área de responsabilidad."""
        return self.__area_responsabilidad
    
    def get_metas_produccion(self) -> float:
        """Retorna las metas de producción establecidas."""
        return self.__metas_produccion
    
    def get_publicaciones(self) -> list:
        """Retorna la lista de publicaciones creadas."""
        return self.__publicaciones_creadas.copy()
    
    def establecer_metas_produccion(self, meta: float) -> None:
        """
        Establece las metas de producción.
        
        Args:
            meta: Meta de producción en kilogramos
        """
        if meta > 0:
            self.__metas_produccion = meta
            print(f"Jefe de Planta {self.get_nombre_completo()} estableció meta de {meta}kg")
        else:
            raise ValueError("La meta debe ser mayor a 0")
    
    def crear_publicacion(self, titulo: str, contenido: str):
        """
        Crea una nueva publicación en el mural.
        
        Args:
            titulo: Título de la publicación
            contenido: Contenido de la publicación
            
        Returns:
            Diccionario con la publicación creada
        """
        from datetime import datetime
        
        publicacion = {
            "id": len(self.__publicaciones_creadas) + 1,
            "titulo": titulo,
            "contenido": contenido,
            "autor": self.get_nombre_completo(),
            "fecha": datetime.now()
        }
        
        self.__publicaciones_creadas.append(publicacion)
        print(f"Publicación creada: '{titulo}' por {self.get_nombre_completo()}")
        return publicacion
    
    def editar_publicacion(self, id_publicacion: int, nuevo_contenido: str) -> bool:
        """
        Edita una publicación existente.
        
        Args:
            id_publicacion: ID de la publicación a editar
            nuevo_contenido: Nuevo contenido de la publicación
            
        Returns:
            True si se editó exitosamente, False en caso contrario
        """
        for pub in self.__publicaciones_creadas:
            if pub["id"] == id_publicacion:
                pub["contenido"] = nuevo_contenido
                print(f"Publicación {id_publicacion} editada")
                return True
        return False
    
    def eliminar_publicacion(self, id_publicacion: int) -> bool:
        """
        Elimina una publicación.
        
        Args:
            id_publicacion: ID de la publicación a eliminar
            
        Returns:
            True si se eliminó exitosamente, False en caso contrario
        """
        for i, pub in enumerate(self.__publicaciones_creadas):
            if pub["id"] == id_publicacion:
                self.__publicaciones_creadas.pop(i)
                print(f"Publicación {id_publicacion} eliminada")
                return True
        return False
    
    def generar_reporte_general(self) -> str:
        """
        Genera un reporte general de toda la planta.
        
        Returns:
            String con el reporte general
        """
        return f"""
========================================
REPORTE GENERAL DE PLANTA
========================================
Jefe de Planta: {self.get_nombre_completo()}
Meta de Producción: {self.__metas_produccion}kg
Publicaciones realizadas: {len(self.__publicaciones_creadas)}
========================================
"""
    
    def evaluar_cumplimiento_metas(self, produccion_actual: float) -> dict:
        """
        Evalúa el cumplimiento de las metas de producción.
        
        Args:
            produccion_actual: Producción actual en kilogramos
            
        Returns:
            Diccionario con el análisis del cumplimiento
        """
        if self.__metas_produccion > 0:
            porcentaje = (produccion_actual / self.__metas_produccion) * 100
            cumplido = porcentaje >= 100
            
            return {
                "meta": self.__metas_produccion,
                "actual": produccion_actual,
                "porcentaje": porcentaje,
                "cumplido": cumplido,
                "diferencia": produccion_actual - self.__metas_produccion
            }
        return {"error": "No se han establecido metas"}
    
    # Implementación de métodos abstractos (POLIMORFISMO)
    
    def generar_reporte(self) -> str:
        """
        Genera un reporte ejecutivo para el jefe de planta.
        Implementación del método abstracto de Usuario.
        ESTE MÉTODO TIENE INFORMACIÓN GERENCIAL (Polimorfismo)
        
        Returns:
            String con el reporte del jefe de planta
        """
        reporte = f"""
========================================
REPORTE EJECUTIVO - JEFE DE PLANTA
========================================
Jefe de Planta: {self.get_nombre_completo()}
Username: {self.get_username()}
Área de Responsabilidad: {self.__area_responsabilidad}
Meta de Producción: {self.__metas_produccion}kg
Publicaciones Realizadas: {len(self.__publicaciones_creadas)}
========================================
Últimas Publicaciones:
"""
        # Mostrar las últimas 3 publicaciones
        ultimas = self.__publicaciones_creadas[-3:] if len(self.__publicaciones_creadas) > 0 else []
        for pub in ultimas:
            reporte += f"  - {pub['titulo']} ({pub['fecha'].strftime('%d/%m/%Y')})\n"
        
        if len(ultimas) == 0:
            reporte += "  No hay publicaciones aún\n"
        
        reporte += "========================================"
        return reporte
    
    def obtener_permisos(self) -> list:
        """
        Retorna los permisos del jefe de planta.
        Implementación del método abstracto de Usuario.
        
        Returns:
            Lista con TODOS los permisos del sistema
        """
        return [
            "ver_estanterias",
            "registrar_observaciones",
            "completar_tareas",
            "ver_publicaciones",
            "crear_publicaciones",
            "editar_publicaciones",
            "eliminar_publicaciones",
            "asignar_tareas",
            "supervisar_trabajadores",
            "aprobar_reportes",
            "revisar_estanterias",
            "establecer_metas",
            "generar_reportes_generales",
            "ver_todos_reportes",
            "administrar_usuarios"
        ]
    
    def __str__(self) -> str:
        """Representación en string del jefe de planta."""
        return f"JefePlanta({self.get_nombre_completo()}, meta={self.__metas_produccion}kg)"
