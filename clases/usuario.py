"""
Clase Usuario - Clase abstracta base para todos los tipos de usuarios
Sistema de Gestión de Producción de Orellanas

Autor: [Juan David Valencia Vera]
Fecha: Noviembre 2024
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Usuario(ABC):
    """
    Clase abstracta que representa a un usuario del sistema.
    
    Esta clase implementa los principios de:
    - Abstracción: Define la estructura común para todos los usuarios
    - Encapsulación: Atributos privados con getters y setters
    - Polimorfismo: Métodos abstractos que deben implementar las clases hijas
    """
    

    _contador_id = 0
    
    def __init__(self, nombre: str, apellido: str, username: str, 
                 password: str, email: str, rol: str):
        """
        Constructor de la clase Usuario.
        
        Args:
            nombre: Nombre del usuario
            apellido: Apellido del usuario
            username: Nombre de usuario único
            password: Contraseña del usuario
            email: Correo electrónico
            rol: Rol del usuario en el sistema
        """
        
        Usuario._contador_id += 1
        self.__id = Usuario._contador_id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__username = username
        self.__password = password
        self.__email = email
        self.__rol = rol
        self.__fecha_creacion = datetime.now()
    
  
    def get_id(self) -> int:
        """Retorna el ID del usuario."""
        return self.__id
    
    def get_nombre(self) -> str:
        """Retorna el nombre del usuario."""
        return self.__nombre
    
    def get_apellido(self) -> str:
        """Retorna el apellido del usuario."""
        return self.__apellido
    
    def get_username(self) -> str:
        """Retorna el nombre de usuario."""
        return self.__username
    
    def get_email(self) -> str:
        """Retorna el email del usuario."""
        return self.__email
    
    def get_rol(self) -> str:
        """Retorna el rol del usuario."""
        return self.__rol
    
    def get_fecha_creacion(self) -> datetime:
        """Retorna la fecha de creación del usuario."""
        return self.__fecha_creacion
    
    def get_nombre_completo(self) -> str:
        """Retorna el nombre completo del usuario."""
        return f"{self.__nombre} {self.__apellido}"
    
    def set_nombre(self, nombre: str) -> None:
        """Establece un nuevo nombre para el usuario."""
        if nombre and len(nombre) > 0:
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    def set_apellido(self, apellido: str) -> None:
        """Establece un nuevo apellido para el usuario."""
        if apellido and len(apellido) > 0:
            self.__apellido = apellido
        else:
            raise ValueError("El apellido no puede estar vacío")
    
    def set_email(self, email: str) -> None:
        """Establece un nuevo email para el usuario."""
        if email and "@" in email:
            self.__email = email
        else:
            raise ValueError("El email no es válido")
    
    def validar_credenciales(self, username: str, password: str) -> bool:
        """
        Valida las credenciales del usuario.
        
        Args:
            username: Nombre de usuario a validar
            password: Contraseña a validar
            
        Returns:
            True si las credenciales son correctas, False en caso contrario
        """
        return self.__username == username and self.__password == password
    
    def cambiar_password(self, password_actual: str, password_nueva: str) -> bool:
        """
        Cambia la contraseña del usuario.
        
        Args:
            password_actual: Contraseña actual para verificación
            password_nueva: Nueva contraseña a establecer
            
        Returns:
            True si el cambio fue exitoso, False en caso contrario
        """
        if self.__password == password_actual:
            if len(password_nueva) >= 6:
                self.__password = password_nueva
                return True
            else:
                raise ValueError("La contraseña debe tener al menos 6 caracteres")
        return False
    

    
    @abstractmethod
    def generar_reporte(self) -> str:
        """
        Genera un reporte específico según el tipo de usuario.
        Este método debe ser implementado por cada clase hija.
        
        Returns:
            String con el contenido del reporte
        """
        pass
    
    @abstractmethod
    def obtener_permisos(self) -> list:
        """
        Retorna la lista de permisos del usuario según su rol.
        Este método debe ser implementado por cada clase hija.
        
        Returns:
            Lista de strings con los permisos del usuario
        """
        pass
    
    def __str__(self) -> str:
        """Representación en string del usuario."""
        return f"Usuario(id={self.__id}, username='{self.__username}', rol='{self.__rol}')"
    
    def __repr__(self) -> str:
        """Representación técnica del usuario."""
        return self.__str__()
