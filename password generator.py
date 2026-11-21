import random
import string
CHARACTERS = string.ascii_letters + string.digits + string.punctuation
PASSWORD = ''.join(random.choices(CHARACTERS, k=10))
print(PASSWORD)