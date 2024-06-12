from POM.tec_gpt.SkillStudio_Base import SkillStudioTest as SST
from Resources.Locators import SkillStudioLocators as SSLocators
import allure as AL
SST.main(__name__, __file__)

class AnalizadorSintactico_Funcional(SST):
    username = "L01096586@pprd.tec.mx"
    password = "Mariojuache1."
    skillName = "Prueba dia 3"
    
    AL.title("El parametro creativity no se encuentra.")
    def test_faltaCreativity_Warning(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "warning",
                                     SSLocators.faltaCreativity_Warning);
        self.assert_equal(resultado,
                          "Warning: El modelo 'gpt3.5' no cuenta con el parámetro opcional creativity");
""""
    AL.title("No se encuentra el parámetro opcional 'url_image' dentro de la configuración del Skill")
    def test_faltaImage_Warning(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "warning",
                                     SSLocators.faltaImage_Warning);
        self.assert_equal(resultado,
                          "No se encuentra el parámetro opcional 'url_image' dentro de la configuración del Skill");
        
    AL.title("Error no manejado - Falta el parametro inputs.")
    def test_faltaInputs_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "error",
                                     SSLocators.faltaInputs_Error);
        self.assert_equal(resultado,
                          "Lamentamos el inconveniente. Se ha encontrado un error no reconocido. "+
                          "Por favor, verifica tu código. Ten en cuenta que estamos en fase beta, "+
                          "por lo que aún estamos perfeccionando nuestro sistema y puede haber situaciones no previstas.");

    AL.title("Error no manejado - Falta el parametro description.")
    def test_faltaDescription_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "error",
                                     SSLocators.faltaDescription_Error);
        self.assert_equal(resultado,
                          "Lamentamos el inconveniente. Se ha encontrado un error no reconocido. "+
                          "Por favor, verifica tu código. Ten en cuenta que estamos en fase beta, "+
                          "por lo que aún estamos perfeccionando nuestro sistema y puede haber situaciones no previstas.");       

    AL.title("Advertencia - Falta el parametro version en la configuracion del Skrill.")
    def test_faltaVersion_Warning(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "warning",
                                     SSLocators.faltaVersion_Warning);
        self.assert_equal(resultado,
                          "No se encuentra el parámetro opcional 'version' dentro de la configuración del Skill");

    AL.title("Error - Falta el parametro name en la configuracion del Skrill.")
    def test_faltaName_Warning(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                     AnalizadorSintactico_Funcional.password,
                                     AnalizadorSintactico_Funcional.skillName,
                                     "error",
                                     SSLocators.faltaName_Error);
        self.assert_equal(resultado,
                          "No se encuentra el parámetro obligatorio 'name' dentro de la configuración del Skill(skill_config)");
         
    AL.title("Error - Parametro creativity arriba de 1 en la configuracion del Skrill.")
    def test_creativityIncorrecto_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                 AnalizadorSintactico_Funcional.password,
                                 AnalizadorSintactico_Funcional.skillName,
                                 "error",
                                 SSLocators.creativityIncorrecto_Warning);
        self.assert_equal(resultado,
                      "Lamentamos el inconveniente. Se ha encontrado un error no reconocido. Por favor, verifica tu código. Ten en cuenta que estamos en fase beta, por lo que aún estamos perfeccionando nuestro sistema y puede haber situaciones no previstas.");  
    
        AL.title("Error - Falta variable PROMPT en configuracion del Skrill.")
    def test_faltaPrompt_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                 AnalizadorSintactico_Funcional.password,
                                 AnalizadorSintactico_Funcional.skillName,
                                 "error",
                                 SSLocators.faltaPrompt_Error);
        self.assert_equal(resultado,
                      "Lamentamos el inconveniente. Se ha encontrado un error no reconocido. Por favor, verifica tu código. Ten en cuenta que estamos en fase beta, por lo que aún estamos perfeccionando nuestro sistema y puede haber situaciones no previstas.");  
                
        AL.title("Error - Creativity arriba de 1 en configuracion del Skrill.")
    def test_creativityArribaDe1_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                 AnalizadorSintactico_Funcional.password,
                                 AnalizadorSintactico_Funcional.skillName,
                                 "error",
                                 SSLocators.creativityArribaDe1_Error);
        self.assert_equal(resultado,
                      "Error de sintaxis: En la declaración de tu modelo 'gpt3.5' el parámetro creativity no tiene un valor permitido, solo se aceptan números positivos entre 0-1 y se proporciono 1.5");  
        
        AL.title("Error - Falta parametro Model en configuracion del Skrill.")
    def test_faltaModel_Error(self):
        resultado = self.validarAnalizadorSintactico(AnalizadorSintactico_Funcional.username,
                                 AnalizadorSintactico_Funcional.password,
                                 AnalizadorSintactico_Funcional.skillName,
                                 "error",
                                 SSLocators.faltaParametroModel_Error);
        self.assert_equal(resultado,
                      "Lamentamos el inconveniente. Se ha encontrado un error no reconocido. Por favor, verifica tu código. Ten en cuenta que estamos en fase beta, por lo que aún estamos perfeccionando nuestro sistema y puede haber situaciones no previstas.");  
"""