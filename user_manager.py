import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":


    # RNF3
    um = UserManager()
um.add_user(10, "Ana")
um.add_user(10, "Luis")  # Duplicado

print("\nUsuarios después de agregar duplicados:", um.users)

print("find_user(10):", um.find_user(10)) 

um.delete_user(10) 
print("Usuarios después de delete_user(10):", um.users) 
