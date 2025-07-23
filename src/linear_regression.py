import matplotlib.pyplot as plt
import pandas as pd

path = "../ressources/data.csv"
thetas = "theta0_theta1.txt"


def main():
    df = pd.read_csv(path)
    with open(thetas, 'r') as f:
        line = f.read()
        theta0, theta1 = map(float, line.strip().split(','))
    kms = df["km"].tolist()
    prices = df["price"].tolist()
    x_min = min(kms)
    x_max = max(kms)
    x_values = list(range(x_min, x_max + 1000, 1000))
    y_values = [theta0 + theta1 * (x / 1000) for x in x_values]

    plt.scatter(kms, prices, color='blue', label='Data points')
    plt.plot(x_values, y_values, color='red', label='Regression Line')
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price (euros)")
    plt.title("Linear Regression")
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
