from Framework.WhatsappBase import WhatsappBase as wb

wb.main(__name__, __file__)

class FAQSPosgrado(wb):
    
    def test_FAQSPosgrado(self):
        self.probarPreguntasFrecuentes("posgrado","1")