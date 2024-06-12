import sys
sys.dont_write_bytecode = True

from selenium.webdriver.common.keys import Keys
from Resources.Locators import MiTecLocators as MTLocators
from selenium.common.exceptions import NoSuchElementException
from Framework.BaseTest import BaseTestCase
import allure as AL 


class MiTecBase(BaseTestCase):
    @AL.step("Dar click en la opcion.")
    def darClickOpcion(self, opcion:str, wait:int, message:int=1) -> str:
        """TODO Cambiar las lineas self.wait(wait) por una espera definida para aumentar eficiencia"""
        try:  
            self.wait(wait)
            opcionSeleccionada = MTLocators.opciones.replace("PLACEHOLDER",opcion)
            self.wait_for_element_clickable(opcionSeleccionada)
            self.click(opcionSeleccionada)
            self.wait(wait)
            mensajesRecibidos = self.find_elements(MTLocators.textoMensajeRecibido,"xpath")
            mensaje = mensajesRecibidos[len(mensajesRecibidos)-message].text
            self.wait(wait)
        except NoSuchElementException:
            print("No se recibieron mensajes nuevos.")
        return mensaje
    
#----------------------------------------------------------------#

    @AL.step("Abrir el bot.")
    def abrirBot(self):
        try:
            self.loginMiTec()
            self.click(MTLocators.abrirBot_Button)
        except Exception:
            print("Inicio de sesion fallido.")
    
     
