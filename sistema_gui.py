"""
SISTEMA_GUI.PY - Sistema de Gestión de Orellanas con Interfaz Gráfica
"""

import tkinter as tk
from tkinter import ttk, messagebox
from clases.usuario import Usuario
from clases.trabajador import Trabajador
from clases.supervisor import Supervisor
from clases.jefe_planta import JefePlanta
from clases.estanteria import Estanteria
from clases.publicacion import Publicacion
from clases.reporte import Reporte
from clases.alerta import Alerta

class SistemaOrellanas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Orellanas")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Usuario actual
        self.usuario_actual = None
        
        # Base de datos de usuarios (simulada)
        self.usuarios = self._crear_usuarios_ejemplo()
        
        # Estanterías de ejemplo
        self.estanterias = self._crear_estanterias_ejemplo()
        
        self._crear_interfaz_login()
    
    def _crear_usuarios_ejemplo(self):
        """Crear usuarios de ejemplo para el sistema"""
        return {
            "trabajador": Trabajador("Juan", "Pérez", "trabajador", "123", "juan@orellanas.com", "mañana"),
            "supervisor": Supervisor("Carlos", "Ramírez", "supervisor", "123", "carlos@orellanas.com", "Producción"),
            "jefe": JefePlanta("Ana", "Martínez", "jefe", "123", "ana@orellanas.com"),
            "admin": JefePlanta("Admin", "Sistema", "admin", "admin", "admin@orellanas.com")
        }
    
    def _crear_estanterias_ejemplo(self):
        """Crear estanterías de ejemplo"""
        estanterias = []
        for i in range(3):
            est = Estanteria(f"00{i+1}")
            if i < 2:
                est.iniciar_produccion()
            estanterias.append(est)
        return estanterias
    
    def _crear_interfaz_login(self):
        """Crear interfaz de login"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        frame = tk.Frame(self.root, bg='#2c3e50', padx=50, pady=50)
        frame.pack(expand=True, fill='both')
        
        # Título
        titulo = tk.Label(frame, text="Sistema de Gestión de Orellanas", 
                         font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
        titulo.pack(pady=20)
        
        # Frame de login
        login_frame = tk.Frame(frame, bg='#34495e', padx=30, pady=30, relief='raised', bd=2)
        login_frame.pack(pady=20)
        
        # Usuario
        tk.Label(login_frame, text="Usuario:", font=('Arial', 12), 
                fg='white', bg='#34495e').grid(row=0, column=0, sticky='w', pady=10)
        self.entry_usuario = tk.Entry(login_frame, font=('Arial', 12), width=20)
        self.entry_usuario.grid(row=0, column=1, pady=10, padx=10)
        self.entry_usuario.insert(0, "trabajador")  # Usuario por defecto
        
        # Contraseña
        tk.Label(login_frame, text="Contraseña:", font=('Arial', 12), 
                fg='white', bg='#34495e').grid(row=1, column=0, sticky='w', pady=10)
        self.entry_password = tk.Entry(login_frame, font=('Arial', 12), width=20, show='*')
        self.entry_password.grid(row=1, column=1, pady=10, padx=10)
        self.entry_password.insert(0, "123")  # Contraseña por defecto
        
        # Botón de login
        btn_login = tk.Button(login_frame, text="Iniciar Sesión", font=('Arial', 12, 'bold'),
                             command=self._login, bg='#27ae60', fg='white', width=15)
        btn_login.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Información de usuarios de prueba
        info_frame = tk.Frame(frame, bg='#2c3e50')
        info_frame.pack(pady=20)
        
        info_text = """Usuarios de prueba:
