import pandas as pd


path = "../ressources/data.csv"
iterations = 1000000
learning_rate = 0.0001


def print_progress_bar(current, total, bar_length=30):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rTraining: [{bar}] {percent * 100:.1f}%", end="", flush=True)



def create_theta(lst: list):
    file = "theta0_theta1.txt"
    with open(file, 'w') as f:
        f.write(f"{lst[0]},{lst[1]}")


def estimate_prices(km, theta0, theta1):
    return theta0 + (theta1 * km)


def train(path, iterations, learning_rate):
    df = pd.read_csv(path)
    ret = []
    kms = df["km"].tolist()
    kms = [i / 1000 for i in kms]
    prices = df["price"].tolist()
    theta0 = 0
    theta1 = 0
    len_kms = len(kms)

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
            theta0 = theta0 - tmp_theta0
            theta1 = theta1 - tmp_theta1
    ret.append(theta0)
    ret.append(theta1)
    create_theta(ret)


if __name__ == "__main__":
    train(path, iterations, learning_rate)
