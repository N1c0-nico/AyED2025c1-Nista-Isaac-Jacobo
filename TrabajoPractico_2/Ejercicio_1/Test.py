import unittest
from modules.arbol import ArbolBinarioDB
import numpy as np

class TestColaPrioridad(unittest.TestCase):
    
    def setUp(self):
        self.ArbolBinarioDB = ArbolBinarioDB()
    
    def agregar_claves(self, *args):
        for value in args:
            self.ArbolBinarioDB.agregar(clave=value, valor=2*value)
    
    def tearDown(self):
        pass
    
    def test_busqueda(self):
        claves = [45, 100, 20, 80, 55, 25, 18]
        self.agregar_claves(*claves)
        for clave in claves:
            self.assertEqual( self.ArbolBinarioDB.obtener(clave), 2*clave )        
    
    def test_insercion(self):
        """
        Verifica la insercion binaria tradicional
        """
        self.agregar_claves(45, 100, 20, 80, 10, 110, 50)
        # verifico posicion relativa desde la raiz
        self.assertEqual(self.ArbolBinarioDB.raiz.clave, 45,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.cargaUtil, 90,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoDerecho.clave, 100,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoDerecho.cargaUtil, 200,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoIzquierdo.clave, 20,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoIzquierdo.cargaUtil, 40,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoDerecho.hijoIzquierdo.clave, 80,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoDerecho.hijoIzquierdo.cargaUtil, 160,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoIzquierdo.hijoIzquierdo.clave, 10,
                        "ArbolBinarioDB insertado incorrectamente")
        self.assertEqual(self.ArbolBinarioDB.raiz.hijoIzquierdo.hijoIzquierdo.cargaUtil, 20,
                        "ArbolBinarioDB insertado incorrectamente")
        # verifico ColaPrioridads hojas
        self.assertTrue(self.ArbolBinarioDB.raiz.hijoIzquierdo.hijoIzquierdo.esHoja(), 
                        "ArbolBinarioDB 10 debe ser un ArbolBinarioDB hoja")
        self.assertTrue(self.ArbolBinarioDB.raiz.hijoDerecho.hijoIzquierdo.hijoIzquierdo.esHoja(), 
                        "ArbolBinarioDB 50 debe ser un ArbolBinarioDB hoja")
        self.assertTrue(self.ArbolBinarioDB.raiz.hijoDerecho.hijoDerecho.esHoja(), 
                        "ArbolBinarioDB 110 debe ser un ArbolBinarioDB hoja")
        # verifico ColaPrioridads internos
        self.assertFalse(self.ArbolBinarioDB.raiz.esHoja(), 
                        "ArbolBinarioDB 45 debe ser ArbolBinarioDB interno, no un ArbolBinarioDB hoja")
        self.assertFalse(self.ArbolBinarioDB.raiz.hijoIzquierdo.esHoja(), 
                        "ArbolBinarioDB 20 debe ser ArbolBinarioDB interno, no un ArbolBinarioDB hoja")
        self.assertFalse(self.ArbolBinarioDB.raiz.hijoDerecho.esHoja(), 
                        "ArbolBinarioDB 100 debe ser un ArbolBinarioDB interno, no un ArbolBinarioDB hoja")
        self.assertFalse(self.ArbolBinarioDB.raiz.hijoDerecho.hijoIzquierdo.esHoja(), 
                        "ArbolBinarioDB 80 debe ser un ArbolBinarioDB interno, no un ArbolBinarioDB hoja")
    

    def test_operador_contains(self):
        """
        Verifica la sobrecarga del operador 'in', que corrobora si
        un elemento está o no en el ArbolBinarioDB
        """
        self.agregar_claves(45, 100, 20, 80, 10)
        self.assertTrue( 100 in self.ArbolBinarioDB )
        self.assertTrue( 10 in self.ArbolBinarioDB )
        self.assertFalse( 1 in self.ArbolBinarioDB )
    
    def test_recorrido(self):
        """
        Para evaluar el recorrido, los elementos del árbol deben 
        recorrerse in-orden al iterar sobre él en un ciclo for
        """
        # tratamos de evitar tener claves repetidas
        claves = list(set(np.random.randint(0,1000, (100,))))
        np.random.shuffle(claves)
        self.agregar_claves(*claves)
        # comparo recorrido del árbol con lista ordenada
        claves = np.sort(claves)
        for n, item in enumerate(self.ArbolBinarioDB):
            self.assertEqual(claves[n], item[0])
    
    # def test_eliminacion(self):
    #     """
    #     Verifica los distintos casos de eliminacion en un arbol
    #     """
    #     self.agregar_claves(100, 50, 20, 35, 75, 110, 105, 137, 150, 
    #             145, 25, 170, 80, 120, 22, 125, 108, 79, 115, 130, 60)
    #     # elimino ArbolBinarioDB hoja izquierdo
    #     self.ArbolBinarioDB.eliminar(clave=115)
    #     self.assertFalse( 115 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")

    #     self.assertIs( self.ArbolBinarioDB.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoIzquierdo, None, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB hoja" )
    #     # elimino ArbolBinarioDB hoja derecho
    #     self.ArbolBinarioDB.eliminar(clave=130)
    #     self.assertFalse( 130 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertIs( self.ArbolBinarioDB.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoDerecho.hijoDerecho, None, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB hoja" )
    #     # elimino ArbolBinarioDB con un hijo izquierdo
    #     self.ArbolBinarioDB.eliminar(clave=35)
    #     self.assertFalse( 35 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ArbolBinarioDB.raiz.hijoIzquierdo.hijoIzquierdo.hijoDerecho.clave, 25, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB con un hijo" )
    #     # elimino ArbolBinarioDB con un hijo derecho
    #     self.ArbolBinarioDB.eliminar(clave=120)
    #     self.assertFalse( 120 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ArbolBinarioDB.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.clave, 125, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB con un hijo" )
    #     # elimino ArbolBinarioDB con hijo derecho e izquierdo (reemplazo con sucesor)
    #     self.ArbolBinarioDB.eliminar(clave=110)
    #     self.assertFalse( 110 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ArbolBinarioDB.raiz.hijoDerecho.clave, 125, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB con dos hijos: " +
    #                         "debe ser con reemplazo con sucesor" )
    #     self.assertIs( self.ArbolBinarioDB.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo, None,
    #                     msg="No se elimino el ArbolBinarioDB sucesor de su posicion original" )
    #     # elimino ArbolBinarioDB raiz (reemplazo con sucesor)
    #     self.ArbolBinarioDB.eliminar(clave=100)
    #     self.assertFalse( 100 in self.ArbolBinarioDB,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ArbolBinarioDB.raiz.clave, 105, 
    #                     msg="Procedimiento erroneo de eliminacion de ArbolBinarioDB con dos hijos: " +
    #                         "debe ser con reemplazo con sucesor" )
    #     self.assertIs( self.ArbolBinarioDB.raiz.hijoDerecho.hijoIzquierdo.clave, 108,
    #                     msg="No se elimino correctamente el ArbolBinarioDB " +
    #                     "sucesor de su posicion original" )
    
    def test_tamano(self):
        # insercion
        claves = [5, 7, 3, 4, 9, 1, 6, 8]
        self.assertEqual(self.ArbolBinarioDB.tamano, 0, "Al instanciar el ArbolBinarioDB, su tamaño debe ser cero")
        for n, i in enumerate(claves):
            self.ArbolBinarioDB.agregar(clave=i, valor=2*i)
            self.assertEqual(self.ArbolBinarioDB.tamano, n+1, f"ArbolBinarioDB deberia tener {n+1} elementos")
        self.assertEqual(len(self.ArbolBinarioDB), len(claves), "El operador len() debería estar correctamente sobrecargado")
        # eliminacion
        size = len(self.ArbolBinarioDB)
        for n, i in enumerate(claves):
            self.ArbolBinarioDB.eliminar(clave=i)
            self.assertEqual(self.ArbolBinarioDB.tamano, size-1-n, f"ArbolBinarioDB deberia tener {size-1-n} elementos")
        # (re)agregado
        np.random.shuffle(claves)
        for n, i in enumerate(claves):
            self.ArbolBinarioDB.agregar(clave=i, valor=2*i)
            self.assertEqual(self.ArbolBinarioDB.tamano, n+1, f"ArbolBinarioDB deberia tener {n+1} elementos")
    
    # def test_excepciones(self):
    #     """
    #     Asegura que se lancen debidamente las excepciones al realizar 
    #     operaciones inválidas
    #     """
    #     claves = [45, 100, 20, 80, 55, 25, 18]
    #     self.agregar_claves(*claves)
    #     # eliminacion de elemento que no esta en el arbol
    #     with self.assertRaises(Exception, msg='Debe arrojar error si se elimina elemento que no esta en el arbol') as _:
    #         self.ArbolBinarioDB.eliminar(clave=120)
    #     # acceso a clave que no existe en el arbol
    #     with self.assertRaises(Exception, msg='Debe arrojar error si se pide el valor de una clave inexistente') as _:
    #         self.ArbolBinarioDB.obtener(clave=50)
    #     # Por el momento se permite que se agreguen claves repetidas,
    #     # se deja libertad al programador si permite agregarlo mas de
    #     # una vez o sobrescribe el valor previo.
        
    # def test_sobrecarga_indexacion(self):
    #     """
    #     Verifica que el ArbolBinarioDB tenga sobrecargado los métodos necesarios
    #     para poder asignar, acceder y eliminar elementos mediante 
    #     indexación (es decir, con los corchetes)
    #     """
    #     claves = [45, 100, 20, 80, 55, 25, 18]
    #     # asignacion por indexado
    #     # por el momento no se verifica sobrescritura de carga util
    #     for i in claves:
    #         self.ArbolBinarioDB[i] = 2*i
    #     self.assertEqual(len(self.ArbolBinarioDB), len(claves))
    #     # acceso por indexado
    #     for i in claves:
    #         self.assertEqual(self.ArbolBinarioDB[i], 2*i)
    #     # eliminacion por indexado
    #     for i in claves:
    #         del self.ArbolBinarioDB[i]
    #     self.assertEqual(len(self.ArbolBinarioDB), 0)
        
    
if __name__ == '__main__':
    unittest.main()