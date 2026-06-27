from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message":"Hello, World"}

@app.get("/kurset")
def return_kurset():
    return {"kurset":["Python Adv", "AI", "PHP"]}

@app.get("/kurset/{kursi_id}")
def return_kurset(item_id:int):
    return {"kurset":["Python Adv", "AI", "PHP"]}

@app.post("/register")
def create_user(name:str, password:str):
    return {"user_id":name, "password":password}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"message":"Item is deleted"}

@app.put("/user/password/{user_id}")
def change_Password(user_id:int,password:str):
    return {"message":"passwordi u ndryshua me sukses"}

