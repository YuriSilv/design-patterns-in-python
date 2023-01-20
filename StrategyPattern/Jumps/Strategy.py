#"Strategy pattern define a family of algorithms, encapsulates each one, and makes them interchangeable.
# Strategy lets the algorithm vary independently from clients that use it." - book Head First Design Patterns

#Behavioral pattern

#Em minhas palavras: o padrão de projeto splita/divide um algoritmo que pode ser implementado de muitas formas, cada
#uma com seu propósito. Logo, ele traz a vantagem de manutenção nos algoritmos específicos.

from abc import ABC, abstractclassmethod

class Istrategy(ABC):

    @abstractclassmethod
    def execute(self):
        pass