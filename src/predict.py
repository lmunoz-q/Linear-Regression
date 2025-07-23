from train import estimate_prices

path = "theta0_theta1.txt"


def predict(path):
    print("Enter a mileage value")
    x = input()
    try:
        x = float(x)
    except:
        print("Mileage value must be a number")
        return
    with open(path, 'r') as f:
        line = f.read()
        theta0, theta1 = map(float, line.strip().split(','))
        price = estimate_prices((x / 1000), theta0, theta1)
        print(f"Estimate price = {price:.2f} euros")


if __name__ == "__main__":
    predict(path)
