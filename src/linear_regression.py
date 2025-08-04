import matplotlib.pyplot as plt
import pandas as pd
from train import train
from predict import predict
import math

path = "../ressources/data.csv"
thetas = "theta0_theta1.txt"


def evaluate_model(path, thetas):
    """
    Evaluates the performance of a trained linear regression model
    using MSE and RMSE.

    Parameters:
        path (str): Path to the CSV file containing the dataset
        (columns: km, price).

        thetas (str): Path to the text file containing the trained
        theta0 and theta1 values.

    Prints:
        Mean Squared Error (MSE) and
        Root Mean Squared Error (RMSE) of the model predictions.
    """
    try:
        df = pd.read_csv(path)
        with open(thetas, 'r') as f:
            line = f.read()
            theta0, theta1 = map(float, line.strip().split(','))
        kms = df["km"].tolist()
        prices = df["price"].tolist()

        if not kms or not prices:
            print("Empty dataset.")
            return

        m = len(kms)
        total_squared_error = 0

        for km, actual_price in zip(kms, prices):
            predicted_price = theta0 + theta1 * (km / 1000)
            error = predicted_price - actual_price
            total_squared_error += error ** 2

        mse = total_squared_error / m
        rmse = math.sqrt(mse)

        print(f"\nModel Evaluation:")
        print(f" - Mean Squared Error (MSE): {mse:.2f}")
        print(f" - Root Mean Squared Error (RMSE): {rmse:.2f} €")

    except Exception as e:
        print(f"Error during evaluation: {e}")

def plot_graph(path, thetas):
    """
    Plots the linear regression line along with the dataset points.

    Parameters:
        path (str): Path to the CSV file containing the dataset
        (columns: km, price).

        thetas (str): Path to the text file containing the trained
        theta0 and theta1 values.

    Displays:
        A scatter plot of the dataset and the regression line.
    """
    df = pd.read_csv(path)
    with open(thetas, 'r') as f:
        line = f.read()
        theta0, theta1 = map(float, line.strip().split(','))
    kms = df["km"].tolist()
    prices = df["price"].tolist()
    if not kms or not prices:
        print("Empty dataset.")
        return
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


def print_menu():
    """
    Displays the menu options for the user.
    """
    print("#---------------------#")
    print("|        Menu :       |")
    print("|1. Train a Model     |")
    print("|2. Predict a price   |")
    print("|3. Show graphic      |")
    print("|4. Mean Square Error |")
    print("|5. Quit              |")
    print("#---------------------#")


def main():
    """
    Main function that runs the menu loop and handles user choices.
    """
    while True:
        print_menu()
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
            if learning_rate <= 0 or learning_rate > 1:
                print("Invalid learning rate, Using default: 0.0001")
                learning_rate = 0.0001
            train(path, iterations, learning_rate)
        elif choice == "2":
            print("################")
            print("#Predict thetas#")
            print("################")
            predict(thetas)
        elif choice == "3":
            plot_graph(path, thetas)
        elif choice == "4":
            print("################")
            print("#Evaluate model#")
            print("################")
            evaluate_model(path, thetas)
        elif choice == "5":
            break
        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
