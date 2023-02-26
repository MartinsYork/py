class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer created")

c = Customer("York", "Diamond")
print(c.name, c.membership_type)

c2 = Customer("marino", "Danger")
print(c2.name, c2.membership_type)

