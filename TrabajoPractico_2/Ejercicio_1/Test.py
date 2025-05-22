import unittest
from modules.ordenamiento import ColaPrioridad
import numpy as np

class TestColaPrioridad(unittest.TestCase):
    
    def setUp(self):
        self.ColaPrioridad = ColaPrioridad()
    
    def agregar_claves(self, *args):
        for value in args:
            self.ColaPrioridad.agregar(clave=value, valor=2*value)
    
    def tearDown(self):
        pass
    
    def test_busqueda(self):
        claves = [45, 100, 20, 80, 55, 25, 18]
        self.agregar_claves(*claves)
        for clave in claves:
            self.assertEqual( self.ColaPrioridad.obtener(clave), 2*clave )        
    
    # def test_insercion(self):
    #     """
    #     Verifica la insercion binaria tradicional
    #     """
    #     self.agregar_claves(45, 100, 20, 80, 10, 110, 50)
    #     # verifico posicion relativa desde la raiz
    #     self.assertEqual(self.ColaPrioridad.raiz.clave, 45,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.cargaUtil, 90,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoDerecho.clave, 100,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoDerecho.cargaUtil, 200,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoIzquierdo.clave, 20,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoIzquierdo.cargaUtil, 40,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoDerecho.hijoIzquierdo.clave, 80,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoDerecho.hijoIzquierdo.cargaUtil, 160,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoIzquierdo.hijoIzquierdo.clave, 10,
    #                     "ColaPrioridad insertado incorrectamente")
    #     self.assertEqual(self.ColaPrioridad.raiz.hijoIzquierdo.hijoIzquierdo.cargaUtil, 20,
    #                     "ColaPrioridad insertado incorrectamente")
    #     # verifico ColaPrioridads hojas
    #     self.assertTrue(self.ColaPrioridad.raiz.hijoIzquierdo.hijoIzquierdo.esHoja(), 
    #                     "ColaPrioridad 10 debe ser un ColaPrioridad hoja")
    #     self.assertTrue(self.ColaPrioridad.raiz.hijoDerecho.hijoIzquierdo.hijoIzquierdo.esHoja(), 
    #                     "ColaPrioridad 50 debe ser un ColaPrioridad hoja")
    #     self.assertTrue(self.ColaPrioridad.raiz.hijoDerecho.hijoDerecho.esHoja(), 
    #                     "ColaPrioridad 110 debe ser un ColaPrioridad hoja")
    #     # verifico ColaPrioridads internos
    #     self.assertFalse(self.ColaPrioridad.raiz.esHoja(), 
    #                     "ColaPrioridad 45 debe ser ColaPrioridad interno, no un ColaPrioridad hoja")
    #     self.assertFalse(self.ColaPrioridad.raiz.hijoIzquierdo.esHoja(), 
    #                     "ColaPrioridad 20 debe ser ColaPrioridad interno, no un ColaPrioridad hoja")
    #     self.assertFalse(self.ColaPrioridad.raiz.hijoDerecho.esHoja(), 
    #                     "ColaPrioridad 100 debe ser un ColaPrioridad interno, no un ColaPrioridad hoja")
    #     self.assertFalse(self.ColaPrioridad.raiz.hijoDerecho.hijoIzquierdo.esHoja(), 
    #                     "ColaPrioridad 80 debe ser un ColaPrioridad interno, no un ColaPrioridad hoja")
    
    # def test_operador_contains(self):
    #     """
    #     Verifica la sobrecarga del operador 'in', que corrobora si
    #     un elemento está o no en el ColaPrioridad
    #     """
    #     self.agregar_claves(45, 100, 20, 80, 10)
    #     self.assertTrue( 100 in self.ColaPrioridad )
    #     self.assertTrue( 10 in self.ColaPrioridad )
    #     self.assertFalse( 1 in self.ColaPrioridad )
    
    # def test_recorrido(self):
    #     """
    #     Para evaluar el recorrido, los elementos del árbol deben 
    #     recorrerse in-orden al iterar sobre él en un ciclo for
    #     """
    #     # tratamos de evitar tener claves repetidas
    #     claves = list(set(np.random.randint(0,1000, (100,))))
    #     np.random.shuffle(claves)
    #     self.agregar_claves(*claves)
    #     # comparo recorrido del árbol con lista ordenada
    #     claves = np.sort(claves)
    #     for n, item in enumerate(self.ColaPrioridad):
    #         self.assertEqual(claves[n], item[0])
    
    # def test_eliminacion(self):
    #     """
    #     Verifica los distintos casos de eliminacion en un arbol
    #     """
    #     self.agregar_claves(100, 50, 20, 35, 75, 110, 105, 137, 150, 
    #             145, 25, 170, 80, 120, 22, 125, 108, 79, 115, 130, 60)
    #     # elimino ColaPrioridad hoja izquierdo
    #     self.ColaPrioridad.eliminar(clave=115)
    #     self.assertFalse( 115 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertIs( self.ColaPrioridad.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoIzquierdo, None, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad hoja" )
    #     # elimino ColaPrioridad hoja derecho
    #     self.ColaPrioridad.eliminar(clave=130)
    #     self.assertFalse( 130 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertIs( self.ColaPrioridad.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.hijoDerecho.hijoDerecho, None, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad hoja" )
    #     # elimino ColaPrioridad con un hijo izquierdo
    #     self.ColaPrioridad.eliminar(clave=35)
    #     self.assertFalse( 35 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ColaPrioridad.raiz.hijoIzquierdo.hijoIzquierdo.hijoDerecho.clave, 25, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad con un hijo" )
    #     # elimino ColaPrioridad con un hijo derecho
    #     self.ColaPrioridad.eliminar(clave=120)
    #     self.assertFalse( 120 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ColaPrioridad.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo.clave, 125, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad con un hijo" )
    #     # elimino ColaPrioridad con hijo derecho e izquierdo (reemplazo con sucesor)
    #     self.ColaPrioridad.eliminar(clave=110)
    #     self.assertFalse( 110 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ColaPrioridad.raiz.hijoDerecho.clave, 125, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad con dos hijos: " +
    #                         "debe ser con reemplazo con sucesor" )
    #     self.assertIs( self.ColaPrioridad.raiz.hijoDerecho.hijoDerecho.hijoIzquierdo, None,
    #                     msg="No se elimino el ColaPrioridad sucesor de su posicion original" )
    #     # elimino ColaPrioridad raiz (reemplazo con sucesor)
    #     self.ColaPrioridad.eliminar(clave=100)
    #     self.assertFalse( 100 in self.ColaPrioridad,
    #                     msg="Elemento sigue figurando en el arbol")
    #     self.assertEqual( self.ColaPrioridad.raiz.clave, 105, 
    #                     msg="Procedimiento erroneo de eliminacion de ColaPrioridad con dos hijos: " +
    #                         "debe ser con reemplazo con sucesor" )
    #     self.assertIs( self.ColaPrioridad.raiz.hijoDerecho.hijoIzquierdo.clave, 108,
    #                     msg="No se elimino correctamente el ColaPrioridad " +
    #                     "sucesor de su posicion original" )
    
    # def test_tamano(self):
    #     # insercion
    #     claves = [5, 7, 3, 4, 9, 1, 6, 8]
    #     self.assertEqual(self.ColaPrioridad.tamano, 0, "Al instanciar el ColaPrioridad, su tamaño debe ser cero")
    #     for n, i in enumerate(claves):
    #         self.ColaPrioridad.agregar(clave=i, valor=2*i)
    #         self.assertEqual(self.ColaPrioridad.tamano, n+1, f"ColaPrioridad deberia tener {n+1} elementos")
    #     self.assertEqual(len(self.ColaPrioridad), len(claves), "El operador len() debería estar correctamente sobrecargado")
    #     # eliminacion
    #     size = len(self.ColaPrioridad)
    #     for n, i in enumerate(claves):
    #         self.ColaPrioridad.eliminar(clave=i)
    #         self.assertEqual(self.ColaPrioridad.tamano, size-1-n, f"ColaPrioridad deberia tener {size-1-n} elementos")
    #     # (re)agregado
    #     np.random.shuffle(claves)
    #     for n, i in enumerate(claves):
    #         self.ColaPrioridad.agregar(clave=i, valor=2*i)
    #         self.assertEqual(self.ColaPrioridad.tamano, n+1, f"ColaPrioridad deberia tener {n+1} elementos")
    
    # def test_excepciones(self):
    #     """
    #     Asegura que se lancen debidamente las excepciones al realizar 
    #     operaciones inválidas
    #     """
    #     claves = [45, 100, 20, 80, 55, 25, 18]
    #     self.agregar_claves(*claves)
    #     # eliminacion de elemento que no esta en el arbol
    #     with self.assertRaises(Exception, msg='Debe arrojar error si se elimina elemento que no esta en el arbol') as _:
    #         self.ColaPrioridad.eliminar(clave=120)
    #     # acceso a clave que no existe en el arbol
    #     with self.assertRaises(Exception, msg='Debe arrojar error si se pide el valor de una clave inexistente') as _:
    #         self.ColaPrioridad.obtener(clave=50)
    #     # Por el momento se permite que se agreguen claves repetidas,
    #     # se deja libertad al programador si permite agregarlo mas de
    #     # una vez o sobrescribe el valor previo.
        
    # def test_sobrecarga_indexacion(self):
    #     """
    #     Verifica que el ColaPrioridad tenga sobrecargado los métodos necesarios
    #     para poder asignar, acceder y eliminar elementos mediante 
    #     indexación (es decir, con los corchetes)
    #     """
    #     claves = [45, 100, 20, 80, 55, 25, 18]
    #     # asignacion por indexado
    #     # por el momento no se verifica sobrescritura de carga util
    #     for i in claves:
    #         self.ColaPrioridad[i] = 2*i
    #     self.assertEqual(len(self.ColaPrioridad), len(claves))
    #     # acceso por indexado
    #     for i in claves:
    #         self.assertEqual(self.ColaPrioridad[i], 2*i)
    #     # eliminacion por indexado
    #     for i in claves:
    #         del self.ColaPrioridad[i]
    #     self.assertEqual(len(self.ColaPrioridad), 0)
        
    
if __name__ == '__main__':
    unittest.main()