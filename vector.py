class Vector3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector3D(self.x * other, self.y * other, self.z * other)

        if type(other) is type(self):
            return Vector3D(
                self.y * other.z - other.y * self.z,
                other.x * self.z - self.x * other.z,
                self.x * other.y - other.x * self.y
            )

    def __rmul__(self, other: int | float):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
