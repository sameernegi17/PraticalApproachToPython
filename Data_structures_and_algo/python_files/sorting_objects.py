class User:
    def __init__(self,user_id) -> None:
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"User {self.user_id}"
user_list = [User(11),User(1),User(5),User(2),User(17)]

print(sorted(user_list,key=lambda u : u.user_id))

#Pythonic Way

from operator import attrgetter

print(sorted(user_list,key=attrgetter('user_id')))
print(max(user_list,key=attrgetter('user_id')))
print(min(user_list,key=attrgetter('user_id')))