from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n: int = 8) -> str:
    if not isinstance(n, int):
        raise ValueError("Значение длины пароля задано некорректно.")
    population = ascii_uppercase + ascii_lowercase + digits
    return "".join(sample(population, n))

print(get_random_password())
