"""
Clase Tubular - Representa un tubular de hongos orellana
Sistema de Gestión de Producción de Orellanas

Autor: [Tu nombre]
Fecha: Noviembre 2024
"""

from datetime import datetime


class Tubular:
    """
    Clase que representa un tubular de producción de hongos.
    
    Demuestra:
    - Encapsulación: Todos los atributos son privados
    - Abstracción: Representa solo lo importante de un tubular
    """
    
    _contador_id = 0
    
    def __init__(self, numero: int):
        """
        Constructor de Tubular.
        
        Args:
            numero: Número identificador del tubular en el piso (1-80)
        """
        Tubular._contador_id += 1
        self.__id = Tubular._contador_id
        self.__numero = numero
        self.__estado = "vacío"  
        self.__fecha_inoculacion = None
        self.__observaciones = []
        self.__defectuoso = False
    

    def get_id(self) -> int:
        """Retorna el ID único del tubular."""
        return self.__id
    
    def get_numero(self) -> int:
        """Retorna el número del tubular."""
        return self.__numero
    
    def get_estado(self) -> str:
        """Retorna el estado actual del tubular."""
        return self.__estado
    
    def get_fecha_inoculacion(self):
        """Retorna la fecha de inoculación."""
        return self.__fecha_inoculacion
    
    def get_observaciones(self) -> list:
        """Retorna la lista de observaciones."""
        return self.__observaciones.copy()
    
    def es_defectuoso(self) -> bool:
        """Indica si el tubular está defectuoso."""
        return self.__defectuoso
    

    def set_estado(self, nuevo_estado: str) -> None:
        """
        Cambia el estado del tubular.
        
        Args:
            nuevo_estado: Nuevo estado del tubular
        """
        estados_validos = ["vacío", "inoculado", "en_desarrollo", "producción", "cosechado"]
        if nuevo_estado.lower() in estados_validos:
            self.__estado = nuevo_estado.lower()
            print(f"Tubular {self.__numero}: Estado cambiado a '{nuevo_estado}'")
        else:
            raise ValueError(f"Estado inválido. Debe ser: {', '.join(estados_validos)}")
    
    def marcar_defectuoso(self) -> None:
        """Marca el tubular como defectuoso."""
        self.__defectuoso = True
        self.__estado = "defectuoso"
        print(f"⚠️ Tubular {self.__numero} marcado como defectuoso")
    
    def agregar_observacion(self, observacion: str) -> None:
        """
        Agrega una observación al tubular.
        
        Args:
            observacion: Texto de la observación
        """
        if observacion and len(observacion) > 0:
            obs = {
                "fecha": datetime.now(),
                "texto": observacion
            }
            self.__observaciones.append(obs)
            print(f"Observación agregada a tubular {self.__numero}")
    
    def inocular(self) -> None:
        """Registra la inoculación del tubular."""
        if self.__estado == "vacío":
            self.__fecha_inoculacion = datetime.now()
            self.__estado = "inoculado"
            print(f"✓ Tubular {self.__numero} inoculado exitosamente")
        else:
            print(f"✗ Error: Tubular {self.__numero} no está vacío")
    
    def calcular_tiempo_desarrollo(self) -> float:
        """
        Calcula el tiempo de desarrollo en días.
        
        Returns:
            Días transcurridos desde la inoculación, 0 si no ha sido inoculado
        """
        if self.__fecha_inoculacion:
            diferencia = datetime.now() - self.__fecha_inoculacion
            return diferencia.days + (diferencia.seconds / 86400)
        return 0.0
    
    def __str__(self) -> str:
        """Representación en string del tubular."""
        defectuoso_str = " DEFECTUOSO" if self.__defectuoso else ""
        return f"Tubular #{self.__numero} [{self.__estado}]{defectuoso_str}"
    
    def __repr__(self) -> str:
        """Representación técnica del tubular."""
        return f"Tubular(id={self.__id}, num={self.__numero}, estado='{self.__estado}')"
