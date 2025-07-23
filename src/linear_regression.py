import matplotlib.pyplot as plt
import pandas as pd
from train import train
from predict import predict

path = "../ressources/data.csv"
thetas = "theta0_theta1.txt"


def plot_graph(path, thetas):
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


def main():
    while True:
        print("\nMenu :")
        print("1. Train a Model")
        print("2. Predict a price")
        print("3. Show graphic")
        print("4. Mean Square Error")
        print("5. Quit")
        choice = input("Choose an option : ")

        if choice == "1":
            print("Enter number of iterations")
            iterations = input()
            try:
                iterations = int(iterations)
            except:
                print("iterations must be an integer")
                return
            print("Enter the learning_rate")
            learning_rate = input()
            try:
                learning_rate = float(learning_rate)
            except:
                print("learning_rate must be a float")
            train(path, iterations, learning_rate)
        elif choice == "2":
            predict(thetas)
        elif choice == "3":
            plot_graph(path, thetas)
        elif choice == "4";
            evaluate_model(path, thetas)
        elif choice == "5":
            break
        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