• Trabajador: trabajador / 123
• Supervisor: supervisor / 123  
• Jefe: jefe / 123
• Admin: admin / admin"""
        
        tk.Label(info_frame, text=info_text, font=('Arial', 10), 
                fg='#bdc3c7', bg='#2c3e50', justify='left').pack()
    
    def _login(self):
        """Manejar el proceso de login"""
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        if usuario in self.usuarios:
            user_obj = self.usuarios[usuario]
            if user_obj.validar_credenciales(usuario, password):
                self.usuario_actual = user_obj
                self._crear_interfaz_principal()
                return
        
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    
    def _crear_interfaz_principal(self):
        """Crear interfaz principal según el rol del usuario"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Barra superior
        top_frame = tk.Frame(self.root, bg='#34495e', height=60)
        top_frame.pack(fill='x')
        top_frame.pack_propagate(False)
        
        # Información del usuario
        user_info = f"Usuario: {self.usuario_actual.get_nombre_completo()} - Rol: {self.usuario_actual.get_rol()}"
        tk.Label(top_frame, text=user_info, font=('Arial', 12, 'bold'), 
                fg='white', bg='#34495e').pack(side='left', padx=20, pady=20)
        
        # Botón de logout
        btn_logout = tk.Button(top_frame, text="Cerrar Sesión", font=('Arial', 10),
                              command=self._logout, bg='#e74c3c', fg='white')
        btn_logout.pack(side='right', padx=20, pady=20)
        
        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Pestañas según permisos
        permisos = self.usuario_actual.obtener_permisos()
        
        # Pestaña de Dashboard (todos los roles)
        self._crear_pestana_dashboard(notebook)
        
        # Pestaña de Estanterías (todos los roles)
        if "ver_estanterias" in permisos:
            self._crear_pestana_estanterias(notebook)
        
        # Pestaña de Tareas (trabajadores y supervisores)
        if "completar_tareas" in permisos or "asignar_tareas" in permisos:
            self._crear_pestana_tareas(notebook)
        
        # Pestaña de Publicaciones (jefes y supervisores)
        if "crear_publicaciones" in permisos:
            self._crear_pestana_publicaciones(notebook)
        
        # Pestaña de Reportes (supervisores y jefes)
        if "generar_reportes" in permisos:
            self._crear_pestana_reportes(notebook)
    
    def _crear_pestana_dashboard(self, notebook):
        """Crear pestaña de dashboard"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Dashboard")
        
        # Título
        tk.Label(frame, text=f"Bienvenido, {self.usuario_actual.get_nombre_completo()}",
                font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Información del usuario
        info_text = f"""
Rol: {self.usuario_actual.get_rol()}
Permisos: {', '.join(self.usuario_actual.obtener_permisos())}

