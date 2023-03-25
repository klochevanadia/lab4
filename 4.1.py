class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sum__(self, number):
        x1 = self.x + number.x
        y1 = self.y + number.y
        z1 = self.z + number.z
        return Vector(x1, y1, z1)

    def __dif__(self, number):
        x2 = self.x - number.x
        y2 = self.y - number.y
        z2 = self.z - number.z
        return Vector(x2, y2, z2)

    def __mult__(self, number):
        if type(number) is Vector:
            factor = self.x*number.x, self.y*number.y, self.z*number.z
            return factor
        else:
            return Vector(self.x*number,self.y*number, self.z*number)
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)
vector3 = vector1.__sum__(vector2)
printObject = '; '.join([str(vector3.x), str(vector3.y), str(vector3.z)])
print('(' + printObject + ')')




