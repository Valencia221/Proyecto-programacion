"""
Clase Piso - Representa un piso de estantería
Sistema de Gestión de Producción de Orellanas

Autor: [Tu nombre]
Fecha: Noviembre 2024
"""

from clases.tubular import Tubular


class Piso:
    """
    Clase que representa un piso de una estantería.
    Cada piso contiene 80 tubulares de producción.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Composición: Contiene objetos Tubular
    """
    

    TUBULARES_POR_PISO = 80
    
    def __init__(self, numero: int):
        """
        Constructor de Piso.
        
        Args:
            numero: Número del piso (1-4)
        """
        self.__numero = numero
        self.__tubulares = [Tubular(i + 1) for i in range(self.TUBULARES_POR_PISO)]
        self.__estado_general = "vacío"
    
    def get_numero(self) -> int:
        """Retorna el número del piso."""
        return self.__numero
    
    def get_tubulares(self) -> list:
        """Retorna la lista de tubulares (copia)."""
        return self.__tubulares.copy()
    
    def get_estado_general(self) -> str:
        """Retorna el estado general del piso."""
        return self.__estado_general
    
    def get_tubular_por_numero(self, numero: int):
        """
        Obtiene un tubular por su número.
        
        Args:
            numero: Número del tubular (1-80)
            
        Returns:
            Instancia de Tubular o None si no existe
        """
        if 1 <= numero <= self.TUBULARES_POR_PISO:
            return self.__tubulares[numero - 1]
        return None
    
    def contar_tubulares_por_estado(self) -> dict:
        """
        Cuenta los tubulares por estado.
        
        Returns:
            Diccionario con conteo por estado
        """
        conteo = {
            "vacío": 0,
            "inoculado": 0,
            "en_desarrollo": 0,
            "producción": 0,
            "cosechado": 0,
            "defectuoso": 0
        }
        
        for tubular in self.__tubulares:
            estado = tubular.get_estado()
            if tubular.es_defectuoso():
                conteo["defectuoso"] += 1
            elif estado in conteo:
                conteo[estado] += 1
        
        return conteo
    
    def contar_tubulares_defectuosos(self) -> int:
        """
        Cuenta los tubulares defectuosos en el piso.
        
        Returns:
            Número de tubulares defectuosos
        """
        return sum(1 for tubular in self.__tubulares if tubular.es_defectuoso())
    
    def inocular_piso(self) -> None:
        """
        Inocula todos los tubulares vacíos del piso.
        """
        inoculados = 0
        for tubular in self.__tubulares:
            if tubular.get_estado() == "vacío":
                tubular.inocular()
                inoculados += 1
        
        if inoculados > 0:
            print(f"✓ Piso {self.__numero}: {inoculados} tubulares inoculados")
            self.__actualizar_estado_general()
        else:
            print(f"ℹ️ Piso {self.__numero}: No hay tubulares vacíos para inocular")
    
    def marcar_tubular_defectuoso(self, numero_tubular: int, observacion: str = "") -> bool:
        """
        Marca un tubular específico como defectuoso.
        
        Args:
            numero_tubular: Número del tubular (1-80)
            observacion: Observación opcional
            
        Returns:
            True si se marcó exitosamente, False en caso contrario
        """
        tubular = self.get_tubular_por_numero(numero_tubular)
        if tubular:
            if not tubular.es_defectuoso():
                tubular.marcar_defectuoso()
                if observacion:
                    tubular.agregar_observacion(observacion)
                self.__actualizar_estado_general()
                return True
            else:
                print(f"ℹ️ Tubular {numero_tubular} ya estaba defectuoso")
        else:
            print(f"✗ Tubular {numero_tubular} no existe en el piso {self.__numero}")
        return False
    
    def __actualizar_estado_general(self) -> None:
        """Método privado para actualizar el estado general del piso."""
        conteo = self.contar_tubulares_por_estado()
        
        if conteo["defectuoso"] > 10:
            self.__estado_general = "crítico"
        elif conteo["producción"] > 30:
            self.__estado_general = "óptimo"
        elif conteo["en_desarrollo"] > 40:
            self.__estado_general = "en desarrollo"
        elif conteo["vacío"] == self.TUBULARES_POR_PISO:
            self.__estado_general = "vacío"
        else:
            self.__estado_general = "mixto"
    
    def calcular_porcentaje_ocupacion(self) -> float:
        """
        Calcula el porcentaje de ocupación del piso.
        
        Returns:
            Porcentaje de ocupación (0-100)
        """
        conteo = self.contar_tubulares_por_estado()
        ocupados = sum(conteo[estado] for estado in ["inoculado", "en_desarrollo", "producción", "cosechado", "defectuoso"])
        return (ocupados / self.TUBULARES_POR_PISO) * 100
    
    def generar_reporte_piso(self) -> str:
        """
        Genera un reporte detallado del piso.
        
        Returns:
            String con el reporte del piso
        """
        conteo = self.contar_tubulares_por_estado()
        porcentaje_ocupacion = self.calcular_porcentaje_ocupacion()
        defectuosos = self.contar_tubulares_defectuosos()
        
        reporte = f"""
========================================
REPORTE PISO {self.__numero}
========================================
Estado general: {self.__estado_general}
Ocupación: {porcentaje_ocupacion:.1f}%
Tubulares totales: {self.TUBULARES_POR_PISO}
Tubulares defectuosos: {defectuosos}
========================================
DISTRIBUCIÓN POR ESTADO:
  - Vacíos: {conteo['vacío']}
  - Inoculados: {conteo['inoculado']}
  - En desarrollo: {conteo['en_desarrollo']}
  - En producción: {conteo['producción']}
  - Cosechados: {conteo['cosechado']}
  - Defectuosos: {conteo['defectuoso']}
========================================"""
        return reporte
    
    def obtener_estadisticas(self) -> dict:
        """
        Obtiene estadísticas del piso.
        
        Returns:
            Diccionario con estadísticas
        """
        conteo = self.contar_tubulares_por_estado()
        
        return {
            "numero_piso": self.__numero,
            "estado_general": self.__estado_general,
            "tubulares_totales": self.TUBULARES_POR_PISO,
            "porcentaje_ocupacion": self.calcular_porcentaje_ocupacion(),
            "distribucion_estados": conteo,
            "tubulares_defectuosos": self.contar_tubulares_defectuosos()
        }
    
    def __str__(self) -> str:
        """Representación en string del piso."""
        defectuosos = self.contar_tubulares_defectuosos()
        return f"Piso {self.__numero} [{self.__estado_general}] - Defectuosos: {defectuosos}"
    
    def __repr__(self) -> str:
        """Representación técnica del piso."""
        return f"Piso(numero={self.__numero}, estado='{self.__estado_general}')"
