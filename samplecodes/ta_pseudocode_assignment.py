if __name__ == "__main__":
    initial_amount = 10000
    count = 0
    while initial_amount > 0:
        initial_amount -= 500
        initial_amount += initial_amount * 0.005
        count += 1
        print(initial_amount, count)