import os

name = os.getenv("USER_NAME", "stranger")
print(f"hello {name}!")
