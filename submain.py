def is_not_prime(number):
    if (number <= 0) or (number == 1):
        return False
    elif number > 1:
        for i in range(2, number):
            if number % i != 0:
                return True
            else:
                return False
    
print(is_not_prime(9))  