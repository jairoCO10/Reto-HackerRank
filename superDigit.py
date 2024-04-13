#
# Complete the 'super_digit' function below.
#  https://www.hackerrank.com/challenges/recursive-digit-sum/problem
#  ralizado por Jairo Cogollo
#  mickt681@gmail.com
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def super_digit(n:int):
    # Inicializar la suma de dígitos como 0
    sumOfDigits = 0
    
    # Sumar los dígitos del número utilizando operaciones de división y módulo
    while n > 0:

        sumOfDigits += n % 10
        n //= 10

    return sumOfDigits


def super_digit(n:int):

    sumDigits = super_digit(n)
    if sumDigits < 10:
        return sumDigits
    
    else:
        return super_digit(sumDigits)


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input("enter the value of n:  "))
    k = int(input("enter the value of k:  "))

    number =  n * k
    result = super_digit(number)

    
    print('super digit of (k, n): ({}, {}) is {} \n'.format(k, n, result))

    # fptr.write(str(result) + '\n')

    # fptr.close()

