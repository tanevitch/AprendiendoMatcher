import unittest

from matcher import AprendiendoMatcher 


class AprendiendoMatcherTest(unittest.TestCase):
    '''
    La sintaxis de los patrones que tienen que escribir es:  
        [
            [
                { ... :  ... },
                ...
            ]
        ]
    '''

    def test_detectar_basico(self):
        #........................................................................................................#
        oracion= "The gardener fertilizes the infertile soil."
        matcher = AprendiendoMatcher( 
                    # escribir patron que permita identificar el nucleo de la oración
                )
        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion), ["gardener"]
            )
        
        #........................................................................................................#
        #........................................................................................................#

        oracion= "The agricultural engineer fertilizes the infertile soil."
        matcher.setMatcher(
             # escribir patron que permita identificar el nucleo de la oración y su modificador
        )
        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion), ["agricultural engineer", "engineer"]
            )

        #........................................................................................................#
        #........................................................................................................#

        oracion = "The tomato plant produces tomato fruits."
        matcher.setMatcher(
              # escribir patron que permita identificar el nucleo de la oración y su modificador
        )

        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion), ["tomato plant", "plant"]
        )
        
        #........................................................................................................#
        #........................................................................................................#

        oracion1 = "The tomato plant produces tomato fruits."
        oracion2= "The agricultural engineer fertilizes the infertile soil."
        matcher.setMatcher(
              # escribir patron que permita identificar el nucleo de las oraciones y su modificador
        )

        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion1), ["tomato plant", "plant"]
        )
        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion2), ["agricultural engineer", "engineer"]
        )

        #........................................................................................................#
        #........................................................................................................#
        

        oracion = "The tomato plant produces tomato fruits."
        matcher.setMatcher(
              # escribir patron que permita identificar el nucleo de la oración y su modificador, y el objeto y su modificador
        )
        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion), ["tomato plant", "plant", "tomato fruits", "fruits"]
        )

        #........................................................................................................#
        #........................................................................................................#
        
        oracion = "The tomato plant produces tomato fruits."
        matcher.setMatcher(
            # escribir patron que permita identificar el nucleo de la oración y su modificador, y el objeto y su modificador
        )
        self.assertEqual(
                matcher.procesarOracionLenguajeNatural(oracion), ["tomato plant", "tomato fruits"]
        )