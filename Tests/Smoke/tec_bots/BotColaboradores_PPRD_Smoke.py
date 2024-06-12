from POM.tec_bots.MiTec import MiTecBase
import allure as AL

MiTecBase.main(__name__, __file__)

class BotColaboradores_PPRD_Smoke(MiTecBase):
  
    @AL.title("Preguntas frecuentes Colaboradores - VISA ¿Cómo consigo una constancia para trámtiar VISA?")
    @AL.description("Este test verifica que las preguntas frecuentes sobre VISA se encuentren funcionando.")
    @AL.tag("Smoke")
    @AL.severity(AL.severity_level.MINOR)
    @AL.label("Tester", "Ismael Camacho")
    def test_PreguntaFrecuenteVISA(self):
      self.abrirBot()
      self.darClickOpcion("Otros Temas",3)
      self.darClickOpcion("mi Caja de ahorro",3)
      self.darClickOpcion("Regresar",3)
      self.darClickOpcion("mis Constancias",3)
      self.assertEqual(self.darClickOpcion("¿Cómo consigo una constancia para trámtiar VISA?",3),"¡Es muy importante tu opinión!")

    @AL.title("Preguntas Colaboradores - Datos de tu generalista")
    @AL.description("Este test verifica que se obtengan datos de tu generalista.")
    @AL.tag("Smoke")
    @AL.severity(AL.severity_level.MINOR)
    @AL.label("Tester", "Ismael Camacho")
    def test_DatosGeneralista(self):
      self.abrirBot()
      self.darClickOpcion("Datos de tu generalista",3)
      self.darClickOpcion("Regresar",3)
      self.assertEqual(self.darClickOpcion("Datos de tu generalista",3),"¡Es muy importante tu opinión!")

"""  
    @AL.title("Preguntas frecuentes Colaboradores - SGMM ¿Cómo puedo consultar los planes y costos?")
    @AL.description("Este test verifica que las preguntas frecuentes sobre SGMM se encuentren funcionando.")
    @AL.tag("Smoke")
    @AL.severity(AL.severity_level.MINOR)
    @AL.label("Tester", "Ismael Camacho")
    def test_PreguntaFrecuente1SGMM(self):
      self.abrirBot()
      self.darClickOpcion("mis Seguros",3)
      self.darClickOpcion("mis Seguros voluntarios",3)
      self.darClickOpcion("SGMM",3)
      self.darClickOpcion("Preguntas frecuentes",3)
      self.assertEqual(self.darClickOpcion("¿Cómo puedo consultar los planes y costos?",3),"¡Es muy importante tu opinión!")
"""  