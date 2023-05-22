def bonAppetit(bill, k, b):
    # Write your code here
    b_actual = int((sum(bill) - bill[k]) / 2)
    if b == b_actual:
        print("Bon Appetit")
    else:
        print(b - b_actual)

bonAppetit([3, 10, 2, 9], 1, 7)
