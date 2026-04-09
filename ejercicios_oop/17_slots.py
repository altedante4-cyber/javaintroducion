from datetime import datetime

class Logger:
    __slots__ = ['mensaje', 'nivel']
    
    def __init__(self, mensaje, nivel="INFO"):
        self.mensaje = mensaje
        self.nivel = nivel
    
    def __str__(self):
        return f"[{self.nivel}] {datetime.now().strftime('%H:%M:%S')} - {self.mensaje}"

logs = [
    Logger("Usuario conectado", "INFO"),
    Logger("Error de autenticación", "ERROR"),
    Logger("Backup completado", "DEBUG")
]

for log in logs:
    print(log)
