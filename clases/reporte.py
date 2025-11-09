"""
Clase Reporte - Representa un reporte de producción
Sistema de Gestión de Producción de Orellanas

Fecha: Noviembre 2025
"""

from datetime import datetime


class Reporte:
    """
    Clase que representa un reporte de producción o gestión.
    
    Demuestra:
    - Encapsulación: Atributos privados
    - Agregación: Tiene una relación con Usuario (generador)
    """
    
    _contador_id = 0
    
    def __init__(self, tipo: str, periodo: str, usuario):
        """
        Constructor de Reporte.
        
        Args:
            tipo: Tipo de reporte ('diario', 'semanal', 'mensual', 'produccion', 'calidad')
            periodo: Periodo del reporte (ej: "Noviembre 2024", "Semana 45")
            usuario: Instancia de Usuario que genera el reporte
        """
        Reporte._contador_id += 1
        self.__id = Reporte._contador_id
        self.__tipo = tipo
        self.__fecha_generacion = datetime.now()
        self.__periodo = periodo
        self.__datos = {}  
        self.__generado_por = usuario 
        self.__finalizado = False
    

    def get_id(self) -> int:
        """Retorna el ID del reporte."""
        return self.__id
    
    def get_tipo(self) -> str:
        """Retorna el tipo de reporte."""
        return self.__tipo
    
    def get_fecha_generacion(self) -> datetime:
        """Retorna la fecha de generación del reporte."""
        return self.__fecha_generacion
    
    def get_periodo(self) -> str:
        """Retorna el periodo del reporte."""
        return self.__periodo
    
    def get_datos(self) -> dict:
        """Retorna una copia de los datos del reporte."""
        return self.__datos.copy()
    
    def get_generado_por(self):
        """Retorna el usuario que generó el reporte."""
        return self.__generado_por
    
    def esta_finalizado(self) -> bool:
        """Indica si el reporte está finalizado."""
        return self.__finalizado
    
    # Métodos de negocio
    def agregar_dato(self, clave: str, valor) -> None:
        """
        Agrega un dato al reporte.
        
        Args:
            clave: Clave del dato
            valor: Valor del dato
        """
        if not self.__finalizado:
            self.__datos[clave] = valor
            print(f" Dato '{clave}' agregado al reporte #{self.__id}")
        else:
            print(f" No se puede modificar reporte #{self.__id}: ya está finalizado")
    
    def agregar_datos_multiples(self, datos: dict) -> None:
        """
        Agrega múltiples datos al reporte.
        
        Args:
            datos: Diccionario con los datos a agregar
        """
        if not self.__finalizado:
            self.__datos.update(datos)
            print(f"✓ {len(datos)} datos agregados al reporte #{self.__id}")
        else:
            print(f"✗ No se puede modificar reporte #{self.__id}: ya está finalizado")
    
    def obtener_dato(self, clave: str, default=None):
        """
        Obtiene un dato específico del reporte.
        
        Args:
            clave: Clave del dato a obtener
            default: Valor por defecto si no existe la clave
            
        Returns:
            El valor del dato o default si no existe
        """
        return self.__datos.get(clave, default)
    
    def calcular_produccion_total(self) -> float:
        """
        Calcula la producción total reportada.
        
        Returns:
            Total de kilogramos producidos
        """
       
        total = 0.0
        claves_produccion = ['produccion', 'kg_producidos', 'total_kg', 'cosecha']
        
        for clave in claves_produccion:
            if clave in self.__datos:
                total += float(self.__datos[clave])
        
        return total
    
    def finalizar_reporte(self) -> None:
        """Marca el reporte como finalizado (no se puede editar más)."""
        self.__finalizado = True
        print(f"✓ Reporte #{self.__id} finalizado y cerrado para edición")
    
    def generar_resumen(self) -> str:
        """
        Genera un resumen del reporte.
        
        Returns:
            String con el resumen del reporte
        """
        estado = "✓ FINALIZADO" if self.__finalizado else "⚠️ EN PROGRESO"
        
        resumen = f"""

   REPORTE #{self.__id} - {estado}

  Tipo: {self.__tipo.upper()}
  Periodo: {self.__periodo}
  Generado por: {self.__generado_por.get_nombre_completo()}
  Fecha: {self.__fecha_generacion.strftime('%d/%m/%Y %H:%M')}

  DATOS REGISTRADOS:
"""
        if len(self.__datos) > 0:
            for clave, valor in self.__datos.items():
                resumen += f"  • {clave}: {valor}\n"
        else:
            resumen += "  (Sin datos registrados)\n"
        
        resumen += "╚══════════════════════════════════════════════════════════╝"
        return resumen
    
    def exportar_pdf(self) -> str:
        """
        Simula la exportación del reporte a PDF.
        
        Returns:
            Nombre del archivo PDF generado
        """
        archivo = f"reporte_{self.__id}_{self.__tipo}_{datetime.now().strftime('%Y%m%d')}.pdf"
        print(f"📄 Reporte exportado a: {archivo}")
        return archivo
    
    def exportar_excel(self) -> str:
        """
        Simula la exportación del reporte a Excel.
        
        Returns:
            Nombre del archivo Excel generado
        """
        archivo = f"reporte_{self.__id}_{self.__tipo}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        print(f" Reporte exportado a: {archivo}")
        return archivo
    
    def obtener_estadisticas(self) -> dict:
        """
        Calcula estadísticas básicas del reporte.
        
        Returns:
            Diccionario con estadísticas
        """
        estadisticas = {
            "id": self.__id,
            "tipo": self.__tipo,
            "periodo": self.__periodo,
            "fecha_generacion": self.__fecha_generacion.strftime('%d/%m/%Y'),
            "generado_por": self.__generado_por.get_nombre_completo(),
            "numero_datos": len(self.__datos),
            "finalizado": self.__finalizado,
            "produccion_total": self.calcular_produccion_total()
        }
        
      
        valores_numericos = []
        for valor in self.__datos.values():
            try:
                valores_numericos.append(float(valor))
            except (ValueError, TypeError):
                pass
        
        if valores_numericos:
            estadisticas["promedio"] = sum(valores_numericos) / len(valores_numericos)
            estadisticas["maximo"] = max(valores_numericos)
            estadisticas["minimo"] = min(valores_numericos)
        
        return estadisticas
    
    def comparar_con_meta(self, meta: float) -> dict:
        """
        Compara la producción del reporte con una meta establecida.
        
        Args:
            meta: Meta de producción en kilogramos
            
        Returns:
            Diccionario con el análisis de cumplimiento
        """
        produccion = self.calcular_produccion_total()
        
        if meta > 0:
            porcentaje = (produccion / meta) * 100
            cumplido = porcentaje >= 100
            diferencia = produccion - meta
            
            return {
                "meta": meta,
                "produccion": produccion,
                "porcentaje": porcentaje,
                "cumplido": cumplido,
                "diferencia": diferencia,
                "estado": "✓ Meta cumplida" if cumplido else "Meta no cumplida"
            }
        
        return {"error": "Meta debe ser mayor a 0"}
    
    def __str__(self) -> str:
        """Representación en string del reporte."""
        estado = "Finalizado" if self.__finalizado else "En progreso"
        return f"Reporte #{self.__id} [{self.__tipo}] - {estado}"
    
    def __repr__(self) -> str:
        """Representación técnica del reporte."""
        return f"Reporte(id={self.__id}, tipo='{self.__tipo}', periodo='{self.__periodo}')"
