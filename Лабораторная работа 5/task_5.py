import string
import random
def get_random_password(n: int = 8) -> str:
    alphabet = string.digits + string.ascii_letters
    return ''.join(random.sample(alphabet, n))

print(get_random_password())
