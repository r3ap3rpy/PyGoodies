class Validator:
    @classmethod
    def check(cls, value):
        return value


class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"The expected type is {expencted_type}")
        return super().check(value)

class Integer(Typed):
    expeted_type = int

class String(Typed):
    expected_type = str

class Float(Typed):
    expected_type = float

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError("The value should be positive!")
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if not value:
            raise ValueError("The value should not be empty!")
        return super().check(value)
