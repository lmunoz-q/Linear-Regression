import pandas as pd


path = "../ressources/data.csv"
iterations = 1000000
learning_rate = 0.0001


def print_progress_bar(current, total, bar_length=30):
    """
    Displays a progress bar in the terminal to track training progress.

    Parameters:
    - current (int): The current iteration.
    - total (int): The total number of iterations.
    - bar_length (int): The length of the progress bar in characters.
    """
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rTraining: [{bar}] {percent * 100:.1f}%", end="", flush=True)


def create_theta(lst: list):
    """
    Saves the learned theta0 and theta1 values to a file.

    Parameters:
    - lst (list): A list containing two elements: theta0 and theta1.
    """
    file = "theta0_theta1.txt"
    try:
        with open(file, 'w') as f:
            f.write(f"{lst[0]},{lst[1]}")
    except Exception as e:
        print(f"Failed to save theta: {e}")
    print(f"\ntheta0 and theta1 was created in file : {file}\n")


def estimate_prices(km, theta0, theta1):
    """
    Estimates the price based on a linear regression model.

    Parameters:
    - km (float): The distance in kilometers (normalized).
    - theta0 (float): The intercept of the linear model.
    - theta1 (float): The slope of the linear model.

    Returns:
    - float: The estimated price.
    """
    return theta0 + (theta1 * km)


def train(path, iterations, learning_rate):
    """
    Trains a simple linear regression model using gradient descent.

    Parameters:
    - path (str): Path to the CSV file containing 'km' and 'price' columns.
    - iterations (int): Number of iterations for gradient descent.
    - learning_rate (float): The learning rate for gradient descent.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        return
    ret = []
    kms = df["km"].tolist()
    kms = [i / 1000 for i in kms]
    prices = df["price"].tolist()
    theta0 = 0
    theta1 = 0
    len_kms = len(kms)
    if not kms or not prices:
        print("Error: CSV file is empty or malformed.")
        return
    if len_kms != len(prices):
        print("The data.csv must contain same lenght of data")
        return

    for i in range(iterations):
        if i % 1000 == 0 or i == iterations - 1:
            print_progress_bar(i + 1, iterations)
        sum_error = 0
        sum_error_times_km = 0
        for x, y in zip(kms, prices):
            y_pred = estimate_prices(x, theta0, theta1)
            error = y_pred - y
            sum_error += error
            sum_error_times_km += error * x
            tmp_theta0 = learning_rate * (1 / len_kms) * sum_error
            tmp_theta1 = learning_rate * (1 / len_kms) * sum_error_times_km
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    ret.append(theta0)
    ret.append(theta1)
    create_theta(ret)


if __name__ == "__main__":
    train(path, iterations, learning_rate)
