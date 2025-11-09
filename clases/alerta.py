"""
Clase Alerta - Representa una alerta del sistema
Sistema de Gestión de Producción de Orellanas

Autor: [Tu nombre]
Fecha: Noviembre 2024
"""

from datetime import datetime


class Alerta:
    """
    Clase que representa una alerta del sistema.
    Las alertas notifican problemas o situaciones que requieren atención.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Agregación: Tiene una relación con Estanteria
    """
    
   
    _contador_id = 0
    
    def __init__(self, tipo: str, mensaje: str, estanteria=None):
        """
        Constructor de Alerta.
        
        Args:
            tipo: Tipo de alerta ('defecto', 'tiempo', 'produccion', 'sistema')
            mensaje: Mensaje descriptivo de la alerta
            estanteria: Instancia de Estanteria relacionada (opcional)
        """
        Alerta._contador_id += 1
        self.__id = Alerta._contador_id
        self.__tipo = tipo
        self.__mensaje = mensaje
        self.__nivel = self.__determinar_nivel(tipo)
        self.__fecha_creacion = datetime.now()
        self.__estanteria = estanteria  
        self.__resuelta = False
        self.__fecha_resolucion = None
    
    def __determinar_nivel(self, tipo: str) -> str:
        """
        Método privado para determinar el nivel de la alerta según su tipo.
        
        Args:
            tipo: Tipo de alerta
            
        Returns:
            Nivel de alerta ('info', 'advertencia', 'critico')
        """
        niveles = {
            "defecto": "advertencia",
            "tiempo": "advertencia",
            "produccion": "advertencia",
            "sistema": "critico",
            "mantenimiento": "info"
        }
        return niveles.get(tipo.lower(), "info")
    
    
    def get_id(self) -> int:
        """Retorna el ID de la alerta."""
        return self.__id
    
    def get_tipo(self) -> str:
        """Retorna el tipo de alerta."""
        return self.__tipo
    
    def get_mensaje(self) -> str:
        """Retorna el mensaje de la alerta."""
        return self.__mensaje
    
    def get_nivel(self) -> str:
        """Retorna el nivel de severidad de la alerta."""
        return self.__nivel
    
    def get_fecha_creacion(self) -> datetime:
        """Retorna la fecha de creación de la alerta."""
        return self.__fecha_creacion
    
    def get_estanteria(self):
        """Retorna la estantería asociada (puede ser None)."""
        return self.__estanteria
    
    def esta_resuelta(self) -> bool:
        """Indica si la alerta ha sido resuelta."""
        return self.__resuelta
    
    def get_fecha_resolucion(self):
        """Retorna la fecha de resolución (None si no está resuelta)."""
        return self.__fecha_resolucion
    
 
    def marcar_resuelta(self) -> None:
        """Marca la alerta como resuelta."""
        if not self.__resuelta:
            self.__resuelta = True
            self.__fecha_resolucion = datetime.now()
            print(f"✓ Alerta #{self.__id} marcada como resuelta")
        else:
            print(f"⚠️ Alerta #{self.__id} ya estaba resuelta")
    
    def reabrir(self) -> None:
        """Reabre una alerta previamente resuelta."""
        if self.__resuelta:
            self.__resuelta = False
            self.__fecha_resolucion = None
            print(f"⚠️ Alerta #{self.__id} reabierta")
        else:
            print(f"ℹ️ Alerta #{self.__id} ya estaba abierta")
    
    def es_urgente(self) -> bool:
        """
        Determina si la alerta es urgente.
        
        Returns:
            True si es crítica o lleva más de 24 horas sin resolver
        """
        if self.__nivel == "critico":
            return True
        
        if not self.__resuelta:
            tiempo_abierta = datetime.now() - self.__fecha_creacion
            return tiempo_abierta.total_seconds() > 86400  # 24 horas
        
        return False
    
    def calcular_tiempo_abierta(self) -> float:
        """
        Calcula el tiempo que la alerta ha estado abierta.
        
        Returns:
            Horas que ha estado abierta
        """
        if self.__resuelta:
            diferencia = self.__fecha_resolucion - self.__fecha_creacion
        else:
            diferencia = datetime.now() - self.__fecha_creacion
        
        return round(diferencia.total_seconds() / 3600, 2)
    
    def obtener_tiempo_formateado(self) -> str:
        """
        Obtiene el tiempo de la alerta en formato legible.
        
        Returns:
            String con el tiempo formateado
        """
        horas = self.calcular_tiempo_abierta()
        
        if horas < 1:
            minutos = int(horas * 60)
            return f"{minutos} minutos"
        elif horas < 24:
            return f"{horas:.1f} horas"
        else:
            dias = int(horas / 24)
            horas_resto = int(horas % 24)
            return f"{dias} días, {horas_resto} horas"
    
    def notificar(self) -> None:
        """Simula el envío de una notificación de la alerta."""
        simbolo = self.__obtener_simbolo()
        urgente_str = " ⚠️ URGENTE" if self.es_urgente() else ""
        
        print(f"\n{'='*60}")
        print(f"{simbolo} ALERTA #{self.__id}{urgente_str}")
        print(f"{'='*60}")
        print(f"Tipo: {self.__tipo.upper()}")
        print(f"Nivel: {self.__nivel.upper()}")
        print(f"Mensaje: {self.__mensaje}")
        
        if self.__estanteria:
            print(f"Estantería: {self.__estanteria.get_codigo()}")
        
        print(f"Tiempo abierta: {self.obtener_tiempo_formateado()}")
        print(f"{'='*60}\n")
    
    def __obtener_simbolo(self) -> str:
        """
        Método privado para obtener el símbolo según el nivel.
        
        Returns:
            Emoji representativo del nivel
        """
        simbolos = {
            "info": "ℹ️",
            "advertencia": "⚠️",
            "critico": "🚨"
        }
        return simbolos.get(self.__nivel, "ℹ️")
    
    def generar_resumen(self) -> str:
        """
        Genera un resumen de la alerta.
        
        Returns:
            String con el resumen de la alerta
        """
        simbolo = self.__obtener_simbolo()
        estado = "✓ RESUELTA" if self.__resuelta else "⚠️ ACTIVA"
        urgente = " 🔥 URGENTE" if self.es_urgente() else ""
        
        estanteria_str = ""
        if self.__estanteria:
            estanteria_str = f"\n  📍 Estantería: {self.__estanteria.get_codigo()}"
        
        tiempo_str = self.obtener_tiempo_formateado()
        if self.__resuelta:
            tiempo_label = "Tiempo de resolución"
        else:
            tiempo_label = "Tiempo abierta"
        
        resolucion_str = ""
        if self.__resuelta and self.__fecha_resolucion:
            resolucion_str = f"\n  ✅ Resuelta: {self.__fecha_resolucion.strftime('%d/%m/%Y %H:%M')}"
        
        resumen = f"""
╔══════════════════════════════════════════════════════════╗
  {simbolo} ALERTA #{self.__id} - {estado}{urgente}
╠══════════════════════════════════════════════════════════╣
  Tipo: {self.__tipo.upper()}
  Nivel: {self.__nivel.upper()}
  Creada: {self.__fecha_creacion.strftime('%d/%m/%Y %H:%M')}{estanteria_str}
  {tiempo_label}: {tiempo_str}{resolucion_str}
╠══════════════════════════════════════════════════════════╣
  Mensaje:
  {self.__mensaje}
╚══════════════════════════════════════════════════════════╝
"""
        return resumen
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas de la alerta.
        
        Returns:
            Diccionario con estadísticas
        """
        stats = {
            "id": self.__id,
            "tipo": self.__tipo,
            "nivel": self.__nivel,
            "fecha_creacion": self.__fecha_creacion.strftime('%d/%m/%Y %H:%M'),
            "tiempo_abierta_horas": self.calcular_tiempo_abierta(),
            "tiempo_formateado": self.obtener_tiempo_formateado(),
            "resuelta": self.__resuelta,
            "urgente": self.es_urgente()
        }
        
        if self.__estanteria:
            stats["estanteria"] = self.__estanteria.get_codigo()
        
        if self.__resuelta:
            stats["fecha_resolucion"] = self.__fecha_resolucion.strftime('%d/%m/%Y %H:%M')
        
        return stats
    
    def __str__(self) -> str:
        """Representación en string de la alerta."""
        estado = "Resuelta" if self.__resuelta else "Activa"
        urgente = " URGENTE" if self.es_urgente() else ""
        return f"Alerta #{self.__id} [{self.__tipo}] - {estado}{urgente}"
    
    def __repr__(self) -> str:
        """Representación técnica de la alerta."""
        return f"Alerta(id={self.__id}, tipo='{self.__tipo}', nivel='{self.__nivel}')"
