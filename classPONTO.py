# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 2024

@author: pbg

@info: exemplo de classe Ponto no âmbito da u.c. tomsa

@version: 0.1

"""
    
class Ponto:
    """Um ponto 3D no plano cartesiano"""
    
    def __init__(self, x=0, y=0, z=0):
        """
        Constrói um objeto ponto dado as coordenadas x, y e z.

        Parâmetros:
            x (float): coordenada x no plano cartesiano 3D
            y (float): coordenada y no plano cartesiano 3D
            z (float): coordenada z no plano cartesiano 3D
        """
        self._x = x
        self._y = y
        self._z = z
  
    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self._x}, y={self._y}, z={self._z})"
    
    def __str__(self) -> str:
        return '[ %2.1f, %2.1f, %2.1f]' % (self._x, self._y, self._z)

    """
    Métodos de acesso para os valores das coordenadas.
    """
    @property
    def x(self):
        """
        Retorna:
            x (float): coordenada x no plano cartesiano 3D
        """    
        return self._x
 
    @property
    def y(self):
        """
        Retorna:
            y (float): coordenada y no plano cartesiano 3D
        """    
        return self._y

    @property          
    def z(self):
        """
        Retorna:
            z (float): coordenada z no plano cartesiano 3D
        """    
        return self._z

    """
    Definir os valores das coordenadas.
    """
    @x.setter
    def x(self, x):
        """
        Parâmetros:
            x (float): coordenada x no plano cartesiano 3D
        """    
        self._x = x

    @y.setter
    def y(self, y):
        """
        Parâmetros:
            y (float): coordenada y no plano cartesiano 3D
        """    
        self._y = y
           
    @z.setter
    def z(self, z):
        """
        Parâmetros:
            z (float): coordenada z no plano cartesiano 3D
        """    
        self._z = z
