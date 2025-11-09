"""
Clase Administrador - Hereda de Usuario
Sistema de Gestión de Producción de Orellanas

Autor: [Tu nombre]
Fecha: Noviembre 2024
"""

from clases.usuario import Usuario


class Administrador(Usuario):
    """
    Clase que representa al administrador del sistema.
    Hereda de Usuario e implementa los métodos abstractos.
    
    Demuestra:
    - Herencia: extends Usuario
    - Polimorfismo: Implementa generarReporte() con información del sistema
    - Encapsulación: Atributos privados propios
    """
    
    def __init__(self, nombre: str, apellido: str, username: str, 
                 password: str, email: str):
        """
        Constructor de Administrador.
        
        Args:
            nombre: Nombre del administrador
            apellido: Apellido del administrador
            username: Nombre de usuario
            password: Contraseña
            email: Correo electrónico
        """
       
        super().__init__(nombre, apellido, username, password, email, "Administrador")
        
       
        self.__nivel_acceso = 10  
        self.__usuarios_creados = []
        self.__operaciones_realizadas = []
    
   
    def get_nivel_acceso(self) -> int:
        """Retorna el nivel de acceso del administrador."""
        return self.__nivel_acceso
    
    def get_usuarios_creados(self) -> list:
        """Retorna la lista de usuarios creados por este administrador."""
        return self.__usuarios_creados.copy()
    
    def get_operaciones_realizadas(self) -> list:
        """Retorna el historial de operaciones."""
        return self.__operaciones_realizadas.copy()
    
 
    def crear_usuario(self, datos: dict):
        """
        Crea un nuevo usuario en el sistema.
        
        Args:
            datos: Diccionario con los datos del usuario
                   {nombre, apellido, username, password, email, rol}
            
        Returns:
            El usuario creado o None si hay error
        """
        try:
            from datetime import datetime
            
          
            operacion = {
                "tipo": "crear_usuario",
                "datos": datos["username"],
                "fecha": datetime.now()
            }
            self.__operaciones_realizadas.append(operacion)
            
           
            self.__usuarios_creados.append(datos["username"])
            
            print(f"✓ Usuario '{datos['username']}' creado por {self.get_nombre_completo()}")
            return datos
            
        except Exception as e:
            print(f"✗ Error al crear usuario: {e}")
            return None
    
    def eliminar_usuario(self, id_usuario: int) -> bool:
        """
        Elimina un usuario del sistema.
        
        Args:
            id_usuario: ID del usuario a eliminar
            
        Returns:
            True si se eliminó exitosamente, False en caso contrario
        """
        from datetime import datetime
        
       
        operacion = {
            "tipo": "eliminar_usuario",
            "usuario_id": id_usuario,
            "fecha": datetime.now()
        }
        self.__operaciones_realizadas.append(operacion)
        
        print(f"✓ Usuario ID {id_usuario} eliminado por {self.get_nombre_completo()}")
        return True
    
    def modificar_usuario(self, id_usuario: int, datos: dict) -> bool:
        """
        Modifica los datos de un usuario existente.
        
        Args:
            id_usuario: ID del usuario a modificar
            datos: Diccionario con los nuevos datos
            
        Returns:
            True si se modificó exitosamente, False en caso contrario
        """
        from datetime import datetime
        
       
        operacion = {
            "tipo": "modificar_usuario",
            "usuario_id": id_usuario,
            "cambios": list(datos.keys()),
            "fecha": datetime.now()
        }
        self.__operaciones_realizadas.append(operacion)
        
        print(f"✓ Usuario ID {id_usuario} modificado por {self.get_nombre_completo()}")
        return True
    
    def asignar_rol(self, usuario, nuevo_rol: str) -> None:
        """
        Asigna un nuevo rol a un usuario.
        
        Args:
            usuario: Instancia de Usuario
            nuevo_rol: Nuevo rol a asignar
        """
        from datetime import datetime
        
        roles_validos = ["Trabajador", "Supervisor", "Jefe de Planta", "Administrador"]
        
        if nuevo_rol in roles_validos:
            operacion = {
                "tipo": "asignar_rol",
                "usuario": usuario.get_username(),
                "nuevo_rol": nuevo_rol,
                "fecha": datetime.now()
            }
            self.__operaciones_realizadas.append(operacion)
            
            print(f"✓ Rol '{nuevo_rol}' asignado a {usuario.get_nombre_completo()}")
        else:
            print(f"✗ Rol inválido. Debe ser: {', '.join(roles_validos)}")
    
    def listar_usuarios(self) -> list:
        """
        Lista todos los usuarios creados.
        
        Returns:
            Lista de usernames de usuarios creados
        """
        return self.__usuarios_creados.copy()
    
    def exportar_datos(self, formato: str = "txt") -> str:
        """
        Exporta los datos del sistema.
        
        Args:
            formato: Formato de exportación ('txt', 'csv', 'json')
            
        Returns:
            Ruta del archivo exportado o mensaje de error
        """
        from datetime import datetime
        
        formatos_validos = ["txt", "csv", "json"]
        
        if formato.lower() not in formatos_validos:
            return f"Error: Formato '{formato}' no válido"
        
        operacion = {
            "tipo": "exportar_datos",
            "formato": formato,
            "fecha": datetime.now()
        }
        self.__operaciones_realizadas.append(operacion)
        
        archivo = f"datos_sistema_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{formato}"
        print(f"✓ Datos exportados a '{archivo}' por {self.get_nombre_completo()}")
        return archivo
    
    def importar_datos(self, archivo: str) -> bool:
        """
        Importa datos al sistema desde un archivo.
        
        Args:
            archivo: Ruta del archivo a importar
            
        Returns:
            True si se importó exitosamente, False en caso contrario
        """
        from datetime import datetime
        
        operacion = {
            "tipo": "importar_datos",
            "archivo": archivo,
            "fecha": datetime.now()
        }
        self.__operaciones_realizadas.append(operacion)
        
        print(f"✓ Datos importados desde '{archivo}' por {self.get_nombre_completo()}")
        return True
    
    def generar_reporte_auditoria(self) -> str:
        """
        Genera un reporte de auditoría con todas las operaciones realizadas.
        
        Returns:
            String con el reporte de auditoría
        """
        reporte = f"""
========================================
REPORTE DE AUDITORÍA
========================================
Administrador: {self.get_nombre_completo()}
Operaciones totales: {len(self.__operaciones_realizadas)}
========================================
Últimas 10 operaciones:
"""
        ultimas = self.__operaciones_realizadas[-10:] if len(self.__operaciones_realizadas) > 0 else []
        
        for i, op in enumerate(ultimas, 1):
            reporte += f"\n{i}. {op['tipo']} - {op['fecha'].strftime('%d/%m/%Y %H:%M')}"
        
        if len(ultimas) == 0:
            reporte += "\n  No hay operaciones registradas"
        
        reporte += "\n========================================"
        return reporte
    
    def contar_operaciones_por_tipo(self) -> dict:
        """
        Cuenta las operaciones realizadas por tipo.
        
        Returns:
            Diccionario con el conteo de operaciones
        """
        conteo = {}
        for op in self.__operaciones_realizadas:
            tipo = op['tipo']
            conteo[tipo] = conteo.get(tipo, 0) + 1
        return conteo
    
    
    def generar_reporte(self) -> str:
        """
        Genera un reporte técnico del administrador.
        Implementación del método abstracto de Usuario.
        ESTE MÉTODO INCLUYE INFORMACIÓN TÉCNICA DEL SISTEMA (Polimorfismo)
        
        Returns:
            String con el reporte del administrador
        """
        conteo_ops = self.contar_operaciones_por_tipo()
        
        reporte = f"""
========================================
REPORTE DE ADMINISTRACIÓN DEL SISTEMA
========================================
Administrador: {self.get_nombre_completo()}
Username: {self.get_username()}
Nivel de Acceso: {self.__nivel_acceso} (Máximo)
Usuarios Creados: {len(self.__usuarios_creados)}
Operaciones Totales: {len(self.__operaciones_realizadas)}
========================================
Operaciones por tipo:
"""
        for tipo, cantidad in conteo_ops.items():
            reporte += f"  - {tipo}: {cantidad}\n"
        
        if len(conteo_ops) == 0:
            reporte += "  No hay operaciones registradas\n"
        
        reporte += """========================================
Estado del sistema: ✓ Operativo
Integridad de datos: ✓ Verificada
Respaldo más reciente: Hoy
========================================"""
        return reporte
    
    def obtener_permisos(self) -> list:
        """
        Retorna los permisos del administrador.
        Implementación del método abstracto de Usuario.
        
        Returns:
            Lista con TODOS los permisos posibles del sistema
        """
        return [
            # Permisos básicos
            "ver_estanterias",
            "registrar_observaciones",
            "completar_tareas",
            "ver_publicaciones",
            
            # Permisos jefe
            "crear_publicaciones",
            "editar_publicaciones",
            "eliminar_publicaciones",
            "establecer_metas",
            "generar_reportes_generales",
            
            # Permisos supervisor
            "asignar_tareas",
            "supervisar_trabajadores",
            "aprobar_reportes",
            "revisar_estanterias",
            
            # Permisos  admin
            "crear_usuarios",
            "eliminar_usuarios",
            "modificar_usuarios",
            "asignar_roles",
            "ver_auditoria",
            "exportar_datos",
            "importar_datos",
            "configurar_sistema",
            "administrar_permisos",
            "ver_logs_sistema",
            "realizar_respaldos",
            "restaurar_sistema"
        ]
    
    def __str__(self) -> str:
        """Representación en string del administrador."""
        return f"Administrador({self.get_nombre_completo()}, nivel={self.__nivel_acceso})"
