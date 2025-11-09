"""
Clase RegistroTiempo - Representa un registro de entrada/salida
Sistema de Gestión de Producción de Orellanas

Fecha: Noviembre 2025
"""

from datetime import datetime


class RegistroTiempo:
    """
    Clase que representa un registro de tiempo de trabajo.
    Registra la entrada y salida de un trabajador.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Agregación: Tiene una relación con Trabajador
    """
    
    _contador_id = 0
    
    def __init__(self, trabajador):
        """
        Constructor de RegistroTiempo.
        
        Args:
            trabajador: Instancia de Trabajador
        """
        RegistroTiempo._contador_id += 1
        self.__id = RegistroTiempo._contador_id
        self.__trabajador = trabajador  
        self.__fecha_registro = datetime.now().date()
        self.__hora_entrada = None
        self.__hora_salida = None
        self.__horas_trabajadas = 0.0
        self.__completo = False
    
    def get_id(self) -> int:
        """Retorna el ID del registro."""
        return self.__id
    
    def get_trabajador(self):
        """Retorna el trabajador asociado al registro."""
        return self.__trabajador
    
    def get_fecha_registro(self):
        """Retorna la fecha del registro."""
        return self.__fecha_registro
    
    def get_hora_entrada(self):
        """Retorna la hora de entrada."""
        return self.__hora_entrada
    
    def get_hora_salida(self):
        """Retorna la hora de salida."""
        return self.__hora_salida
    
    def get_horas_trabajadas(self) -> float:
        """Retorna las horas trabajadas."""
        return self.__horas_trabajadas
    
    def es_completo(self) -> bool:
        """Indica si el registro está completo (tiene entrada y salida)."""
        return self.__completo
    
    def registrar_entrada(self) -> None:
        """Registra la hora de entrada del trabajador."""
        if self.__hora_entrada is None:
            self.__hora_entrada = datetime.now()
            print(f"Entrada registrada para {self.__trabajador.get_nombre_completo()}")
            print(f" Fecha: {self.__fecha_registro}")
            print(f" Hora: {self.__hora_entrada.strftime('%H:%M:%S')}")
        else:
            print(f" Ya existe una entrada registrada para hoy")
    
    def registrar_salida(self) -> None:
        """Registra la hora de salida del trabajador y calcula las horas."""
        if self.__hora_entrada is None:
            print(f"✗ Error: No se ha registrado entrada")
            return
        
        if self.__hora_salida is None:
            self.__hora_salida = datetime.now()
            self.__horas_trabajadas = self.calcular_horas()
            self.__completo = True
            
            print(f"Salida registrada para {self.__trabajador.get_nombre_completo()}")
            print(f"  Hora: {self.__hora_salida.strftime('%H:%M:%S')}")
            print(f"  Horas trabajadas: {self.__horas_trabajadas:.2f}h")
            
            self.__trabajador.agregar_horas(self.__horas_trabajadas)
        else:
            print(f" Ya existe una salida registrada para hoy")
    
    def calcular_horas(self) -> float:
        """
        Calcula las horas trabajadas entre entrada y salida.
        
        Returns:
            Horas trabajadas en formato decimal
        """
        if self.__hora_entrada and self.__hora_salida:
            diferencia = self.__hora_salida - self.__hora_entrada
            horas = diferencia.total_seconds() / 3600
            return round(horas, 2)
        return 0.0
    
    def obtener_duracion_formateada(self) -> str:
        """
        Obtiene la duración en formato legible (Xh Ym).
        
        Returns:
            String con la duración formateada
        """
        if self.__horas_trabajadas > 0:
            horas = int(self.__horas_trabajadas)
            minutos = int((self.__horas_trabajadas - horas) * 60)
            return f"{horas}h {minutos}m"
        return "0h 0m"
    
    def es_jornada_completa(self, horas_esperadas: float = 8.0) -> bool:
        """
        Verifica si se completó una jornada completa.
        
        Args:
            horas_esperadas: Horas esperadas de trabajo
            
        Returns:
            True si se trabajaron las horas esperadas o más
        """
        return self.__horas_trabajadas >= horas_esperadas
    
    def detectar_horas_extra(self, jornada_normal: float = 8.0) -> float:
        """
        Calcula las horas extra trabajadas.
        
        Args:
            jornada_normal: Duración de la jornada normal
            
        Returns:
            Horas extra trabajadas, 0 si no hay
        """
        if self.__horas_trabajadas > jornada_normal:
            return round(self.__horas_trabajadas - jornada_normal, 2)
        return 0.0
    
    def generar_resumen(self) -> str:
        """
        Genera un resumen del registro de tiempo.
        
        Returns:
            String con el resumen del registro
        """
        estado = " COMPLETO" if self.__completo else " INCOMPLETO"
        
        entrada_str = self.__hora_entrada.strftime('%H:%M:%S') if self.__hora_entrada else "No registrada"
        salida_str = self.__hora_salida.strftime('%H:%M:%S') if self.__hora_salida else "No registrada"
        
        horas_extra = self.detectar_horas_extra()
        extra_str = f"\n  ⏰ Horas extra: {horas_extra:.2f}h" if horas_extra > 0 else ""
        
        resumen = f"""

    REGISTRO DE TIEMPO #{self.__id} - {estado}

   Trabajador: {self.__trabajador.get_nombre_completo()}
   Fecha: {self.__fecha_registro.strftime('%d/%m/%Y')}
   Entrada: {entrada_str}
   Salida: {salida_str}
   Duración: {self.obtener_duracion_formateada()}{extra_str}

"""
        return resumen
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas del registro.
        
        Returns:
            Diccionario con estadísticas del registro
        """
        return {
            "id": self.__id,
            "trabajador": self.__trabajador.get_nombre_completo(),
            "fecha": self.__fecha_registro.strftime('%d/%m/%Y'),
            "hora_entrada": self.__hora_entrada.strftime('%H:%M:%S') if self.__hora_entrada else None,
            "hora_salida": self.__hora_salida.strftime('%H:%M:%S') if self.__hora_salida else None,
            "horas_trabajadas": self.__horas_trabajadas,
            "duracion_formateada": self.obtener_duracion_formateada(),
            "jornada_completa": self.es_jornada_completa(),
            "horas_extra": self.detectar_horas_extra(),
            "completo": self.__completo
        }
    
    def __str__(self) -> str:
        """Representación en string del registro."""
        estado = "Completo" if self.__completo else "Incompleto"
        return f"RegistroTiempo #{self.__id} - {self.__trabajador.get_nombre_completo()} [{estado}]"
    
    def __repr__(self) -> str:
        """Representación técnica del registro."""
        return f"RegistroTiempo(id={self.__id}, trabajador={self.__trabajador.get_username()}, fecha={self.__fecha_registro})"
