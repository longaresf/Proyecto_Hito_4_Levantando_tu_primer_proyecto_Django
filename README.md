# Django Data Models & MVT Architecture

Este repositorio contiene un proyecto backend desarrollado en **Python** utilizando el framework **Django**. El enfoque principal de este hito es el diseño, implementación y migración de la capa de datos a través del **ORM de Django**, consolidando la arquitectura **MVT (Model-View-Template)** para permitir la persistencia real de información y su renderizado dinámico en la interfaz web.

## 🚀 Características y Capacidades Técnicas

* **Modelado de Datos con ORM:** Diseño de entidades y tablas relacionales en código Python utilizando `models.Model`, definiendo tipos de datos estructurados y restricciones de integridad.
* **Sistema de Migraciones Activo:** Gestión del ciclo de vida de la base de datos mediante comandos de preparación (`makemigrations`) y ejecución (`migrate`) para sincronizar de forma segura el esquema del servidor.
* **Integración Completa MVT:** Conexión fluida del flujo web: consultas a la base de datos desde los Modelos, procesamiento lógico en las Vistas e inyección de datos dinámicos mediante etiquetas del motor de plantillas (*Django Templates*).
* **Consola de Administración (Django Admin):** Configuración y personalización del panel administrador nativo para la gestión y auditoría directa de los registros de la aplicación.

## 🛠️ Stack Tecnológico

* **Lenguaje de Programación:** Python 3.x
* **Framework Backend:** Django 4.x / 5.x
* **Base de Datos:** PostgreSQL.
* **Arquitectura:** MVT (Model-View-Template)

## ⚙️ Arquitectura de Datos y Buenas Prácticas Solucionadas

El desarrollo de este hito aborda la resolución de la persistencia de datos en aplicaciones comerciales:

1. **Abstracción de Consultas (ORM):** Se implementó el uso de *QuerySets* para interactuar con la base de datos sin escribir código SQL crudo, lo que garantiza la seguridad del sistema contra ataques de inyección SQL y facilita la portabilidad de la base de datos.
2. **Consistencia en las Relaciones:** Configuración de llaves foráneas (`ForeignKey`) o relaciones de datos aplicando borrados en cascada (`on_delete=models.CASCADE`) para mantener la integridad de la información.
3. **Control del Contexto en Plantillas:** Optimización del paso de datos del backend al frontend, permitiendo que las interfaces HTML reaccionen dinámicamente según los registros existentes en la base de datos (ej. bucles `{% for %}` y condicionales `{% if %}`).

## 🔧 Configuración e Instalación Local

Sigue estos pasos para clonar el proyecto, preparar la base de datos y ejecutar el servidor localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/django-data-models-mvt.git](https://github.com/longaresf/django-data-models-mvt.git)
   ```
2. Ingresar al directorio del proyecto:
   Bash
   cd django-data-models-mvt

3. Inicializar y activar el entorno virtual:
   Bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

4. Instalar dependencias:
   Bash
   pip install -r requirements.txt

5. Ejecutar las migraciones (Creación de tablas de base de datos):
   Bash
   python manage.py makemigrations
   python manage.py migrate

6. [Opcional] Crear superusuario para el panel de administración:
   Bash
   python manage.py createsuperuser

7. Iniciar el servidor de desarrollo:
   Bash
   python manage.py runserver

   Visita http://127.0.0.1:8000/ para ver la aplicación o http://127.0.0.1:8000/admin para gestionar los modelos de datos creados.

✒️ Créditos y Contexto
   Francisco Longares - Desarrollador Backend Python - longaresf
   Este proyecto representa la resolución del hito práctico de persistencia, ORM y lógica de modelos dentro del programa de especialización Full Stack Python de Desafío Latam.
