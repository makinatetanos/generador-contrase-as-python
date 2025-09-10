# Generador de Contraseñas con Flet

Una sencilla aplicación de escritorio para generar contraseñas seguras, creada con Python y Flet.

## Características

*   Genera contraseñas de longitud personalizable (entre 8 y 32 caracteres).
*   Permite incluir/excluir caracteres: minúsculas, mayúsculas, números y símbolos.
*   Botón para copiar la contraseña generada al portapapeles.
*   Interfaz de usuario limpia y sencilla.

## Captura de Pantalla

*(Aquí puedes añadir una captura de pantalla de la aplicación)*

![Generador de Contraseñas](src/icon.png)

## Cómo Empezar

Sigue estos pasos para ejecutar la aplicación en tu máquina local.

### Prerrequisitos

*   Python 3.7 o superior

### Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/makinatetanos/generador-contrase-as-python.git
    cd generador-contrase-as-python
    ```

2.  **Crea y activa un entorno virtual:**

    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
flet run src/main.py
```

## Dependencias

*   **flet**: El framework utilizado para construir la interfaz de usuario.
