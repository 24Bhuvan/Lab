import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Step 1: Generate some sample data
np.random.seed(42)  
X = 2 * np.random.rand(100, 1)  
y = 4 + 3 * X + 2 * X**2 + np.random.randn(100, 1) 

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Transform the data for polynomial regression
poly_features = PolynomialFeatures(degree=2)  
X_train_poly = poly_features.fit_transform(X_train) 
X_test_poly = poly_features.transform(X_test) 

# Step 4: Create and train the polynomial regression model
model = LinearRegression()
model.fit(X_train_poly,y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test_poly)  

# Print model coefficients and intercept
print(f"Intercept: {model.intercept_}")  
print(f"Coefficients: {model.coef_}") 

# Step 6: Evaluate the model
mse = mean_squared_error(y_test, y_pred) 
print(f"Mean Squared Error: {mse}") 

# Step 6: Model Ploting
X_sorted = np.sort(X_test, axis=0) 
y_sorted_pred = model.predict(poly_features.transform(X_sorted))  
plt.scatter(X_test, y_test, color='blue', label='Actual Data')  
plt.plot(X_sorted, y_sorted_pred, color='red', linewidth=2, label='Polynomial Fit')  
plt.xlabel("X")  
plt.ylabel("y")  
plt.legend() 
plt.title("Polynomial Regression Model") 
plt.show() 