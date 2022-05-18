def create_validator(mode, number):
    if mode == "Max":
        return lambda value: value < number
    elif mode == "Min":
        return lambda value: value > number

is_below_max = create_validator("Max", 31)

print(is_below_max(15))
print(is_below_max(32))

###### another right way #######

class ValidateNumber:
    def __init__(self, number) -> None:
        self.number = number
    
    def is_bigger_than(self, other_number):
        return other_number < self.number
    
    def is_smaller_than(self, other_number):
        return other_number > self.number


input_number = ValidateNumber(31)

print(input_number.is_bigger_than(15))
print(input_number.is_bigger_than(35))