from Framework.WhatsappBase import WhatsappBase as wb

wb.main(__name__, __file__)

class FAQSPrepaTec(wb):
    
   def test_FAQSPlanesAnteriores(self):
      self.probarPreguntasFrecuentes("licenciaturaPlanesAnteriores","1")