from colors import color, inverter

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, c):
        return inverter.get(c, c)

    def verticalMirror(self):
        """Devuelve el espejo vertical de la imagen"""
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen"""
        return Picture(self.img[::-1])

    def negative(self):
        """Devuelve un negativo de la imagen"""
        negative = []
        for row in self.img:
            negative_row = [self._invColor(color[color_code]) for color_code in row]
            negative.append(negative_row)
        return Picture(negative)

    def join(self, p):
        """Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual"""
        joined = []
        for i in range(len(self.img)):
            joined.append(self.img[i] + p.img[i])
        return Picture(joined)

    def up(self, p):
        """Devuelve una nueva figura poniendo la figura del argumento encima de la figura actual"""
        return Picture(p.img + self.img)

    def under(self, p):
        """Devuelve una nueva figura poniendo la figura p debajo de la figura actual"""
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n"""
        repeated = []
        for row in self.img:
            repeated.append(row * n)
        return Picture(repeated)

    def verticalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual encima la cantidad de veces que indique el valor de n"""
        return Picture(self.img * n)

    # Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario o antihorario"""
        rotated = []
        for i in range(len(self.img[0])):
            rotated_row = ''.join([self.img[j][i] for j in range(len(self.img) - 1, -1, -1)])
            rotated.append(rotated_row)
        return Picture(rotated)

