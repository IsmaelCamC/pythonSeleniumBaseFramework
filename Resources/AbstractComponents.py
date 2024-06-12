from seleniumbase import BaseCase
from datetime import datetime
import sys
import allure as AL

sys.dont_write_bytecode = True

class Utilities(BaseCase):
    contador = 1
    def saveScreenshot(self, name, path):
        try:
            hoy = obtener_fecha_hora()
            fecha = obtener_fecha()
            path = "../tecvenv/Resources/Screenshots/"+path+"/"+fecha
            screen_name = name+str(Utilities.contador)+"_"+hoy
            self.save_screenshot(screen_name, path)
        except FileExistsError:
            print("El directorio ya existe.")
        AL.attach.file(path+"/"+screen_name+".png",
               "Captura_Resultado",
                AL.attachment_type.PNG)
        Utilities.contador+=1
        
def obtener_fecha_hora():
    ahora = datetime.now()
    fecha_hora_formateada = ahora.strftime("%d_%m_%Y_%H_%M_%S")
    return fecha_hora_formateada

def obtener_fecha():
    ahora = datetime.now()
    fecha_hora_formateada = ahora.strftime("%d_%m_%Y")
    return fecha_hora_formateada