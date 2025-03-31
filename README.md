1️⃣ Creación y Desarrollo de la Aplicación Flask
Antes de desplegar la aplicación, se trabajó en su desarrollo en Python con Flask.

🔹 Pasos realizados en el código:
Definir el backend con Flask (app.py):

Implementación de la lógica para calcular el IMC y nivel de riesgo.

Uso de Flask para manejar las solicitudes GET y POST.

Renderizado de una plantilla HTML para la interfaz de usuario.

Desarollo frontend - Creación plantilla HTML (templates/index.html):

Formulario para ingresar peso, altura y seleccionar factores de riesgo.

Sección para mostrar el IMC calculado y su clasificación.

Sección con checkboxes alineados para seleccionar factores de riesgo.

Pie de página con una advertencia y firma de la aplicación.

Incluir archivos estáticos (static/):

Se creó la carpeta static/images/ para almacenar el logo de la aplicación.

Se utilizó CSS para mejorar la presentación y alineación del formulario.

Archivo de dependencias (requirements.txt):

Se listaron las librerías necesarias para ejecutar la aplicación:

txt
Copiar
Editar
flask
gunicorn
Esto es esencial para que Render instale los paquetes al momento del despliegue.

2️⃣ Creación del Repositorio en GitHub
Para poder desplegar la aplicación en Render, primero se almacenó en GitHub.

🔹 Pasos realizados en GitHub:
Crear un nuevo repositorio en GitHub con el nombre riesgo-salud-app.

Subir los archivos del proyecto, incluyendo:

app.py (código principal en Flask).

templates/index.html (interfaz HTML).

static/images/logo.png (logo de la aplicación).

requirements.txt (dependencias).

.gitignore (para ignorar archivos innecesarios).

Verificar la estructura del proyecto antes de proceder al despliegue.

3️⃣ Despliegue de la Aplicación en Render
Con el código en GitHub, se procedió a desplegar la aplicación en Render, un servicio gratuito de hosting.

🔹 Pasos realizados en Render:
Ingresar a Render y crear una cuenta.

Seleccionar "New Web Service" para crear un nuevo servicio web.

Conectar con GitHub y elegir el repositorio riesgo-salud-app.

Configurar el despliegue:

Nombre del servicio: riesgo-salud

Runtime: Python 3.x

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Región: Se seleccionó la más cercana para optimizar el rendimiento.

Hacer clic en "Create Web Service" para iniciar el despliegue.

4️⃣ Solución de Problemas y Ajustes
Durante el despliegue, se presentaron algunos inconvenientes que fueron corregidos:

🔹 Errores corregidos:
Error de autenticación al cargar imágenes:
✔ Se solucionó asegurando que las imágenes estuvieran en static/images/ y subiéndolas correctamente a GitHub.

Problemas con dependencias:
✔ Se revisó el archivo requirements.txt y se incluyó gunicorn para que Render ejecutara la aplicación correctamente.

Desalineación de los checkboxes:
✔ Se ajustó el HTML y CSS para que los checkboxes y descripciones quedaran correctamente alineados.

5️⃣ Pruebas y Verificación
Una vez desplegada la aplicación, se realizaron pruebas para confirmar su correcto funcionamiento.

🔹 Verificaciones realizadas:
✅ La URL proporcionada por Render (https://calculadora-riesgo-salud.onrender.com) cargaba correctamente.
✅ Se ingresaron valores de prueba y se verificó que el cálculo del IMC y nivel de riesgo era correcto.
✅ Se confirmó que los checkboxes estaban alineados y que el logo se veía correctamente.
✅ Se agregó un pie de página con advertencia médica y firma de la aplicación.

6️⃣ Despliegue Final y Mantenimiento
🔹 Automatización del despliegue
Cada vez que se sube un cambio a GitHub, Render lo detecta y vuelve a desplegar la aplicación automáticamente.

Se realizaron pruebas periódicas para garantizar que la aplicación siguiera funcionando sin errores.

🎯 Resultado Final
🚀 Aplicación completamente funcional y desplegada en Render.
🌐 Accesible desde cualquier dispositivo con la URL pública.
🔄 Integración automática con GitHub para futuras actualizaciones.

📌 Resumen de las Herramientas Utilizadas
Herramienta	Uso
Flask	Backend para manejar las solicitudes y cálculos.
HTML + CSS	Interfaz gráfica y diseño de la aplicación.
GitHub	Repositorio del código para control de versiones.
Render	Plataforma de hosting para el despliegue web.

📌 Créditos
App creada por: Nestor J. Zuleta M.
