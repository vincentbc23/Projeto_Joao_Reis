class D:
    def __init__ (self, d1, d2):
        self._d1 = d1
        self._d2 = d2

    def get_d1(self):
        return self._d1

    def get_d2(self):
        return self._d2

    def set_d1(self, d):
        self._d1 = d

    def set_d2(self, d):
        self._d2 = d

    def MD1(self):
        print("Método MD1!")

    def MD2(self):
        print("Método MD2!")
