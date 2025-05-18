# 🛡️ Bot seguro de Telegram 🕊️

[![Administrador de paquetes UV](https://img.shields.io/badge/PackageManager-UV-purple.svg)](https://pypi.org/project/uv/)
[![Versión de Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-brightgreen.svg?logo=telegram&logoColor=white)](https://aiogram.dev/)
[![Docker Listo](https://img.shields.io/badge/Docker-Ready-blue.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.x-blue.svg)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-1.7-orange.svg)](https://alembic.sqlalchemy.org/en/latest/)
[![asyncio](https://img.shields.io/badge/asyncio-3. 11-azul.svg)](https://docs.python.org/3/library/asyncio.html)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-green.svg)](https://www.sqlite.org/)
[![NumPy](https://img.shields.io/badge/NumPy-v1.21-azul.svg?logo=numpy&logoColor=blanco)](https://numpy.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-v4.5.1-azul.svg?logo=opencv&logoColor=blanco)](https://opencv.org/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![API de Telegram](https://img.shields.io/badge/Telegram%20API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)

## 🤖 Bienvenido a grammi: un bot de Telegram seguro y ético

¡Bienvenido al repositorio de mi bot de Telegram, diseñado con un enfoque en el uso seguro y ético!

Este bot aprovecha el poder de la biblioteca `aiogram` dentro de una arquitectura de Programación Orientada a Objetos (OOP) y está contenedorizado para una fácil implementación.

Me apasiona contribuir a un entorno de Telegram más seguro y promover interacciones positivas.

**⚠️ Aviso importante:** Prohíbo estrictamente** el uso de este proyecto o cualquier parte del mismo para esquemas fraudulentos, estafas o cualquier actividad que pueda dañar o engañar a personas. Este proyecto se desarrolla con la intención de promover la paz, la amistad y el desarrollo positivo dentro de la comunidad de Telegram. 🚫

## ✨ Ventajas clave de este enfoque

* **Modular y mantenible (OOP):** La arquitectura de programación orientada a objetos promueve la reutilización, la organización y un mantenimiento más sencillo del código. Cada parte de la funcionalidad del bot está encapsulada en clases, lo que hace que el código base sea más limpio y escalable.
* **Gestión eficiente de dependencias (UV):** El uso de `uv` como gestor de paquetes garantiza una instalación de dependencias más rápida y eficiente en comparación con el `pip` tradicional. Esto se traduce en tiempos de compilación más rápidos para la imagen de Docker.
* **Implementación simplificada (Contenedorización):** La contenedorización de Docker empaqueta el bot y todas sus dependencias en un único contenedor portátil. Esto elimina las inconsistencias del entorno y permite una implementación fluida y fiable en diferentes plataformas.
* **Escalabilidad:** La contenedorización facilita el escalado horizontal del bot mediante la ejecución de múltiples instancias del contenedor Docker.
* **Aislamiento:** Docker proporciona cierto nivel de aislamiento, lo que garantiza que las dependencias del bot no interfieran con otras aplicaciones del mismo sistema.

## 🛠️ Primeros pasos

Sigue estos pasos para poner en marcha tu entorno local:

1. **Requisitos previos:**
* 🐍 Python 3.12 o superior instalado en tu sistema ([python.org](https://www.python.org/downloads/)).
* 🐳 Docker instalado en tu sistema ([docker.com](https://www.docker.com/get-started)).
* 📦 `uv` instalado (`pip install uv`).

2. **Clonación del repositorio:**

3. **Compilación de la imagen de Docker:**

``bash
docker build -t grammi-app -f grammi.dockerfile . ```

4. **Crear archivo .env**

Crear archivo .env con el siguiente formato:

``` texto
BOT_TOKEN=<your telegram:token>
ASYNCSQLITE_DB_URL=sqlite+aiosqlite:///data/database/grammi.db
```

* Asegúrate de no usar comillas antes de tu token («, «,» o cualquier otro).
* Coloca el archivo .env en la misma carpeta que dockerfile.

5. **Ejecutar el contenedor Docker**

Deberás proporcionar tu token de bot de Telegram como una variable de entorno.

```bash
# Modo de producción (entorno Windows)
docker run --env-file .env -v ${PWD}/data:/app/data -d grammi-app

# Modo de depuración (entorno Windows)
docker run --env-file .env -v ${PWD}/data:/app/data --rm -it grammi-app /bin/bash
```

## ⚙️ Uso

Próximamente

## 📄 Estructura del proyecto

``` texto
grammi/
├── src/ | 📂 Directorio del código fuente
│ ├── api/ |
| |
│ ├── bot/ |
│ │ ├── core/ |
│ │ │ ├── aiobot.py |
│ │ │ ├── localization.py |
│ │ │ └── t_cc.py | actual
Excluido
| | |
│ │ ├── features/ |
│ │ │ ├── onboarding/ | 🏭 Feature Ciclo de vida en producción
│ │ │ │ ├── locales/ |
│ │ │ │ │ └── en.json |
│ │ │ │ │
│ │ │ │ ├── __init__.py |
│ │ │ │ └── start_handler.py | │ │ │ │ └── start_router.py |
│ │ │ │
│ │ │ ├── imgupload/ | 🏭 Función en el ciclo de producción
│ │ │ │ ├── locales/ |
│ │ │ │ │ └── en.json |
│ │ │ │ │
│ │ │ │ ├── __init__.py | │ │ │ │ └── imgupload_callback.py |
│ │ │ │ └── imgupload_handler.py |
│ │ │ │ └── imgupload_router.py |
│ │ │ │
│ │ │ ├── imgbw/ | 🔥🚧 Nueva función. En desarrollo.
│ │ │ │ ├── locales/ |
│ │ │ │ │ └── en.json | │ │ │ │ │
│ │ │ │ ├── __init__.py |
│ │ │ │ └── imgbw_callback.py |
│ │ │ │ └── imgbw_handler.py |
│ │ │ │ └── imgbw_router.py |
│ │ │ │
│ │ │ └── __init-_.py |
| | |
│ │ ├── middleware/ | │ │ │ ├── cc_middleware.py | actualmente excluido
│ │ │ └── db_middleware.py |
| | |
│ │ └── services/ |
| |
│ └── database/ |
│ ├── __init__.py |
│ ├── db_adapter.py |
│ └── models.py |
│
├── .dockerignore | 🐳 Configuración de Docker para la contenedorización
├── alembic.ini | ├── main.py | 🚀 Punto de entrada principal de la aplicación bot
├── grammi.dockerfile
└── .env
```

## ☕ Apoya mi trabajo

[![Invítame a un café](https://img.shields.io/badge/Buy%20me%20a%20coffee-yellow?logo=kofi)](https://buymeacoffee.com/max.v.zaikin)
[![Dona](https://img.shields.io/badge/Donate-orange?logo=paypal)](próximamente)

Si este proyecto te resulta útil o valoras mi compromiso con el desarrollo ético, ¡considera invitarme a un café o hacer una donación!

Tu apoyo me ayuda a seguir trabajando en proyectos como este y a contribuir a un entorno online positivo. 🙏

No olvides:

- ⭐ Dale a este proyecto una estrella en GitHub
- 👍 Dale a "Me gusta" y compártelo si te resulta útil
- 👔 Conéctate conmigo en [LinkedIn](https://www.linkedin.com/in/maxzaikin)
- 📢 Suscríbete a mi [canal de Telegram](https://t.me/makszaikin) para estar al día de las novedades y las últimas noticias

## 🕊️ Mi visión para un Telegram más seguro

Creo en el poder de Telegram para la comunicación positiva y la creación de comunidad. A través de este proyecto, busco explorar maneras de contribuir a un ecosistema de Telegram más seguro y confiable. Me comprometo a desarrollar herramientas y promover prácticas que ayuden a los usuarios a mantenerse seguros e informados.