
from datetime import datetime
from sqlite3 import Connection
from config.email import EmailService
# llama a la libreria y trae su objecto connection

def getUser(email:str,con:Connection):
    cursor = con.cursor()
    query = "select * from user where email = ?"
    result= cursor.execute(query,email)
    data= result.fetchone()
    return data

def Login(email:str, password:str, conn:Connection):
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM usuarios_sistema where email = ?"
        result = cursor.execute(query,(email,))
        result = result.fetchone()
        emailVerified = result[1]
        passwordVerified = result[2]
        typeUser = result[5]
        if password != passwordVerified:
            return False
        return {
            "user": emailVerified,
            "type_user": typeUser,
            "login": True
        }

        
    except Exception as e:
        print(e)
def WelcomeUser(email: str, emailService: EmailService):
    try:
        subject = "Acceso al Sistema Inmobiliario DATUX"
        message = (
            f"Hola {email},\n\n"
            f"Tu inicio de sesión fue exitoso.\n"
            f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "DATUX - Sistema Inmobiliario"
        )
        emailService.send_email(email, subject, message)
    except Exception as e:
        print("e", e)
    
#marco.diaz@sistema.com