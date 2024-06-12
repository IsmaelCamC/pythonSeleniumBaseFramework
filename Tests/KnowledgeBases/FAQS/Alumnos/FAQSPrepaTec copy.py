from Framework.WhatsappBase import WhatsappBase as wb

wb.main(__name__, __file__)

class FAQSPrepaNet(wb):
    
   def test_FAQSPrepaNet(self):
      self.probarPreguntasFrecuentes("prepaNet","1")