 # SOLID Principle   
   
As any strong structure, to build it you have to follow some rules ,   
SOLID are a set of five design principles in object-oriented programming that    
help programmers to make sure their code is strong, flexible, and easy to change.   
 --- 
   
 ## **`S`ingle Responsibility Principle (SRP)**   
A class should have only one reason to change, meaning it should have only one responsibility.   
magine you have blocks that are only used to build roofs, and others just for doors. That way, if you want to change the roof, you only need to replace the roof blocks, not the whole house.   
 ### Example without SRP   
```
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    def print_receipt(self):
        for item in self.items:
            print(f"{item['name']}: ${item['price']}")
        print(f"Total: ${self.calculate_total()}")

```
 ### Example with SRP   
```
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

class ReceiptPrinter:
    @staticmethod
    def print_receipt(order):
        for item in order.items:
            print(f"{item['name']}: ${item['price']}")
        print(f"Total: ${order.calculate_total()}")

```
 --- 
 ## `O`pen/Closed Principle (OCP)   
Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. In other words, you should be able to add new functionality without changing existing code.   
Example: Adding new shapes to an existing drawing program without modifying existing code.   
 ### Example without OCP   
```
class DrawingProgram:
    def draw_shape(self, shape):
        if shape == 'circle':
            self.draw_circle()
        elif shape == 'square':
            self.draw_square()

    def draw_circle(self):
        print("Drawing a circle")

    def draw_square(self):
        print("Drawing a square")

program = DrawingProgram()
program.draw_shape('circle')
program.draw_shape('square')

```
 ### Example with OCP   
```
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class DrawingProgram:
    def draw_shape(self, shape):
        shape.draw()

program = DrawingProgram()
circle = Circle()
square = Square()

program.draw_shape(circle)
program.draw_shape(square)

```
 --- 
 ## **`L`iskov Substitution Principle (LSP**)   
Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.   
*subclass can do every thing a superclass can do*   
 ### Example without LSP   
```
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Can't fly")
```
 ### Example with LSP   
```
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")

def make_bird_fly(bird):
    bird.fly()
```
 --- 
 ## `I`nterface Segregation Principle (ISP)   
Clients should not be forced to depend on interfaces they do not use.    
This principle encourages the creation of small, focused interfaces instead of large, general-purpose ones.   
 ### Example without ISP   
```
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class SuperWorker(Worker):
    def work(self):
        print("SuperWorker is working")

    def eat(self):
        print("SuperWorker is eating")

class Robot(Worker):
    def work(self):
        print("Robot is working")

```
 ### Example with ISP   
```
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Worker is working")

class SuperWorker(Workable, Eatable):
    def work(self):
        print("SuperWorker is working")

class Robot(Workable):
    def work(self):
        print("Robot is working")

```
 --- 
 ## `D`ependency Inversion Principle (DIP)   
High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.   
*It focuses on decoupling high-level modules from low-level modules by introducing an abstraction layer between them. This principle promotes the idea that both high-level and low-level modules should depend on abstractions rather than concrete implementations.*   
     
   ### *High-Level Modules and Low-Level Modules:*   
  *High-level modules are those that encapsulate complex business logic or application-specific functionality. These modules are responsible for making decisions and orchestrating the overall flow of the program. They should not be concerned with the specific implementation details of low-level operations.*   
  *Low-level modules are responsible for specific technical operations or details, such as database access, file I/O, or network communication.*   
     
   ### *The Problem of Direct Dependencies:*   
  *When high-level modules directly depend on low-level modules, it creates a tight coupling between them. This can lead to several issues:*   
  1. ***Rigidity**: Changes in low-level modules might require modifications in high-level modules, leading to cascading changes throughout the codebase.*   
  2. ***Difficulty in Testing**: Unit testing high-level modules becomes difficult because they are tightly coupled with concrete low-level implementations.*   
  3. ***Limited Flexibility**: It becomes challenging to replace or switch out low-level implementations without affecting the high-level logic.*   
 ### Example without DIP   
```
 """ In this example, the MessagingApp high-level module directly depends on the concrete implementations of EmailSender and SMSSender, violating the Dependency Inversion  Principle. """

class EmailSender:
    def send_email(self, message):
        # Send email logic

class SMSSender:
    def send_sms(self, message):
        # Send SMS logic

class MessagingApp:
    def __init__(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()

    def send_message(self, message, channel):
        if channel == "email":
            self.email_sender.send_email(message)
        elif channel == "sms":
            self.sms_sender.send_sms(message)


```
 ### Example with DIP   
```
""" Now, the high-level module MessagingApp depends on the abstraction MessageSender, and the specific sender (email or SMS) is injected into it. This adheres to the Dependency Inversion Principle, making the code more flexible and maintainable. New sender  implementations can be added without modifying the MessagingApp class. """

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        # Send email logic

class SMSSender(MessageSender):
    def send(self, message):
        # Send SMS logic

class MessagingApp:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message):
        self.sender.send(message)

```
 --- 
