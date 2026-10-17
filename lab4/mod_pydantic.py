from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

def test_pydantic():
    user = User(name="Вадим", age=19)
    print(f"[Pydantic] Валідований об'єкт користувача: {user}")