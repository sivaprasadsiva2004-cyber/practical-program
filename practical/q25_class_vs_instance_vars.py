# ============================================================
# Q25. Illustrate class variables vs instance variables
#      with examples.
# ============================================================


class Student:
    """
    CLASS VARIABLES  – declared inside the class body, outside any method.
                       Shared by ALL instances.
                       Accessed via ClassName.var or self.var

    INSTANCE VARIABLES – declared inside __init__ (or other methods)
                          using self.var.
                          Unique to each instance.
    """

    # ── Class Variables ───────────────────────────────────────
    school_name   = "Python Institute of Technology"   # shared
    student_count = 0                                  # shared counter

    def __init__(self, name: str, roll_no: int, marks: float):
        # ── Instance Variables ────────────────────────────────
        self.name    = name        # unique per object
        self.roll_no = roll_no     # unique per object
        self.marks   = marks       # unique per object

        # Modify the class variable using the class name
        Student.student_count += 1

    def display(self):
        print(f"  Name      : {self.name}")
        print(f"  Roll No   : {self.roll_no}")
        print(f"  Marks     : {self.marks}")
        print(f"  School    : {Student.school_name}")   # class var via class name
        print(f"  Total Std : {Student.student_count}")
        print()

    @classmethod
    def get_count(cls):
        """Class method – operates on the class, not instance."""
        return cls.student_count

    @staticmethod
    def passing_marks():
        """Static method – no access to class or instance."""
        return 35


# ── Create instances ──────────────────────────────────────────
print("=" * 55)
print("  Class vs Instance Variables Demo")
print("=" * 55)

s1 = Student("Alice", 101, 88.5)
s2 = Student("Bob",   102, 73.0)
s3 = Student("Carol", 103, 91.0)

print(f"\n  Class variable  'school_name'   (same for all):")
print(f"    s1.school_name = {s1.school_name}")
print(f"    s2.school_name = {s2.school_name}")
print(f"    s3.school_name = {s3.school_name}")

print(f"\n  Class variable  'student_count' (shared counter):")
print(f"    Student.student_count = {Student.student_count}")

print(f"\n  Instance variables (unique per object):")
print(f"    s1: name={s1.name}, roll_no={s1.roll_no}, marks={s1.marks}")
print(f"    s2: name={s2.name}, roll_no={s2.roll_no}, marks={s2.marks}")
print(f"    s3: name={s3.name}, roll_no={s3.roll_no}, marks={s3.marks}")


# ── Modifying a class variable via an instance ─────────────────
print("\n" + "=" * 55)
print("  Modifying class variable through an instance")
print("─" * 55)
print(f"  Before: Student.school_name = '{Student.school_name}'")

# This creates a NEW instance variable that SHADOWS the class variable
# for s1 only – it does NOT change the class variable.
s1.school_name = "Override University"

print(f"  After s1.school_name = 'Override University':")
print(f"    s1.school_name        = {s1.school_name}  (instance var – shadowed)")
print(f"    s2.school_name        = {s2.school_name}")
print(f"    Student.school_name   = {Student.school_name}  (class var unchanged)")

print(f"\n  'school_name' in s1.__dict__: {'school_name' in s1.__dict__}")
print(f"  'school_name' in s2.__dict__: {'school_name' in s2.__dict__}")


# ── __dict__ inspection ───────────────────────────────────────
print("\n" + "=" * 55)
print("  __dict__ of class vs instance")
print("─" * 55)
print(f"  Student.__dict__ keys : {[k for k in Student.__dict__ if not k.startswith('__')]}")
print(f"  s2.__dict__           : {s2.__dict__}")


# ── classmethod and staticmethod ──────────────────────────────
print("\n" + "=" * 55)
print("  Class method and Static method")
print("─" * 55)
print(f"  Student.get_count()   = {Student.get_count()}  (classmethod)")
print(f"  Student.passing_marks() = {Student.passing_marks()}  (staticmethod)")

print("\n  Full display for each student:")
print("─" * 55)
for s in (s1, s2, s3):
    s.display()