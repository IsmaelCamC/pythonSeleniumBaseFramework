from Framework.WhatsappBase import WhatsappBase as wb

wb.main(__name__, __file__)

class FAQSColaboradores(wb):
    
   def test_FAQSColaboradoresTema1(self):
      self.probarPreguntasFrecuentes("colaboradores","1")
      
   def test_FAQSColaboradoresTema2(self):
      self.probarPreguntasFrecuentes("colaboradores","2")
      
   def test_FAQSColaboradoresTema3(self):
      self.probarPreguntasFrecuentes("colaboradores","3")
      
   def test_FAQSColaboradoresTema4(self):
      self.probarPreguntasFrecuentes("colaboradores","4")
      
   def test_FAQSColaboradoresTema5(self):
      self.probarPreguntasFrecuentes("colaboradores","5")            
