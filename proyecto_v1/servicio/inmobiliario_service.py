from datetime import datetime
def menu_inmobiliario(conn, email_usuario=None, email_service=None):
    """
    Menú/flujo del sistema inmobiliario (TRX IN) según lo visto en clase.
    conn: conexión sqlite3
    email_usuario: email del usuario logueado
    email_service: instancia de EmailService (si la usan)
    """
    if email_usuario and email_service:
        subject = "Ingreso al módulo Sistema Inmobiliario (TRX IN)"
        message = (
            f"Hola {email_usuario},\n\n"
            "Has ingresado al módulo Sistema Inmobiliario (TRX IN).\n"
            f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "DATUX - Sistema Inmobiliario"
        )
        email_service.send_email(email_usuario, subject, message)
    print("\n=== SISTEMA INMOBILIARIO ===")
    print("1) Clientes")
    print("2) Productos (Inmuebles)")
    print("3) TRX IN (Nueva transacción)")
    print("4) Pagos")
    print("5) Documentos")
    print("6) Reportes")
    print("0) Volver")

    op = input("Elige una opción: ")
   
    print(f"Elegiste: {op} (pendiente de implementar)")
