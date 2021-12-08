"""
Roberto Reynoso
Sets Solution
"""

class MySets():
    
    def __init__(self):
        self.my_set_one = set()
        self.my_set_two = set()
        self.set_choice = "1"

# choose a set
    def choose_set(self):
        self.set_choice = input("""\n1. Set one
2. Set two
choice: """)

# add to set
    def add_set(self):
        if self.set_choice == "1":
            member = input("Add a member to the First set: ")
            self.my_set_one.add(member)
        elif self.set_choice == "2":
            member = input("Add a member to the Second set: ")
            self.my_set_two.add(member)

# remove from the set
    def remove_set(self):
        remove_set = input("""\n1. Remove a specific member from the set
2. Remove a random member from the set
3. Clear the set
Choice: """)

# Remove a specific member from the set
        if remove_set == "1" and self.set_choice == "1":
            if self.my_set_one:
                member_choice = input("Remove: ")
            else:
                print(f"Set_One is empty: {self.my_set_one}")
        elif remove_set == "1" and self.set_choice == "2":
            if self.my_set_two:
                member_choice = input("Remove: ")
            else:
                print(f"Set_Two is empty: {self.my_set_two}")
            
        if remove_set == "1" and self.set_choice == "1":
            if member_choice in self.my_set_one:
                self.my_set_one.remove(member_choice)
            else:
                print(f"""Member not found: {member_choice}
Set_One: {self.my_set_one}""")
        elif remove_set == "1" and self.set_choice == "2":
            if member_choice in self.my_set_two:
                self.my_set_two.remove(member_choice)
            else:
                print(f"""Member not found: {member_choice}
Set_Two: {self.my_set_two}""")

# Remove a random member from the set
        elif remove_set == "2" and self.set_choice == "1":
            if self.my_set_one:
                self.my_set_one.pop()
            else:
                print(f"Set_One is empty: {self.my_set_one}")
        elif remove_set == "2" and self.set_choice == "2":
            if self.my_set_two:
                self.my_set_two.pop()
            else:
                print(f"Set_Two is empty: {self.my_set_two}")

# Clear the set       
        elif remove_set == "3" and self.set_choice == "1":
            if self.my_set_one:
                self.my_set_one.clear()
            else:
                print(f"Set_One is empty: {self.my_set_one}")
        elif remove_set == "3" and self.set_choice == "2":
            if self.my_set_two:
                self.my_set_two.clear()
            else:
                print(f"Set_Two is empty: {self.my_set_two}")

# Compare the set
    def compare_set(self):
        unique = self.my_set_one.copy()
        unique.update(self.my_set_two)
        print(f"""\nSet_One: {self.my_set_one}
Set_Two: {self.my_set_two}
Unique_Values: {unique}
""")

# user menu
    def menu(self):
        select = ""
        while True:
            select = input(f"""\n1. Choose_Set
2. Add
3. Remove
4. Compare
5. Return Sets
Choice: """)
            if select == "1":
                MySets.choose_set(self)
            elif select == "2":
                MySets.add_set(self)
            elif select == "3":
                MySets.remove_set(self)
            elif select == "4":
                MySets.compare_set(self)
            elif select == "5":
                print(f"""Set_One: {self.my_set_one}
Set_Two: {self.my_set_two}""")
                break


start_set = MySets()
start_set.menu()
