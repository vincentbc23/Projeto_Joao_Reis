class C:
    def __init__ (self, c1, c2):
        self._c1 = c1
        self._c2 = c2

    def get_c1(self):
        return self._c1

    def get_c2(self):
        return self._c2

    def set_c1(self, c):
        self._c1 = c

    def set_c2(self, c):
        self._c2 = c

    def MC1(self):
        print("Método MC1!")

    def MC2(self):
        print("Método MC2!")

    def MC3(self):
        print("Método MC3!")
