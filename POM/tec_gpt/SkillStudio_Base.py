from selenium.webdriver.common.keys import Keys
from Resources.Locators import SkillStudioLocators as SSLocators
from selenium.common.exceptions import NoSuchElementException
from Framework.BaseTest import BaseTestCase
import codecs
import inspect
import time
import allure as AL

class SkillStudioTest(BaseTestCase):
    
    @AL.step("Validacion en el analizador sintactico")
    def validarAnalizadorSintactico(self, username, password,skillName,tipo:str, texto:str = "Lorem ipsum"):
      self.loginMicrosoft(username,password)
      try:
          self.editarSkill(skillName)
          self.click(SSLocators.lineaEditorCodigoSkrill)
          self.send_keys(SSLocators.editorCodigoSkrill,
                         Keys.COMMAND + "a")
          self.send_keys(SSLocators.editorCodigoSkrill,
                         Keys.DELETE)
          self.send_keys(SSLocators.editorCodigoSkrill, codecs.decode(texto, 'unicode_escape'))
          self.click(SSLocators.guardar_Button)
      except Exception:
          self.fail("Test failed.")
     #print(self.__class__.__name__)
      if "warning" in tipo:
          self.wait_for_element(SSLocators.warning_Text,"xpath")
          return self.get_text(SSLocators.warning_Text,"xpath")
      if "error" in tipo:
          self.wait_for_element(SSLocators.error_Text,"xpath")
          return self.get_text(SSLocators.error_Text,"xpath")
    
  #-----------------------------------------------------------------------------------#

    @AL.step("Editar un Skrill")
    def editarSkill(self,skillName):
        self.click(SSLocators.editarSkill.replace("TEXTOEJEMPLO",skillName))
  
    @AL.step("Ejecucion del skill que se recibe como parametro.")
    def ejecutarSkill(self, username, password,skillName, texto:str = "Lorem ipsum"):
        #Para la ejecución de este Script se medirá el tiempo de ejecución
        inicio = time.time()
        try:
            self.loginMicrosoft(username,password)
            self.click(SSLocators.ejecutarSkill.replace("TEXTOEJEMPLO",skillName))
            #self.click(".ac-input-container")
            self.wait_for_element_clickable(SSLocators.textoResumir_TextBox,timeout=30)
            self.clear(SSLocators.textoResumir_TextBox)
            self.send_keys(SSLocators.textoResumir_TextBox,texto)
            self.click(SSLocators.vamosButton)
            self.assert_non_empty_text(SSLocators.resultado,timeout=60)
        except NoSuchElementException:
            self.fail("Test failed.")
        fin = time.time()
        print(fin-inicio)
        
    @AL.step("Creacion de un skill nuevo.")
    def nuevoSkill(self,username, password, titulo="Ejemplo", descripcion="Ejemplo", etiqueta="Prueba", comando:str="Prueba" ):
        continuar_Buttons = [SSLocators.continuar_Button1,SSLocators.continuar_Button2,SSLocators.continuar_Button3]
        try:
            self.loginMicrosoft(username, password)
            self.click(SSLocators.nuevo_Button,timeout=60)
            self.click(SSLocators.imagen)
            self.click(SSLocators.icono)
            self.send_keys(SSLocators.titulo_TextBox,titulo)
            self.send_keys(SSLocators.descripcion_TextBox,descripcion)
            self.click(continuar_Buttons[1])
            self.click(continuar_Buttons[2])
            self.click(SSLocators.agregarCampo_Button,"xpath")
            self.send_keys(SSLocators.etiqueta_TextBox,etiqueta)
            self.send_keys(SSLocators.comando_TextBox,comando)
            self.select_option_by_text(SSLocators.tipoCampo_Dropdown,"Texto","xpath")
            self.click(continuar_Buttons[3])
        except Exception:
            self.fail("Test failed")

# Codigo para localizar un elemento activo
 #test = self.driver.switch_to.active_element  
 #print(test.get_attribute('outerHTML'))