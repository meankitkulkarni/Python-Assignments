# Practical 7 — Design Note

This program demonstrates inheritance, composition, method overriding, a validated property, and Python package structure.

The **IS-A relationship** is used in the hierarchy `Person → Employee → Developer`. An Employee is a Person, and a Developer is an Employee, so inheritance allows child classes to reuse the parent class's attributes and methods. `super()` calls the parent constructor so that shared information, such as the person's name and employee ID, is initialized without repeating code.

The **HAS-A relationship** is shown by `Employee` having a `Department` object. The department is stored in `self.department`, but `Department` is not a subclass of `Employee`. This is composition: the employee refers to a separate object that represents the department.

`Developer` overrides `describe()` to add the developer's role and programming language. It also calls `super().describe()` so the description from `Employee` is preserved and extended. The `salary` property provides normal attribute-style access while its setter validates values. A negative salary raises `ValueError` instead of being stored. Without the setter, invalid salary values could be assigned without this check.

The classes are separated into `people.py` and `department.py` inside the `staff_app` package. `__init__.py` exposes the classes for convenient imports, while `run.py` demonstrates their use from the project root.
