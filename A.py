class A:
    def __init__(self, a1, a2):
        self._a1 = a1
        self._a2 = a2

    def get_a1(self):
        return self._a1

    def set_a1(self, valor):
        self._a1 = valor

    def get_a2(self):
        return self._a2

    def set_a2(self, valor):
        self._a2 = valor

    def MA1(self):
        print("Método MA1!")

    def MA2(self):
        print("Método MA2!")

    def MA3(self):
        print("Alteração a classe A partir do clone")

    def getSoma(a, b):
        return a + b
