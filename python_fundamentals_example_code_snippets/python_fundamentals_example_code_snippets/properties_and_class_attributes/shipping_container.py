import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    next_serial = 133

    @classmethod
    def _get_next_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return str(serial)

    @staticmethod
    def _get_bic_code(owner, serial):
        return iso6346.create(owner, str(serial).zfill(6))

    @staticmethod
    def _f_to_c(fahreinheit):
        return (fahreinheit - 32) * 5 / 9

    @staticmethod
    def _c_to_f(celsius):
        return (celsius + 32) * 9 / 5

    @classmethod
    def create_empty(cls, owner, length_ft, *args, **kwargs):
        return cls(owner, length_ft, *args, **kwargs)

    def __init__(self, owner, length_ft, contents):
        self.owner = owner
        self.contents = contents
        self._length_ft = length_ft
        self.bic = self._get_bic_code(owner=self.owner, serial=ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return (self._length_ft * ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT)


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4
    REFRIGERATOR_VOLUME_FT3 = 100

    @staticmethod
    def _get_bic_code(owner, serial):
        return iso6346.create(owner, str(serial).zfill(6), category="R")

    def __init__(self, owner, length_ft, contents, celsius):
        super().__init__(owner, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > self.MAX_CELSIUS:
            raise ValueError("Temperature is too hot")
        self._celsius = value

    @property
    def fahreinheit(self):
        return ShippingContainer._c_to_f(self.celsius)

    @fahreinheit.setter
    def fahhreinheit(self, value):
        self.celsius = ShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return (super().volume_ft3 - RefrigeratorShippingContainer.REFRIGERATOR_VOLUME_FT3)


class HeatedRefrigeratorShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20

    @RefrigeratorShippingContainer.celsius.setter
    def celsius(self, value):
        if (value <= HeatedRefrigeratorShippingContainer.MIN_CELSIUS):
            raise ValueError("Temperature Too cold")
        RefrigeratorShippingContainer.celsius.fset(self, value)
