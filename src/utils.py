def create_theta(lst: list):
    file = "theta0_theta1.txt"
    with open(file, 'w') as f:
        f.write(f"{lst[0]},{lst[1]}")
