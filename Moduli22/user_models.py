from pydantic import BaseModel,  constr , conint

class User(BaseModel):
    id:int
    name:str
    age:int=0
    email: str="noname@gmail.com"

user1 = User(id=2, name="Stina",email="hello@gmail.com")
print(user1)

user2 = User(id=2, name="Stina")
print(user2)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length = 2 ,max_length=50)

user3 = another_user(id=5,name="test test")
print(user3)






