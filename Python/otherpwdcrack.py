import itertools
import string
import time

pwsd = input("Your Password:")

start = time.time()

def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)

print(guess_password(pwsd))


end = time.time()
print("Time taken:", end - start)