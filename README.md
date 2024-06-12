
# Tec Tests

Este repositorio contiene el Framework de pruebas automatizadas de los proyectos de TEC.GPT y TEC.BOTS, construido a partir de las librerías PyTest y SeleniumBase.


## Clases principales

Todas las clases heredan de la clase BaseCase de SeleniumBase, sin embargo las clase principales del framework son AbstractComponents.py, contenida en la carpeta Resources y BaseTest en la carpeta Framework.
AbstractComponents contiene los métodos necesarios para hacer capturas de pantalla necesarias en los reportes de allure que se generan en ejecución. BaseCase hace un override de los métodos TearDown() de BaseTest, inyectando codigo en el cierre de los drivers de Selenium y asi consiguiendo ejecutar código al finalizar y comenzar pruebas, lo que puede servir para hacer logins y logouts de aplicaciones, asi como obtener evidencias de pruebas. 
## Generar un Test
Para generar un test los pasos a seguir son:
1. Generar una clase en la subcarpeta correspondiente del proyecto en la carpeta POM, importando de la clase Locators los localizadores correspondientes.
2. Heredar BaseTestCase en la clase desde Framework.BaseTest.
3. Generar los métodos necesarios para las pruebas, señalizando correctamente los pasos con allure.step.
4. Generar la suite de pruebas, señalizado los métodos con decoradores de allure para garantizar la homogeneidad de los reportes en su generación.