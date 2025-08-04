from train import estimate_prices

path = "theta0_theta1.txt"


def predict(path):
    """
    Predicts the price of a car based on user-input mileage using a
    linear regression model.

    Parameters:
        path (str): Path to the file containing trained
        theta0 and theta1 values.

    Behavior:
        - Prompts the user to input a mileage value.
        - Loads the thetas from the file.
        - Uses the regression formula to estimate the price.
        - Displays the predicted price in euros.

    Notes:
        - Mileage should be entered in kilometers.
        - The model assumes mileage normalization by dividing by 1000.
    """
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
