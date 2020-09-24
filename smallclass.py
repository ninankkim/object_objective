class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.greeting_count = 0
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.count_greetings()


    def description(self):
        print('I am {self.name}, my email is {self.email}, and my phone number is {self.phone}!'.format(self.name, self.email, self.phone))

    def count_greetings(self):
        self.greeting_count += 1
        print(self.greeting_count)

    def add_friend(self.friends):
        self.friends.append(friends)



Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
Alison = Person("Alison", "alison@yahoo.com", "123456789" )
Nina = Person ("Nina", "nina@gmail.com", "987654321")

Jordan.greet(Sonny)
Sonny.greet(Jordan)

Alison.friends.append(Sonny)
print(len)


print(f" {Sonny.name}: \n {Sonny.email}: \n {Sonny.phone}:")
print(f" {Jordan.name}: \n {Jordan.email}: \n {Jordan.phone}:")







