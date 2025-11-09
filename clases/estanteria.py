"""
Clase Estanteria - Representa una estantería de producción
Sistema de Gestión de Producción de Orellanas

Autor: [Tu nombre]
Fecha: Noviembre 2024
"""

from clases.piso import Piso
from datetime import datetime


class Estanteria:
    """
    Clase que representa una estantería completa de producción.
    Cada estantería contiene 4 pisos con 80 tubulares cada uno.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Composición: Contiene objetos Piso
    """
    
   
    NUMERO_PISOS = 4
    TUBULARES_POR_PISO = 80
    TUBULARES_TOTALES = NUMERO_PISOS * TUBULARES_POR_PISO
    
    def __init__(self, codigo: str):
        """
        Constructor de Estanteria.
        
        Args:
            codigo: Código único de la estantería (ej: "0001")
        """
        self.__codigo = codigo
       
        self.__pisos = [Piso(i + 1) for i in range(self.NUMERO_PISOS)]
        self.__fase = "preparación"  
        self.__fecha_inicio = None
        self.__fecha_ultima_revision = None
        self.__ubicacion = "Almacén principal"
        self.__activa = False
    

    def get_codigo(self) -> str:
        """Retorna el código de la estantería."""
        return self.__codigo
    
    def get_pisos(self) -> list:
        """Retorna la lista de pisos (copia)."""
        return self.__pisos.copy()
    
    def get_fase(self) -> str:
        """Retorna la fase actual de la estantería."""
        return self.__fase
    
    def get_fecha_inicio(self):
        """Retorna la fecha de inicio de producción."""
        return self.__fecha_inicio
    
    def get_fecha_ultima_revision(self):
        """Retorna la fecha de la última revisión."""
        return self.__fecha_ultima_revision
    
    def get_ubicacion(self) -> str:
        """Retorna la ubicación de la estantería."""
        return self.__ubicacion
    
    def esta_activa(self) -> bool:
        """Indica si la estantería está activa."""
        return self.__activa
    
    def get_piso(self, numero: int):
        """
        Obtiene un piso por su número.
        
        Args:
            numero: Número del piso (1-4)
            
        Returns:
            Instancia de Piso o None si no existe
        """
        if 1 <= numero <= self.NUMERO_PISOS:
            return self.__pisos[numero - 1]
        return None
    
   
    def set_ubicacion(self, nueva_ubicacion: str) -> None:
        """
        Establece una nueva ubicación para la estantería.
        
        Args:
            nueva_ubicacion: Nueva ubicación
        """
        self.__ubicacion = nueva_ubicacion
        print(f"✓ Estantería {self.__codigo} movida a: {nueva_ubicacion}")
    
 
    def iniciar_produccion(self) -> None:
        """Inicia la producción en la estantería."""
        if not self.__activa:
            self.__activa = True
            self.__fecha_inicio = datetime.now()
            self.__fase = "germinación"
            print(f"✓ Estantería {self.__codigo} iniciada en fase: {self.__fase}")
        else:
            print(f"ℹ️ Estantería {self.__codigo} ya está activa")
    
    def cambiar_fase(self, nueva_fase: str) -> None:
        """
        Cambia la fase de producción de la estantería.
        
        Args:
            nueva_fase: Nueva fase ('germinación', 'fructificación', 'cosecha')
        """
        fases_validas = ["preparación", "germinación", "fructificación", "cosecha"]
        
        if nueva_fase in fases_validas:
            self.__fase = nueva_fase
            print(f"✓ Estantería {self.__codigo} cambió a fase: {nueva_fase}")
        else:
            raise ValueError(f"Fase inválida. Debe ser: {', '.join(fases_validas)}")
    
    def registrar_revision(self) -> None:
        """Registra una revisión de la estantería."""
        self.__fecha_ultima_revision = datetime.now()
        print(f"✓ Revisión registrada para estantería {self.__codigo}")
    
    def contar_tubulares_total(self) -> int:
        """
        Cuenta el total de tubulares en la estantería.
        
        Returns:
            Número total de tubulares
        """
        return self.TUBULARES_TOTALES
    
    def contar_tubulares_por_estado(self) -> dict:
        """
        Cuenta los tubulares por estado en toda la estantería.
        
        Returns:
            Diccionario con conteo por estado
        """
        conteo_total = {
            "vacío": 0,
            "inoculado": 0,
            "en_desarrollo": 0,
            "producción": 0,
            "cosechado": 0,
            "defectuoso": 0
        }
        
        for piso in self.__pisos:
            conteo_piso = piso.contar_tubulares_por_estado()
            for estado, cantidad in conteo_piso.items():
                conteo_total[estado] += cantidad
        
        return conteo_total
    
    def contar_defectuosos_total(self) -> int:
        """
        Cuenta el total de tubulares defectuosos en la estantería.
        
        Returns:
            Número total de defectuosos
        """
        return sum(piso.contar_tubulares_defectuosos() for piso in self.__pisos)
    
    def calcular_tiempo_produccion(self) -> float:
        """
        Calcula el tiempo de producción en días.
        
        Returns:
            Días de producción, 0 si no ha iniciado
        """
        if self.__fecha_inicio:
            diferencia = datetime.now() - self.__fecha_inicio
            return diferencia.days + (diferencia.seconds / 86400)
        return 0.0
    
    def calcular_eficiencia_total(self) -> float:
        """
        Calcula la eficiencia general de la estantería.
        
        Returns:
            Porcentaje de eficiencia (0-100)
        """
        defectuosos = self.contar_defectuosos_total()
        total_tubulares = self.TUBULARES_TOTALES
        
        if total_tubulares == 0:
            return 100.0
        
        eficiencia = ((total_tubulares - defectuosos) / total_tubulares) * 100
        return round(eficiencia, 2)
    
    def obtener_estado_general(self) -> dict:
        """
        Obtiene el estado general de la estantería.
        
        Returns:
            Diccionario con estado general
        """
        return {
            "codigo": self.__codigo,
            "fase": self.__fase,
            "activa": self.__activa,
            "ubicacion": self.__ubicacion,
            "dias_produccion": int(self.calcular_tiempo_produccion()),
            "tubulares_totales": self.TUBULARES_TOTALES,
            "tubulares_defectuosos": self.contar_defectuosos_total(),
            "eficiencia": self.calcular_eficiencia_total(),
            "en_produccion": sum(1 for piso in self.__pisos if piso.get_estado_general() == "óptimo")
        }
    
    def generar_resumen(self) -> str:
        """
        Genera un resumen completo de la estantería.
        
        Returns:
            String con el resumen de la estantería
        """
        estado = self.obtener_estado_general()
        conteo = self.contar_tubulares_por_estado()
        
        # LÍNEA CORREGIDA - COMPLETA
        fecha_inicio_str = self.__fecha_inicio.strftime('%d/%m/%Y') if self.__fecha_inicio else "No iniciada"
        fecha_revision_str = self.__fecha_ultima_revision.strftime('%d/%m/%Y') if self.__fecha_ultima_revision else "Sin revisiones"
        
        resumen = f"""
╔══════════════════════════════════════════════════════════╗
  🏭 ESTANTERÍA {self.__codigo} - RESUMEN COMPLETO
╠══════════════════════════════════════════════════════════╣
  Estado: {'✅ ACTIVA' if self.__activa else '⏸️ INACTIVA'}
  Fase: {self.__fase.upper()}
  Ubicación: {self.__ubicacion}
  Fecha inicio: {fecha_inicio_str}
  Última revisión: {fecha_revision_str}
  Días en producción: {estado['dias_produccion']}
╠══════════════════════════════════════════════════════════╣
  📊 ESTADÍSTICAS GENERALES:
  • Tubulares totales: {self.TUBULARES_TOTALES}
  • Tubulares defectuosos: {estado['tubulares_defectuosos']}
  • Eficiencia: {estado['eficiencia']}%
╠══════════════════════════════════════════════════════════╣
  📈 DISTRIBUCIÓN POR ESTADO:
  • Vacíos: {conteo['vacío']}
  • Inoculados: {conteo['inoculado']}
  • En desarrollo: {conteo['en_desarrollo']}
  • En producción: {conteo['producción']}
  • Cosechados: {conteo['cosechado']}
  • Defectuosos: {conteo['defectuoso']}
╚══════════════════════════════════════════════════════════╝
"""
        return resumen
    
    def obtener_estadisticas_detalladas(self) -> dict:
        """
        Obtiene estadísticas detalladas de toda la estantería.
        
        Returns:
            Diccionario con estadísticas completas
        """
        estadisticas = {
            "codigo": self.__codigo,
            "fase": self.__fase,
            "activa": self.__activa,
            "ubicacion": self.__ubicacion,
            "fecha_inicio": self.__fecha_inicio.strftime('%d/%m/%Y %H:%M') if self.__fecha_inicio else None,
            "fecha_ultima_revision": self.__fecha_ultima_revision.strftime('%d/%m/%Y %H:%M') if self.__fecha_ultima_revision else None,
            "dias_produccion": self.calcular_tiempo_produccion(),
            "tubulares_totales": self.TUBULARES_TOTALES,
            "eficiencia_general": self.calcular_eficiencia_total(),
            "distribucion_estados": self.contar_tubulares_por_estado(),
            "pisos": []
        }
        
        # Estadísticas por piso
        for i, piso in enumerate(self.__pisos, 1):
            stats_piso = piso.obtener_estadisticas()
            estadisticas["pisos"].append(stats_piso)
        
        return estadisticas
    
    def __str__(self) -> str:
        """Representación en string de la estantería."""
        estado = "Activa" if self.__activa else "Inactiva"
        defectuosos = self.contar_defectuosos_total()
        return f"Estanteria {self.__codigo} [{estado}] - Fase: {self.__fase} - Defectuosos: {defectuosos}"
    
    def __repr__(self) -> str:
        """Representación técnica de la estantería."""
        return f"Estanteria(codigo='{self.__codigo}', fase='{self.__fase}', activa={self.__activa})"
