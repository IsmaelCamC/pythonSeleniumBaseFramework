from Resources.Locators import SkillStudioLocators as SSLocators
from Resources.Locators import MiTecLocators as MTLocators
from Resources.AbstractComponents import Utilities
import pytest as PT
import allure as AL
import sys

class BaseTestCase(Utilities):
    
    @AL.title("Carga de la clase base.")
    def setUp(self):
        super().setUp()
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>

    @AL.title("Cierre de la clase base y generacion de reporte.")
    def tearDown(self):
        self.wait(1)
        callerClass = self.__class__.__name__
        callerClass.replace('.','')
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"
        if self.has_exception():
            self.saveScreenshot(callerClass,callerClass)
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            self.saveScreenshot(callerClass,callerClass)
            #print(get_some_info())
            pass
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        super().tearDown()     
    
    
    #Metodos para loguearse en cualquiera de los proyectos 
    AL.step("Inicio de sesion con cuenta de tec en Microsoft.") 
    def loginMicrosoft(self,username, password:str):
        self.open(SSLocators.skillStudioURL)
        self.send_keys(SSLocators.userNameField,username,"id")
        self.send_keys(SSLocators.passWordField,password,"id")
        self.click(SSLocators.submitButton,"id")
     
    AL.step("Inicio de sesion con cuenta del tec en MiTec.")    
    def loginMiTec(self):
        self.open(MTLocators.miTecPPRDURL)
        self.send_keys(MTLocators.userNameField_MiTec,"L01096586@pprd.tec.mx")
        self.send_keys(MTLocators.passWordField_MiTec,"Mariojuache1.")
        self.click(MTLocators.ingresarButton_MiTec)
        self.click(MTLocators.cerrarButton_VentanaMiTec,timeout=25)
        self.click(MTLocators.masTardeButton_VentanaMiTec,timeout=25)
        self.click(MTLocators.botButton)
        
    