Resumen del sistema:
• Estanterías activas: {sum(1 for e in self.estanterias if e.esta_activa())}
• Total de tubulares: {sum(e.contar_tubulares_total() for e in self.estanterias)}
• Estanterías en producción: {sum(1 for e in self.estanterias if e.esta_activa())}
"""
        
        tk.Label(frame, text=info_text, font=('Arial', 12), justify='left').pack(pady=20)
        
        # Reporte del usuario actual
        reporte_frame = tk.Frame(frame, relief='sunken', bd=2, padx=10, pady=10)
        reporte_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(reporte_frame, text="Mi Reporte:", font=('Arial', 12, 'bold')).pack(anchor='w')
        reporte_text = tk.Text(reporte_frame, height=8, width=80)
        reporte_text.pack(pady=10, fill='both', expand=True)
        reporte_text.insert('1.0', self.usuario_actual.generar_reporte())
        reporte_text.config(state='disabled')
    
    def _crear_pestana_estanterias(self, notebook):
        """Crear pestaña de estanterías"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Estanterías")
        
        # Título
        tk.Label(frame, text="Gestión de Estanterías", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para controles
        controls_frame = tk.Frame(frame)
        controls_frame.pack(pady=10, fill='x')
        
        # Botón para actualizar
        btn_actualizar = tk.Button(controls_frame, text="Actualizar Lista", 
                                  command=lambda: self._actualizar_lista_estanterias(tree))
        btn_actualizar.pack(side='left', padx=5)
        
        # Treeview para estanterías
        columns = ('Código', 'Estado', 'Fase', 'Tubulares', 'Defectuosos', 'Eficiencia')
        tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        tree.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Llenar con datos
        self._actualizar_lista_estanterias(tree)
        
        # Botón para ver detalles
        btn_detalles = tk.Button(frame, text="Ver Detalles", 
                                command=lambda: self._mostrar_detalles_estanteria(tree))
        btn_detalles.pack(pady=10)
    
    def _actualizar_lista_estanterias(self, tree):
        """Actualizar lista de estanterías"""
        # Limpiar treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Agregar estanterías
        for estanteria in self.estanterias:
            estado = "Activa" if estanteria.esta_activa() else "Inactiva"
            tree.insert('', 'end', values=(
                estanteria.get_codigo(),
                estado,
                estanteria.get_fase(),
                estanteria.contar_tubulares_total(),
                estanteria.contar_defectuosos_total(),
                f"{estanteria.calcular_eficiencia_total()}%"
            ))
    
    def _mostrar_detalles_estanteria(self, tree):
        """Mostrar detalles de la estantería seleccionada"""
        selection = tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona una estantería")
            return
        
        item = tree.item(selection[0])
        codigo = item['values'][0]
        
        # Encontrar la estantería
        for estanteria in self.estanterias:
            if estanteria.get_codigo() == codigo:
                detalles = estanteria.generar_resumen()
                messagebox.showinfo(f"Detalles - {codigo}", detalles)
                break
    
    def _crear_pestana_tareas(self, notebook):
        """Crear pestaña de tareas"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Tareas")
        
        tk.Label(frame, text="Gestión de Tareas", font=('Arial', 14, 'bold')).pack(pady=10)
        
        permisos = self.usuario_actual.obtener_permisos()
        
        if "asignar_tareas" in permisos:
            # Interfaz para supervisores
            self._crear_interfaz_supervisor_tareas(frame)
        else:
            # Interfaz para trabajadores
            self._crear_interfaz_trabajador_tareas(frame)
    
    def _crear_interfaz_trabajador_tareas(self, frame):
        """Interfaz de tareas para trabajadores"""
        tk.Label(frame, text="Mis Tareas", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Lista de tareas simuladas
        tareas = [
            "Revisar estantería 001",
            "Inocular tubulares piso 1", 
            "Reportar tubulares defectuosos",
            "Limpiar área de trabajo"
        ]
        
        for i, tarea in enumerate(tareas, 1):
            tarea_frame = tk.Frame(frame, relief='groove', bd=1)
            tarea_frame.pack(pady=5, padx=20, fill='x')
            
            tk.Label(tarea_frame, text=f"{i}. {tarea}", font=('Arial', 10)).pack(side='left', padx=10)
            btn_completar = tk.Button(tarea_frame, text="Completar", 
                                    command=lambda t=tarea: self._completar_tarea(t))
            btn_completar.pack(side='right', padx=10)
    
    def _crear_interfaz_supervisor_tareas(self, frame):
        """Interfaz de tareas para supervisores"""
        tk.Label(frame, text="Asignación de Tareas", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Frame para asignar tareas
        asignar_frame = tk.Frame(frame)
        asignar_frame.pack(pady=10, fill='x', padx=20)
        
        tk.Label(asignar_frame, text="Trabajador:").grid(row=0, column=0, sticky='w')
        trabajador_var = tk.StringVar()
        trabajadores = ["Juan Pérez", "María González", "Pedro López"]
        trabajador_combo = ttk.Combobox(asignar_frame, textvariable=trabajador_var, values=trabajadores)
        trabajador_combo.grid(row=0, column=1, padx=5)
        trabajador_combo.set(trabajadores[0])
        
        tk.Label(asignar_frame, text="Tarea:").grid(row=1, column=0, sticky='w')
        tarea_entry = tk.Entry(asignar_frame, width=30)
        tarea_entry.grid(row=1, column=1, padx=5, pady=5)
        
        btn_asignar = tk.Button(asignar_frame, text="Asignar Tarea",
                               command=lambda: self._asignar_tarea(trabajador_var.get(), tarea_entry.get()))
        btn_asignar.grid(row=2, column=0, columnspan=2, pady=10)
    
    def _crear_pestana_publicaciones(self, notebook):
        """Crear pestaña de publicaciones"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Publicaciones")
        
        tk.Label(frame, text="Gestión de Publicaciones", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Frame para crear publicaciones
        crear_frame = tk.Frame(frame)
        crear_frame.pack(pady=10, fill='x', padx=20)
        
        tk.Label(crear_frame, text="Título:").grid(row=0, column=0, sticky='w')
        titulo_entry = tk.Entry(crear_frame, width=40)
        titulo_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(crear_frame, text="Contenido:").grid(row=1, column=0, sticky='nw')
        contenido_text = tk.Text(crear_frame, width=40, height=5)
        contenido_text.grid(row=1, column=1, padx=5, pady=5)
        
        btn_publicar = tk.Button(crear_frame, text="Crear Publicación",
                               command=lambda: self._crear_publicacion(titulo_entry.get(), contenido_text.get('1.0', 'end')))
        btn_publicar.grid(row=2, column=0, columnspan=2, pady=10)
    
    def _crear_pestana_reportes(self, notebook):
        """Crear pestaña de reportes"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Reportes")
        
        tk.Label(frame, text="Generación de Reportes", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Botones para diferentes reportes
        btn_reporte_personal = tk.Button(frame, text="Mi Reporte Personal", 
                                       command=self._generar_reporte_personal, width=20)
        btn_reporte_personal.pack(pady=5)
        
        btn_reporte_estanterias = tk.Button(frame, text="Reporte de Estanterías",
                                          command=self._generar_reporte_estanterias, width=20)
        btn_reporte_estanterias.pack(pady=5)
        
        btn_reporte_general = tk.Button(frame, text="Reporte General",
                                      command=self._generar_reporte_general, width=20)
        btn_reporte_general.pack(pady=5)
    
    def _completar_tarea(self, tarea):
        """Completar una tarea"""
        messagebox.showinfo("Tarea Completada", f"Tarea completada: {tarea}")
    
    def _asignar_tarea(self, trabajador, tarea):
        """Asignar una tarea a un trabajador"""
        if tarea:
            messagebox.showinfo("Tarea Asignada", f"Tarea '{tarea}' asignada a {trabajador}")
        else:
            messagebox.showwarning("Error", "Ingresa una tarea")
    
    def _crear_publicacion(self, titulo, contenido):
        """Crear una publicación"""
        if titulo and contenido.strip():
            messagebox.showinfo("Publicación Creada", f"Publicación '{titulo}' creada exitosamente")
        else:
            messagebox.showwarning("Error", "Completa título y contenido")
    
    def _generar_reporte_personal(self):
        """Generar reporte personal"""
        reporte = self.usuario_actual.generar_reporte()
        messagebox.showinfo("Mi Reporte", reporte)
    
    def _generar_reporte_estanterias(self):
        """Generar reporte de estanterías"""
        reporte = "REPORTE DE ESTANTERÍAS\n" + "="*30 + "\n"
        for estanteria in self.estanterias:
            reporte += f"\n{estanteria.get_codigo()}: {estanteria.get_fase()} - Defectuosos: {estanteria.contar_defectuosos_total()}\n"
        
        messagebox.showinfo("Reporte de Estanterías", reporte)
    
    def _generar_reporte_general(self):
        """Generar reporte general"""
        total_tubulares = sum(e.contar_tubulares_total() for e in self.estanterias)
        total_defectuosos = sum(e.contar_defectuosos_total() for e in self.estanterias)
        
        reporte = f"""
REPORTE GENERAL DEL SISTEMA
==========================
Estanterías totales: {len(self.estanterias)}
Estanterías activas: {sum(1 for e in self.estanterias if e.esta_activa())}
Tubulares totales: {total_tubulares}
Tubulares defectuosos: {total_defectuosos}
Eficiencia general: {(total_tubulares - total_defectuosos) / total_tubulares * 100:.1f}%
=========================="""
        
        messagebox.showinfo("Reporte General", reporte)
    
    def _logout(self):
        """Cerrar sesión"""
        self.usuario_actual = None
        self._crear_interfaz_login()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()


# Ejecutar el sistema
if __name__ == "__main__":
    app = SistemaOrellanas()
    app.ejecutar()
