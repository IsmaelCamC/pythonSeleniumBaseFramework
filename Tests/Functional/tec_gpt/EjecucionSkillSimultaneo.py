from POM.tec_gpt.SkillStudio_Base import SkillStudioTest as SST
import allure as AL
SST.main(__name__, __file__)

class EjecucionSkillSimultaneo(SST):
  #pytest '../tecvenv/Tests/Functional/tec_gpt/EjecucionSkillSimultaneo.py' --alluredir allure-results -n 5
    texto = "Un agujero negro es un cuerpo celeste con un campo gravitatorio tan fuerte que ni siquiera la radiación electromagnética puede escapar de su proximidad."
    skillName = "Prueba dia 3"
    
    @AL.title("Ejecucion Skill Simultaneo Worker 1")
    def test_ejecutarSkill_P1(self):
       self.ejecutarSkill("L01096586@pprd.tec.mx","Mariojuache1.",EjecucionSkillSimultaneo.skillName,EjecucionSkillSimultaneo.texto) 
    
    @AL.title("Ejecucion Skill Simultaneo Worker 2")
    def test_ejecutarSkill_P2(self):
      self.ejecutarSkill("L01096586@pprd.tec.mx","Mariojuache1.",EjecucionSkillSimultaneo.skillName,EjecucionSkillSimultaneo.texto)
    
    @AL.title("Ejecucion Skill Simultaneo Worker 3")  
    def test_ejecutarSkill_P3(self):
      self.ejecutarSkill("L01096586@pprd.tec.mx","Mariojuache1.",EjecucionSkillSimultaneo.skillName,EjecucionSkillSimultaneo.texto)
    
    @AL.title("Ejecucion Skill Simultaneo Worker 4")  
    def test_ejecutarSkill_P4(self):
      self.ejecutarSkill("L01096586@pprd.tec.mx","Mariojuache1.",EjecucionSkillSimultaneo.skillName,EjecucionSkillSimultaneo.texto)
    
    @AL.title("Ejecucion Skill Simultaneo Worker 5")  
    def test_ejecutarSkill_P5(self):
      self.ejecutarSkill("L01096586@pprd.tec.mx","Mariojuache1.",EjecucionSkillSimultaneo.skillName,EjecucionSkillSimultaneo.texto)
      	

	
