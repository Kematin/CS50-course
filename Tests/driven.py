import math

def is_prime(num) -> bool:
    # Num < 2 not prime
    if num < 2:
        return False

    for i in range(num, int(math.sqrt(num))):

        # Find factors
        if num % i == 0:
            return False

    # If factors not found return True
    return True



# Test Function
def test_prime(num, excepted):
    if is_prime(num) != excepted:
        print(f"ERROR! Bad result for num:{num}, is_prime not return {excepted}")

if __name__ == "__main__":
    test_prime(5, True)
    test_prime(10, False)
    test_prime(25, False)
