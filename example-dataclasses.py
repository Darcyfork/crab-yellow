# dataclasses
import dataclasses

def example_1():
    @dataclasses.dataclass()
    class ExampleA:
        name: str
        price: float = 0
        def hello(self):
            print('name: {}, price: {}'.format(self.name, self.price))
    @dataclasses.dataclass
    class ExampleB(ExampleA):
        score: int

    a = ExampleA('a',1)
    print(a.__repr__())
    # print(a.__hash__())

if __name__ == '__main__':
    example_1()
    