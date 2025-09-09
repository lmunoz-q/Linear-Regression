# Linear Regression (ft_linear_regression)

```diff
+ Final Score: 125/100
```
## 📌 Project Overview

This project implements a **simple linear regression algorithm from scratch** using:

- A CSV file (`resources/data.csv`) with `km` (mileage) and `price` columns
- **Gradient descent** to learn `theta0` (intercept) and `theta1` (slope)
- Normalization of mileage values to improve numerical stability
- A **command-line interface (CLI)** to train the model, make predictions, and visualize the data
- Model persistence: learned parameters are saved in `theta0_theta1.txt`

---

## ✨ Key Features

- 🔄 **Training loop** with live **progress bar** in terminal
- 🧠 Custom implementation of **gradient descent** with adjustable learning rate and iteration count
- 📈 **Graphical visualization** of training results (real data + predicted line)
- 🧪 Easy-to-use CLI interface to:
  - Train the model
  - Predict a price based on mileage
  - Show graph
  - Exit
- 💾 Model saved and reused automatically between sessions
- 📁 Well-structured code split into `train.py`, `predict.py`, `utils.py`, and `linear_regression.py`

---

## ⚙️ Main Functions

### `train(path, iterations, learning_rate)`
- Trains the linear regression model using gradient descent
- Displays a progress bar during training
- Saves `theta0` and `theta1` to `theta0_theta1.txt`

### `predict(path_to_theta)`
- Prompts the user for a mileage
- Uses saved `theta0` and `theta1` to estimate and display the car price

### `plot_graph(path_csv, path_theta)`
- Visualizes the original data and the regression line using `matplotlib`

---

## 🖥️ Bonus: Interactive CLI

The `linear_regression.py` script includes a user-friendly terminal interface:

1. Train a Model
2. Predict a Price
3. Show Graphic
4. Quit

This lets users train, predict, or visualize with **no need to modify code**.

---

## 🧪 Sample Output

```bash
python3 linear_regression.py
```

Then choose:
- `1` → Train the model (input iterations & learning rate)
- `2` → Predict a price from mileage
- `3` → Display the graph
- `4` → Include model evaluation metrics: **MSE**, **RMSE**, **R²**
- `5` → Exit

---

## 📊 Visualizing Gradient Descent

Below is a visual representation (GIF) of how gradient descent progressively adjusts the regression line:

![Gradient Descent in Action](https://upload.wikimedia.org/wikipedia/commons/e/e0/Gradient_descent.gif)


---

## ✅ Requirements

- Python 3
- `pandas`
- `matplotlib`

Install via:

```bash
pip install pandas matplotlib
```

---

## 🛠 Future Improvements

- Add model export as `.json` instead of `.txt`
- Add a script like `evaluate.py` to assess model performance
- Animate training (e.g., `matplotlib.animation`) to show the line adjusting in real-time

---

## ✅ Conclusion

This project is a complete implementation of **linear regression without libraries that do the work for you**.  
It is interactive, visual, and pedagogical — a solid base for more advanced machine learning projects.
