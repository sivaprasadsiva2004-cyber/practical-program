# ============================================================
# Q24. Demonstrate inheritance using a
#      multi-level class hierarchy.
#
#  Hierarchy:
#    Animal  (base)
#      └── Mammal  (level 1)
#            └── Dog  (level 2)
#                  └── GuideDog  (level 3)
# ============================================================


# ── Level 0 – Base class ──────────────────────────────────────
class Animal:
    """
    Root of the hierarchy.
    Every animal has a name and can breathe and eat.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age  = age
        print(f"  [Animal.__init__] '{name}' created")

    def breathe(self):
        print(f"  {self.name} is breathing.")

    def eat(self, food: str):
        print(f"  {self.name} eats {food}.")

    def __str__(self):
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"

    def info(self):
        print(f"\n  {'─'*40}")
        print(f"  Class   : {self.__class__.__name__}")
        print(f"  MRO     : {[c.__name__ for c in type(self).__mro__]}")
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")


# ── Level 1 – Mammal inherits Animal ─────────────────────────
class Mammal(Animal):
    """
    All mammals are warm-blooded and nurse young with milk.
    Inherits from Animal.
    """

    def __init__(self, name: str, age: int, warm_blooded: bool = True):
        super().__init__(name, age)     # call Animal.__init__
        self.warm_blooded = warm_blooded
        print(f"  [Mammal.__init__] warm_blooded={warm_blooded}")

    def nurse_young(self):
        print(f"  {self.name} nurses its young with milk.")

    def regulate_temperature(self):
        status = "warm-blooded" if self.warm_blooded else "cold-blooded"
        print(f"  {self.name} is {status}.")

    def info(self):
        super().info()
        print(f"  Warm-blooded: {self.warm_blooded}")


# ── Level 2 – Dog inherits Mammal ────────────────────────────
class Dog(Mammal):
    """
    A domestic dog – has a breed and can bark/fetch.
    Inherits from Mammal → Animal.
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
        print(f"  [Dog.__init__] breed='{breed}'")

    def bark(self):
        print(f"  {self.name} says: Woof! Woof!")

    def fetch(self, item: str):
        print(f"  {self.name} fetches the {item}!")

    def info(self):
        super().info()
        print(f"  Breed   : {self.breed}")


# ── Level 3 – GuideDog inherits Dog ──────────────────────────
class GuideDog(Dog):
    """
    A trained guide dog assigned to assist a handler.
    Inherits from Dog → Mammal → Animal.
    """

    def __init__(self, name: str, age: int, breed: str, handler: str):
        super().__init__(name, age, breed)
        self.handler     = handler
        self.is_on_duty  = False
        print(f"  [GuideDog.__init__] handler='{handler}'")

    def start_duty(self):
        self.is_on_duty = True
        print(f"  {self.name} is now ON DUTY – guiding {self.handler}.")

    def end_duty(self):
        self.is_on_duty = False
        print(f"  {self.name} is OFF DUTY. Good dog!")

    def guide(self, destination: str):
        if self.is_on_duty:
            print(f"  {self.name} safely guides {self.handler} to {destination}.")
        else:
            print(f"  {self.name} is off duty and cannot guide right now.")

    def info(self):
        super().info()
        print(f"  Handler : {self.handler}")
        print(f"  On Duty : {self.is_on_duty}")
        print(f"  {'─'*40}")


# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Multi-level Inheritance Demo")
    print("=" * 55)

    print("\n--- Creating a plain Animal ---")
    a = Animal("Generic Animal", 3)
    a.breathe()
    a.eat("grass")

    print("\n--- Creating a Mammal ---")
    m = Mammal("Lion", 5)
    m.breathe()          # inherited from Animal
    m.nurse_young()      # own method
    m.regulate_temperature()

    print("\n--- Creating a Dog ---")
    d = Dog("Buddy", 2, "Labrador")
    d.breathe()          # from Animal
    d.nurse_young()      # from Mammal
    d.bark()             # own method
    d.fetch("ball")

    print("\n--- Creating a GuideDog ---")
    g = GuideDog("Max", 4, "Golden Retriever", "Alice")
    g.breathe()          # Animal
    g.bark()             # Dog
    g.start_duty()       # GuideDog
    g.guide("hospital")  # GuideDog
    g.end_duty()

    print("\n--- instanceof / issubclass checks ---")
    print(f"  isinstance(g, GuideDog) = {isinstance(g, GuideDog)}")
    print(f"  isinstance(g, Dog)      = {isinstance(g, Dog)}")
    print(f"  isinstance(g, Mammal)   = {isinstance(g, Mammal)}")
    print(f"  isinstance(g, Animal)   = {isinstance(g, Animal)}")
    print(f"  issubclass(GuideDog, Animal) = {issubclass(GuideDog, Animal)}")

    print("\n--- Full info() via inherited chain ---")
    g.info()