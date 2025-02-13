# Mateando - E-commerce App (Trabajo Final UTN FRRo)

Este repositorio contiene el trabajo final de mi primer año en la Tecnicatura en Programación de la UTN de Rosario, realizado en grupo con mis compañeros. El proyecto fue clonado del repositorio de uno de ellos.

Repositorio original: [https://github.com/GGabi40/UTN-FRRO-Programacion-II-Mateando](https://github.com/GGabi40/UTN-FRRO-Programacion-II-Mateando)

## Descripción

**Mateando** es una aplicación web desarrollada en **ESPAÑOL** con **Flask**, que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar un comercio electrónico de productos relacionados con la cultura del mate. Además, incluye:

- Manejo de inicio de sesión de usuarios.
- Conexión con un servidor de correo electrónico para notificaciones.
- Interfaz web con HTML, CSS y JavaScript.

### Tecnologías utilizadas:
- **Backend**: Flask (incluyendo Flask Login, Flask Mail, etc.)
- **Frontend**: HTML, CSS, JavaScript
- **Base de datos**: SQLite
- **Otros**: Python

## Cómo iniciar el proyecto

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Justina-R/Mateando-TUP
   ```

2. **Crear un entorno virtual**:
   En la raíz del proyecto, crea un entorno virtual con el siguiente comando:
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Crear un archivo `.env`**:
   Copia el archivo `env_example.txt` y renómbralo a `.env`. Asegúrate de completar las variables con la información correspondiente (como las credenciales de correo).

6. **Cargar la base de datos (opcional)**:
   Si quieres cargar los datos iniciales en la base de datos, ejecuta el archivo `load_bbdd.py`:
   ```bash
   python load_bbdd.py
   ```

## Mejoras planeadas

Para mejorar la aplicación, planeo incorporar **Flask Migrate** para gestionar las migraciones de la base de datos de manera más eficiente. Estoy abierta a cualquier otra recomendación para optimizar o agregar nuevas funcionalidades a la app.

## Deployment

Puedes ver la aplicación desplegada en **Render** en el siguiente enlace: https://mateando-tup.onrender.com/.

---

¡Gracias por visitar el repositorio! Si tienes alguna duda o sugerencia, no dudes en contactarme o abrir un issue en este repositorio.

