class WhatsappLocators():
    #URL
    whatsappUrl = "https://web.whatsapp.com"
    #Localizadores
    tecbotdevTitle = "//span[contains(string(), 'Tecbotdev')]"
    sendMessageTextBox = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]' #"div[tabindex='10']"
    threeDotsIconConversation = "//*[@id='main']/header/div[3]/div/div[2]/div/div/span"
    threeDotsIcon = "//span//span[@data-icon='menu']"
    vaciarButton = "//div[contains(text(),'Vaciar')]"
    cerrarSesionButton = "//div[contains(text(),'Cerrar sesión')]"
    hoyLabel = "//span[contains(text(),'HOY')]"
    #Mensajes
    mensajePerfil = "//span[contains(string(), 'escribe el número que mejor corresponda')]"
    mensajeNivelAcademico = "//span[contains(string(), 'nivel académico')]"
    mensajeTema = "//span[contains(string(), 'tema de tu interés')]"
    mensajeEscribePregunta = "//div[contains(string(), 'un solo mensaje')]"
    mensajePlanAcademico = "//div[contains(string(), 'plan educativo')]"
    mensajeModeloEducativo = "//div[contains(string(), 'Elige tu modelo educativo')]"
    mensajeFAQ = "//div[contains(string(), 'preguntas frecuentes:')]"
    mensajeRegresar = "//div[contains(string(), 'Regresar al menú anterior')]"
    mensajeDisculpa = "//div[contains(string(), 'Todavía no puedo responder esta consulta.')]"
    #ArraysAlumnos
    prepaTec = ["1" , "1"]
    licenciaturaPlanesAnteriores = ["1", "2", "1"]
    tec21 = ["1", "2", "1"]
    posgrado = ["1" , "3"]
    futurosAlumnos = ["1", "4"]
    prepaNet = ["1", "5"]
    colaboradores = ["5"]
    #ArraysPreguntas
    questions = ["1","2","3","4","5"]
    
class MiTecLocators():
    #URL
    miTecPPRDURL = "https://mitecpprd.itesm.mx/"
    #Localizadores
    userNameField_MiTec = "#Ecom_User_ID"
    passWordField_MiTec = "#Ecom_Password"
    ingresarButton_MiTec = "#submitButton"
    #VentanaNuevaVersionMiTec
    cerrarButton_VentanaMiTec = "button:nth-child(1) span:nth-child(2)"
    masTardeButton_VentanaMiTec = "button[class='btn btn-secondary']"
    botButton = "#saludo_bot_drag > div.saludo_bot_generico.saludo_bot_cero"
    """IMPORTANTE MENSAJES RECIBIDOS"""
    mensajesAzules=".ac-container.ac-adaptiveCard"
    textoMensajeRecibido = "//div[@class='ac-textBlock']/p"
    opciones = "button[aria-label='PLACEHOLDER']"
    menuInicialColaboradores = ["mis Seguros","Credencial institucional","mis Vales de despensa","Constancia de Situación Fiscal SAT","Equipo de cómputo","mi Cuenta bancaria","Telefonía móvil","Datos de tu generalista","Guías y lineamientos","Otros Temas"]
    regresarMensaje_Button = "button[aria-label='Regresar']"
    abrirBot_Button = "saludo_bot_drag > div.saludo_bot_generico.saludo_bot_cero > div:nth-child(2)"
    #Mensajes
    #Arrays
    ejemplo = "si"
    
class GPTPortalLocators():
    ejemplo = "si"
    
