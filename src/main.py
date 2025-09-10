import flet as ft
import random
import string

def main(page: ft.Page):
    """
    Función principal para la aplicación Flet del generador de contraseñas.
    """
    # --- Configuración de la ventana ---
    page.title = "Generador de Contraseñas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 520
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK # Opcional: modo oscuro

    # --- Lógica de la aplicación ---

    def generate_password(e):
        """Genera una nueva contraseña basada en las opciones seleccionadas."""
        length = int(slider_length.value)
        chars = ""
        if check_lower.value:
            chars += string.ascii_lowercase
        if check_upper.value:
            chars += string.ascii_uppercase
        if check_numbers.value:
            chars += string.digits
        if check_symbols.value:
            chars += string.punctuation

        if not chars:
            password_field.value = "¡Selecciona una opción!"
            password_field.error_text = "Debes elegir al menos un tipo de caracter."
        else:
            password = "".join(random.choice(chars) for _ in range(length))
            password_field.value = password
            password_field.error_text = ""
        
        page.update()

    # --- Componentes reutilizables ---
    
    # SnackBar para notificaciones
    page.snack_bar = ft.SnackBar(
        content=ft.Text("¡Contraseña copiada al portapapeles!"),
        duration=2000
    )

    def copy_to_clipboard(e):
        """Copia la contraseña generada al portapapeles."""
        if password_field.value and "¡Selecciona una opción!" not in password_field.value:
            page.set_clipboard(password_field.value)
            page.snack_bar.open = True
            page.update()

    def update_slider_label(e):
        """Actualiza la etiqueta que muestra la longitud de la contraseña."""
        slider_length_label.value = f"Longitud: {int(e.control.value)}"
        page.update()

    # --- Componentes de la Interfaz de Usuario (UI) ---

    password_field = ft.TextField(
        label="Contraseña generada",
        read_only=True,
        password=True,
        can_reveal_password=True,
        expand=True,
        border_color=ft.Colors.BLUE_400
    )

    copy_button = ft.IconButton(
        icon=ft.Icons.COPY,
        on_click=copy_to_clipboard,
        tooltip="Copiar al portapapeles"
    )

    slider_length_label = ft.Text(f"Longitud: 16")
    
    slider_length = ft.Slider(
        min=8,
        max=32,
        divisions=24,
        value=16,
        on_change=update_slider_label,
    )

    check_lower = ft.Checkbox(label="Minúsculas (a-z)", value=True)
    check_upper = ft.Checkbox(label="Mayúsculas (A-Z)", value=True)
    check_numbers = ft.Checkbox(label="Números (0-9)", value=True)
    check_symbols = ft.Checkbox(label="Símbolos (!-$+%)", value=False)

    generate_button = ft.ElevatedButton(
        text="Generar Contraseña",
        on_click=generate_password,
        icon=ft.Icons.SHUFFLE,
        width=350,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor=ft.Colors.BLUE_400,
        color="white"
    )

    # --- Estructura y Diseño de la Página ---

    page.add(
        ft.Column(
            [
                ft.Text("Generador de Contraseñas", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Row(
                    [
                        password_field,
                        copy_button
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                slider_length_label,
                slider_length,
                ft.Text("Opciones:", weight=ft.FontWeight.BOLD, size=16),
                check_lower,
                check_upper,
                check_numbers,
                check_symbols,
                ft.Container(height=20), # Un pequeño espacio
                generate_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            width=350
        )
    )
    
    # Generar una contraseña al iniciar la app
    generate_password(None)

# --- Punto de entrada para ejecutar la aplicación ---
if __name__ == "__main__":
    ft.app(target=main)
