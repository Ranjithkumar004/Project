import random

def password_generator():
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

    size = random.randint(7,10)

    return ''.join(random.choice(chars) for x in range(size))

print(password_generator())