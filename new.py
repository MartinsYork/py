class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer created")


#c = Customer("York", "Diamond")
#print(c.name, c.membership_type)

#c2 = Customer("Yaji", "Gold")
#print(c2.name, c2.membership_type)

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def read_customer():
        print("Reading customer from database")

    def __str__(self):
        print("Conversion to string ongoing")
        return self.name + " " + self.membership_type

    def print_all_customers(cuctomers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

customers = [Customer("York", "Diamond"), Customer("Yaji", "Gold")]

#print(c.name, c.membership_type)

#print(customers[1].membership_type)
#customers[1].update_membership("Diamond")
#print(customers[1].membership_type)


#def read_customer():

#Customer.read_customer()

#def __str__(self):

#print(customers[1])
#customers[1].update_membership("Diamond")
#print(customers[1])

#Customer.print_all_customers(customers)

print(customers[0] == customers[1])