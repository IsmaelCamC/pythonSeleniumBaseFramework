from Framework.BaseTest import BaseTestCase
from selenium.webdriver.common.keys import Keys
from Resources.Locators import WhatsappLocators as wp
from selenium.common.exceptions import NoSuchElementException

#BaseCase.main(__name__, __file__)

class WhatsappBase(BaseTestCase):
    """
    def probarPreguntasFrecuentes(self, audiencia, tema:str):
        audiencia = self.validarAudiencia(audiencia)
        self.open(wp.whatsappUrl)
        self.click("xpath", wp.tecbotdevTitle, 80)
        self.vaciarChat()
        for i in range(len(wp.questions)):
            try: 
                self.empezarChat()
                self.enviarMensaje(audiencia[0], wp.mensajeNivelAcademico)
                if len(audiencia)>2:
                    self.enviarMensaje(audiencia[1],wp.mensajeModeloEducativo)
                    self.enviarMensaje(audiencia[2], wp.mensajeTema)
                else:
                    self.enviarMensaje(audiencia[1], wp.mensajeTema)
                self.enviarMensaje(tema,wp.mensajeFAQ)
                self.hacerPregunta(i,tema)
                self.vaciarChat()
            except NoSuchElementException:
                print("Surgio un error tratando de encontrar un elemento.")
        self.vaciarChat()
        self.logoutWhatsapp()        
        """
        
    def probarPreguntasFrecuentes(self, audiencia, tema:str):
        audiencia = self.validarAudiencia(audiencia)
        self.open(wp.whatsappUrl)
        self.click("xpath", wp.tecbotdevTitle, 80)
        self.vaciarChat()
        for i in range(len(wp.questions)):
            try: 
                self.empezarChat()
                match len(audiencia):
                    case 3:
                        self.enviarMensaje(audiencia[0], wp.mensajePerfil)  
                        self.enviarMensaje(audiencia[1],wp.mensajeModeloEducativo)
                        self.enviarMensaje(audiencia[2], wp.mensajeTema)
                    case 2:
                        self.enviarMensaje(audiencia[0], wp.mensajePerfil)  
                        self.enviarMensaje(audiencia[1], wp.mensajeTema)
                    case 1:
                        self.enviarMensaje(audiencia[0], wp.mensajeTema)
                        pass
                self.enviarMensaje(tema,wp.mensajeFAQ)
                self.hacerPregunta(i,tema)
                self.vaciarChat()
            except NoSuchElementException:
                print("Surgio un error tratando de encontrar un elemento.")
        self.vaciarChat()
        self.logoutWhatsapp()        
        
#--------------------------------------------------------------------------------------#

    def enviarMensaje(self, sentMessage, receivedMessage):
        self.click(wp.sendMessageTextBox)
        self.type(wp.sendMessageTextBox, text=sentMessage)
        self.send_keys(wp.sendMessageTextBox, Keys.ENTER)
        self.wait_for_element_visible(by="xpath", selector=receivedMessage, timeout=30)
        
    def empezarChat(self):
        self.send_keys(wp.sendMessageTextBox, text="Hola")
        self.send_keys(wp.sendMessageTextBox, Keys.ENTER)
        self.wait(5)

    def vaciarChat(self):
        self.click(by="xpath",selector=wp.threeDotsIconConversation,timeout=30)
        self.click(by="xpath",selector=wp.vaciarButton,timeout=30)
        self.click(by="xpath",selector=wp.vaciarButton,timeout=30)
        self.wait_for_element_visible(wp.hoyLabel)

    def hacerPregunta(self,index,tema):
        self.type(wp.sendMessageTextBox, wp.questions[index])
        self.send_keys(wp.sendMessageTextBox, Keys.ENTER)
        self.wait(20)
        self.saveScreenshot("tema_"+tema+"pregunta_"+wp.questions[index],self.__class__.__name__)
        #self.save_screenshot(self.__class__.__name__+"_tema"+tema+"_pregunta"+wp.questions[index])
        self.wait(10)

    def logoutWhatsapp(self):
        self.click("xpath", wp.threeDotsIcon)
        self.click("xpath", wp.cerrarSesionButton, 30)
        self.click("xpath", wp.cerrarSesionButton, 30)
    
    def validarAudiencia(self, audiencia):
        match audiencia:
            case "prepaTec":
                audiencia = wp.prepaTec
            case "posgrado":
                audiencia = wp.posgrado
            case "futurosAlumos":
                audiencia = wp.futurosAlumnos
            case "prepaNet":
                audiencia = wp.prepaNet
            case "planesAnteriores":
                audiencia = wp.licenciaturaPlanesAnteriores
            case "tec21":
                audiencia = wp.tec21
            case "colaboradores":
                audiencia = wp.colaboradores
        print(audiencia)
        return audiencia
        
        
    """   
    def knowledgeBasesWhatsapp(self, audiencia):
        # En este punto se debe llamar una función que lea un archivo de excel para cargar las preguntas
        self.open(wp.whatsappUrl)
        self.click("xpath", wp.tecbotdevTitle, 80)
        self.vaciarChat()
        try: 
            match audiencia:
                case "prepa":
                    for i in range(len(wp.questions)):
                        self.enviarMensaje("Hola", wp.mensajePerfil)
                        self.enviarMensaje("1", wp.mensajeNivelAcademico)
                        self.enviarMensaje("1", wp.mensajeTema)
                        self.enviarMensaje("6", wp.mensajeEscribePregunta)
                        self.hacerPregunta(i, audiencia)
                        self.vaciarChat()
                case "tec21":
                    for i in range(len(wp.questions)):
                        self.enviarMensaje("Hola", wp.mensajePerfil)
                        self.enviarMensaje("1", wp.mensajeNivelAcademico)
                        self.enviarMensaje("2", wp.mensajeTema)
                        self.enviarMensaje("2", wp.mensajePlanAcademico)
                        self.enviarMensaje("6", wp.mensajeEscribePregunta)
                        self.hacerPregunta(i, audiencia)
                        self.vaciarChat()
                case "posgrado":
                    for i in range(len(wp.questions)):
                        self.enviarMensaje("Hola", wp.mensajePerfil)
                        self.enviarMensaje("1", wp.mensajeNivelAcademico)
                        self.enviarMensaje("3", wp.mensajeTema)
                        self.enviarMensaje("4", wp.mensajeEscribePregunta)
                        self.hacerPregunta(i, audiencia)
                        self.vaciarChat()
                case "colaboradores":
                    for i in range(len(wp.questions)):
                        self.enviarMensaje("Hola", wp.mensajePerfil)
                        self.enviarMensaje("3", wp.mensajeTema)
                        self.enviarMensaje("6", wp.mensajeEscribePregunta)
                        self.hacerPregunta(i, audiencia)
                        self.vaciarChat()
            self.logoutWhatsapp()   
        except Exception:
            self.vaciarChat()
            self.logoutWhatsapp()
            print("Surgio un error, se vació el chat y se cerró sesion en whatsapp.")
    """    