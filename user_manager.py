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

    #RF1
    user_manager=UserManager()
    for i in range(500):
        user_manager.add_user(i,f"Yo soy el num:{i}" )

    #RF2
    um = UserManager()
    um.add_user(1, "Ana")

    print("RF2 existente:", um.find_user(1))

    print("RF2 inexistente:", um.find_user(999))  


    #RF3
    print("Antes de borrar:", um.users)
    um.delete_user(1)
    print("Después de borrar:", um.users)



    #RF4
    um.add_user(1, "Ana")
    um.add_user(2, "Bob")

    print("get_all_names:", um.get_all_names())



