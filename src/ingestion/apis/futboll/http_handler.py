
def manejar_estado_http(status_code):
    """Interpreta el código de estado HTTP de una respuesta."""

    if status_code == 200:
        return "OK: respuesta recibida correctamente"

    elif status_code == 204:
        return "SIN CONTENIDO: no hay datos para procesar"

    elif status_code == 499:
        return "TIMEOUT: la solicitud excedió el tiempo esperado"

    elif status_code == 500:
        return "ERROR DEL SERVIDOR: ocurrió un problema interno"

    else:
        return f"ESTADO NO CONTEMPLADO: HTTP {status_code}"
