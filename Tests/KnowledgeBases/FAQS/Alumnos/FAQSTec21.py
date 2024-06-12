from Framework.WhatsappBase import WhatsappBase as wb

wb.main(__name__, __file__)

class FAQSPrepaTec(wb):
    
   def test_FAQSTec21(self):
      self.probarPreguntasFrecuentes("tec21","1")