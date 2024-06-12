from POM.tec_bots.MiTec import MiTecBase
import allure as AL

MiTecBase.main(__name__, __file__)

class RediseñoTelefoniaMovil_AI01_HU5765(MiTecBase):
    #  pytest BotColaboradores_PPRD_Smoke.py --alluredir allure-results
    #  allure generate --single-file allure-results --clean
    
    @AL.title("AD Rediseño Telefonia móvil")
    @AL.description("Verifica que el rediseño de telefonia movil se encuentre funcionando")
    @AL.tag("Functional")
    @AL.severity(AL.severity_level.MINOR)
    @AL.label("Tester", "Ismael Camacho")
    @AL.story("AI01-5765")
    def test_PreguntaFrecuente1SGMM(self):
      timeout = 4
      self.abrirBot()
      self.darClickOpcion("Telefonía móvil",timeout)
      self.assertEqual(self.darClickOpcion("Conoce tu plan",timeout,3),"Fecha límite de pago:")
      self.darClickOpcion("Regresar",timeout)
      self.assertEqual(self.darClickOpcion("Mi consumo",timeout,2),"$399.00")
