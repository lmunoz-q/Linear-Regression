import pandas as pd


path = "../ressources/data.csv"


def create_theta(lst: list):
    file = "theta0_theta1.txt"
    with open(file, 'w') as f:
        f.write(lst)


def estimate_prices(km, theta0, theta1):
    return theta0 + (theta1 * km)


def train(path):
    df = pd.read_csv(path)
    ret = []
    kms = df["km"].tolist()
    kms = [i / 1000 for i in kms]
    prices = df["price"].tolist()
    theta0 = 0
    theta1 = 0
    learning_rate = 0.0001
    iterations = 1000000
    len_kms = len(kms)

    for i in range(iterations):
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
    train()