class SkillStudioLocators():
    #URL
    skillStudioURL = "https://tecgpt-pprd.azurewebsites.net/"
    #Localizadores
    userNameField = "Ecom_User_ID"
    passWordField = "Ecom_Password"
    submitButton = "submitButton"
    """Locators HomePage"""
    nuevo_Button = "//div[2]/app-home/div/button"
    """Locators nuevoSkill"""
    imagen = "img[src='https://tecgpt0grl0dev0stg0trf.blob.core.windows.net/skillstudioicons/agregar.png']"
    icono = "//img[@title='Cara']"
    titulo_TextBox = "#Titulo"
    descripcion_TextBox = "#floatingTextarea"
    continuar_Button1 = "div[class='flex py-4 ng-star-inserted'] p-button[class='p-element boton-continuar'] span[class='p-button-label ng-star-inserted']"
    continuar_Button2 = "div[id='pn_id_4_1_content'] p-button[class='p-element boton-continuar'] span[class='p-button-label ng-star-inserted']"
    continuar_Button3 = "div[id='pn_id_4_2_content'] p-button[class='p-element boton-continuar'] span[class='p-button-label ng-star-inserted']"
    etiqueta_TextBox = "input[placeholder='Etiqueta en formulario']"
    comando_TextBox = "//textarea[@placeholder='Comando para modelo generativo']"
    agregarCampo_Button = "//button[@class='btn btn btn-outline-secondary']"
    tipoCampo_Dropdown = '//*[@id="cdk-drop-list-0"]/div[2]/div[3]/div/select'
    ejecutarSkill = "//app-card[contains(.,'TEXTOEJEMPLO')]//div[1]//div[2]//span[3]"
    editarSkill = "//app-card[contains(.,'TEXTOEJEMPLO')]//div[1]//div[2]//span[4]"
    editorCodigoSkrill = "textarea"#.monaco-mouse-cursor-text"
    lineaEditorCodigoSkrill = ".view-line"
    guardar_Button = ".btn.btn-primary"
    textoResumir_TextBox = '/html[1]/body[1]/app-root[1]/main[1]/div[2]/ng-component[1]/div[1]/div[1]/div[1]/adaptive-card[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/textarea[1]'
    vamosButton = "button[title='¡Vamos!']"
    resultado= ".result.ng-star-inserted"
    warning_Text = "//div[@class='warning-section ng-star-inserted']//li[@class='ng-star-inserted']"#"li[class='ng-star-inserted']"
    error_Text = "//div[@class='error-section ng-star-inserted']//li[@class='ng-star-inserted']"
    #CodeSnippets
    faltaCreativity_Warning = "#SKILL_DATA\nskpy.skill_config(\n    name=\"Prueba dia 3\",\n    description=\"Escribe la descripci\xF3n de tu Skrill\",\n    version=\"0.0.1\",\n    url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\"\n)\n\n#DEFINE_THE_MODEL\n\nm_gpt35 = model(name='gpt3.5')\n\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]\n" # type: ignore
    faltaImage_Warning = "#SKILL_DATA\n\nskpy.skill_config(\n    name=\"Prueba dia 3\",\n    description=\"Escribe la descripci\xF3n de tu Skrill\",\n    version=\"0.0.1\"\n)\n\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\ntexto = \"Este es un texto de prueba para resumir.\"\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]\nprint(output)"
    faltaInputs_Error = "#SKILL_DATA\nskpy.skill_config(\n    name=\"Prueba dia 3\",\n    description=\"Escribe la descripci\xF3n de tu Skrill\",\n    version=\"0.0.1\",\n    url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\"\n)\n\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n\n#DEFINE_THE_INPUTS\nprint(\"Advertencia: Falta definir el par\xE1metro 'inputs'\")\n\n#VARIABLES_TO_USE\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]\nprint(output)"
    faltaDescription_Error = "#SKILL_DATA\n\nskpy.skill_config(\n    name=\"Prueba dia 3\",\n    version=\"0.0.1\",\n    url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\"\n)\n\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLEES_TO_USE\n\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]\n"
    faltaVersion_Warning = "#SKILL_DATA\n\nskpy.skill_config(\n    name=\"Prueba dia 3\",\n    description=\"Escribe la descripci\xF3n de tu Skrill\",\n    url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\"\n)\n\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\n\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]"
    faltaName_Error = "#SKILL_DATA\n\nskpy.skill_config(\n    description=\"Escribe la descripci\xF3n de tu Skrill\",\n    version=\"0.0.1\",\n    url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\"\n)\n\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\n\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]"
    creativityIncorrecto_Warning ="#SKILL_DATA\nskpy.skill_config(name=\"Escribe el nombre de tu Skrill\",\n                  description=\"Escribe la descripci\xF3n de tu Skrill\",\n                  version=\"0.0.1\",\n                  url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\")\n \n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity=1.7)  \n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\nprompt = f\"\"Dame el resumen del siguiente texto {texto}\"\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]"
    faltaPrompt_Error = "#SKILL_DATA\nskpy.skill_config(name=\"Escribe el nombre de tu Skrill\",\n                  description=\"Escribe la descripci\xF3n de tu Skrill\",\n                  version=\"0.0.1\",\n                  url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\")\n \n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\n\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(m_gpt35)  \n#DEFINE_THE_OUTPUT\noutput = [result]"
    creativityArribaDe1_Error = "#SKILL_DATA\nskpy.skill_config(name=\"Escribe el nombre de tu Skrill\",\n                  description=\"Escribe la descripci\xF3n de tu Skrill\",\n                  version=\"0.0.1\",\n                  url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\")\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='1.5')  \n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt, m_gpt35)\n#DEFINE_THE_OUTPUT\noutput = [result]\n"
    faltaParametroModel_Error = "#SKILL_DATA\nskpy.skill_config(name=\"Escribe el nombre de tu Skrill\",\n                  description=\"Escribe la descripci\xF3n de tu Skrill\",\n                  version=\"0.0.1\",\n                  url_image=\"https://tecgpt0grl0prod0stg.blob.core.windows.net/imagenes-modelos/MOD_POST_REDES_SOCIALES.svg\")\n#DEFINE_THE_MODEL\nm_gpt35 = model(name='gpt3.5', creativity='0.7')\n#DEFINE_THE_INPUTS\ninputs = [{'texto':'Dame el texto a resumir'}]\n#VARIABLES_TO_USE\nprompt = f\"Dame el resumen del siguiente texto {texto}\"\n#EXECUTE_THE_SKILL\nresult = skpy.skill_exec_prompt(prompt) \n#DEFINE_THE_OUTPUT\noutput = [result]\n"