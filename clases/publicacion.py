"""
Clase Publicacion - Representa una publicación en el mural
Sistema de Gestión de Producción de Orellanas

Autor: [Juan David Valencia Vera]
Fecha: Noviembre 2024
5
"""

from datetime import datetime


class Publicacion:
    """
    Clase que representa una publicación en el mural de la planta.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Agregación: Tiene una relación con Usuario (autor)
    """
    
    _contador_id = 0
    
    def __init__(self, titulo: str, contenido: str, autor):
        """
        Constructor de Publicacion.
        
        Args:
            titulo: Título de la publicación
            contenido: Contenido/cuerpo de la publicación
            autor: Instancia de Usuario que crea la publicación
        """
        Publicacion._contador_id += 1
        self.__id = Publicacion._contador_id
        self.__titulo = titulo
        self.__contenido = contenido
        self.__autor = autor  
        self.__fecha_publicacion = datetime.now()
        self.__prioridad = "normal"  
        self.__activa = True
    
    def get_id(self) -> int:
        """Retorna el ID de la publicación."""
        return self.__id
    
    def get_titulo(self) -> str:
        """Retorna el título de la publicación."""
        return self.__titulo
    
    def get_contenido(self) -> str:
        """Retorna el contenido de la publicación."""
        return self.__contenido
    
    def get_autor(self):
        """Retorna el autor de la publicación (Usuario)."""
        return self.__autor
    
    def get_fecha_publicacion(self) -> datetime:
        """Retorna la fecha de publicación."""
        return self.__fecha_publicacion
    
    def get_prioridad(self) -> str:
        """Retorna la prioridad de la publicación."""
        return self.__prioridad
    
    def esta_activa(self) -> bool:
        """Indica si la publicación está activa."""
        return self.__activa
    

    def set_titulo(self, nuevo_titulo: str) -> None:
        """
        Establece un nuevo título.
        
        Args:
            nuevo_titulo: Nuevo título de la publicación
        """
        if nuevo_titulo and len(nuevo_titulo) > 0:
            self.__titulo = nuevo_titulo
            print(f"✓ Título actualizado en publicación #{self.__id}")
        else:
            raise ValueError("El título no puede estar vacío")
    
    def set_contenido(self, nuevo_contenido: str) -> None:
        """
        Establece un nuevo contenido.
        
        Args:
            nuevo_contenido: Nuevo contenido de la publicación
        """
        if nuevo_contenido and len(nuevo_contenido) > 0:
            self.__contenido = nuevo_contenido
            print(f"✓ Contenido actualizado en publicación #{self.__id}")
        else:
            raise ValueError("El contenido no puede estar vacío")
    
    def set_prioridad(self, prioridad: str) -> None:
        """
        Establece la prioridad de la publicación.
        
        Args:
            prioridad: Nivel de prioridad ('normal', 'alta', 'urgente')
        """
        prioridades_validas = ["normal", "alta", "urgente"]
        if prioridad.lower() in prioridades_validas:
            self.__prioridad = prioridad.lower()
            print(f"✓ Prioridad de publicación #{self.__id} cambiada a '{prioridad}'")
        else:
            raise ValueError(f"Prioridad inválida. Debe ser: {', '.join(prioridades_validas)}")
    

    def archivar(self) -> None:
        """Archiva (desactiva) la publicación."""
        self.__activa = False
        print(f"📦 Publicación #{self.__id} archivada")
    
    def reactivar(self) -> None:
        """Reactiva una publicación archivada."""
        self.__activa = True
        print(f"✓ Publicación #{self.__id} reactivada")
    
    def es_reciente(self, dias: int = 7) -> bool:
        """
        Verifica si la publicación es reciente.
        
        Args:
            dias: Número de días para considerar como reciente
            
        Returns:
            True si fue publicada hace menos de 'dias' días
        """
        diferencia = datetime.now() - self.__fecha_publicacion
        return diferencia.days < dias
    
    def calcular_antiguedad(self) -> int:
        """
        Calcula la antigüedad de la publicación en días.
        
        Returns:
            Número de días desde la publicación
        """
        diferencia = datetime.now() - self.__fecha_publicacion
        return diferencia.days
    
    def formatear_para_mostrar(self) -> str:
        """
        Formatea la publicación para mostrarla en pantalla.
        
        Returns:
            String con la publicación formateada
        """
        simbolo_prioridad = {
            "normal": "📌",
            "alta": "⚠️",
            "urgente": "🚨"
        }
        simbolo = simbolo_prioridad.get(self.__prioridad, "📌")
        
        estado = "✓ ACTIVA" if self.__activa else "📦 ARCHIVADA"
        
        reciente = "🆕 RECIENTE" if self.es_reciente() else f"({self.calcular_antiguedad()} días)"
        
        publicacion = f"""
╔══════════════════════════════════════════════════════════╗
  {simbolo} PUBLICACIÓN #{self.__id} - {estado}
╠══════════════════════════════════════════════════════════╣
  📋 Título: {self.__titulo}
  👤 Autor: {self.__autor.get_nombre_completo()} ({self.__autor.get_rol()})
  📅 Fecha: {self.__fecha_publicacion.strftime('%d/%m/%Y %H:%M')}
  🕐 {reciente}
  ⚡ Prioridad: {self.__prioridad.upper()}
╠══════════════════════════════════════════════════════════╣
{self.__contenido}
╚══════════════════════════════════════════════════════════╝
"""
        return publicacion
    
    def obtener_resumen(self) -> str:
        """
        Obtiene un resumen corto de la publicación.
        
        Returns:
            String con el resumen (primeras 50 caracteres del contenido)
        """
        contenido_corto = self.__contenido[:50]
        if len(self.__contenido) > 50:
            contenido_corto += "..."
        
        return f"#{self.__id}: {self.__titulo} - {contenido_corto}"
    
    def __str__(self) -> str:
        """Representación en string de la publicación."""
        estado = "ACTIVA" if self.__activa else "ARCHIVADA"
        return f"Publicacion #{self.__id}: '{self.__titulo}' [{estado}]"
    
    def __repr__(self) -> str:
        """Representación técnica de la publicación."""
        return f"Publicacion(id={self.__id}, titulo='{self.__titulo}', autor={self.__autor.get_username()})"
