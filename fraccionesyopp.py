#
# Proyecto: Programación Orientada a Objetos (POO) - Fracciones
#
# Este proyecto demuestra el uso de la POO en Python con clases
# para manejar fracciones simples y mixtas.
#
# Características principales:
#   - Creación de clases y objetos
#   - Sobrecarga de operadores para aritmética básica (+, -, *, /)
#   - Herencia (la clase FraccionMixta hereda de Fraccion)
# Elaboración por Francisco Javier Pérez, 2025

class Fraccion:
    """Clase para representar y operar con fracciones."""
    def __init__(self, n, d):
        """Inicializa una fracción, validando el numerador y el denominador."""
        if isinstance(n, int):
            self.num = n
        else:
            self.num = 0
            
        if isinstance(d, int) and d != 0:
            self.den = d
        else:
            self.den = 1
        
        self.simplifica()

    def __str__(self):
        """Devuelve una representación en cadena de la fracción."""
        return f"( {self.num} / {self.den} )"

    def __mul__(self, b):
        """Sobrecarga el operador de multiplicación (*)."""
        n = self.num * b.num
        d = self.den * b.den
        return Fraccion(n, d)

    def __add__(self, b):
        """Sobrecarga el operador de suma (+)."""
        n = (self.num * b.den) + (self.den * b.num)
        d = self.den * b.den
        return Fraccion(n, d)

    def __sub__(self, b):
        """Sobrecarga el operador de resta (-)."""
        n = (self.num * b.den) - (self.den * b.num)
        d = self.den * b.den
        return Fraccion(n, d)

    def __truediv__(self, b):
        """Sobrecarga el operador de división (/)."""
        n = self.num * b.den
        d = self.den * b.num
        return Fraccion(n, d)

    def __eq__(self, b):
        """Sobrecarga el operador de igualdad (==)."""
        return self.ret_resul() == b.ret_resul()

    def __lt__(self, b):
        """Sobrecarga el operador de menor que (<)."""
        return self.ret_resul() < b.ret_resul()

    def __gt__(self, b):
        """Sobrecarga el operador de mayor que (>)."""
        return self.ret_resul() > b.ret_resul()
    
    def ret_resul(self):
        """Devuelve el valor decimal de la fracción."""
        return self.num / self.den

    def simplifica(self):
        """Simplifica la fracción usando el Máximo Común Divisor (MCD)."""
        def mcd(a, b): 
            """Función auxiliar para calcular el MCD."""
            while b:
                a, b = b, a % b
            return a

        mc = mcd(self.num, self.den)
        self.num = int(self.num / mc)
        self.den = int(self.den / mc)

class FraccionMixta(Fraccion):
    """Clase para representar y operar con fracciones mixtas. Hereda de Fraccion."""
    def __init__(self, ent, num=0, den=1):
        self.ent = ent
        super().__init__(num, den)
        self._convert_to_proper()

    def __str__(self):
        """Devuelve una representación en cadena de la fracción mixta."""
        if self.ent != 0:
            return f"{self.ent} {super().__str__().strip()}"
        else:
            return super().__str__()

    def _convert_to_proper(self):
        """Simplifica la fracción mixta."""
        if self.num > self.den:
            aux = self.num // self.den
            self.ent += aux
            self.num -= (aux * self.den)

    def toFraccion(self):
        """Convierte la fracción mixta a una fracción simple."""
        n, d = self.num, self.den
        if self.ent != 0:
            n = (self.ent * d) + n
        return Fraccion(n, d)

    def __add__(self, obj):
        """Sobrecarga el operador de suma (+) para fracciones mixtas."""
        result_frac = self.toFraccion() + obj.toFraccion()
        return FraccionMixta(0, result_frac.num, result_frac.den)

    def __sub__(self, obj):
        """Sobrecarga el operador de resta (-) para fracciones mixtas."""
        result_frac = self.toFraccion() - obj.toFraccion()
        return FraccionMixta(0, result_frac.num, result_frac.den)

    def __mul__(self, obj):
        """Sobrecarga el operador de multiplicación (*) para fracciones mixtas."""
        result_frac = self.toFraccion() * obj.toFraccion()
        return FraccionMixta(0, result_frac.num, result_frac.den)

    def __truediv__(self, obj):
        """Sobrecarga el operador de división (/) para fracciones mixtas."""
        result_frac = self.toFraccion() / obj.toFraccion()
        return FraccionMixta(0, result_frac.num, result_frac.den)

    def __eq__(self, b):
        """Sobrecarga el operador de igualdad (==) para fracciones mixtas."""
        return self.toFraccion() == b.toFraccion()

def main():
    """Función principal para probar las clases."""
    print("--- Demostración de la clase Fraccion ---")
    a = Fraccion(3, 2)
    b = Fraccion(7, 4)
    print(f"Fracción A: {a}")
    print(f"Fracción B: {b}")

    print(f"\nSuma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    
    print("\n--- Demostración de la clase FraccionMixta ---")
    c = FraccionMixta(2, 3, 4)  # Representa 2 3/4
    d = FraccionMixta(3, 1, 2)  # Representa 3 1/2
    print(f"Fracción Mixta C: {c}")
    print(f"Fracción Mixta D: {d}")

    print(f"\nSuma: {c} + {d} = {c + d}")
    print(f"Resta: {c} - {d} = {c - d}")
    print(f"Multiplicación: {c} * {d} = {c * d}")
    print(f"División: {c} / {d} = {c / d}")
    
    print("\n--- Demostración de simplificación y comparación ---")
    e = FraccionMixta(2, 3, 4)
    f = FraccionMixta(3, 1, 2)
    print(f"Fracción Mixta E: {e}")
    print(f"Fracción Mixta F: {f}")
    if e == f:
        print(f"Comparación: {e} es igual a {f}")
    else:
        print(f"Comparación: {e} no es igual a {f}")

    g = FraccionMixta(2, 3, 4)
    h = FraccionMixta(3, 1, 2)
    if g < h:
        print(f"\nComparación: {g} es menor que {h}")
    else:
        print(f"\nComparación: {g} es mayor que {h}")

if __name__ == "__main__":
    main()
