import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Carregar os dados
data = pd.read_csv('sample_submission.csv')

# Ajuste os nomes das colunas
X = data.drop(columns=['SalePrice'])
y = data['SalePrice']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo 1: Regressão Linear
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

# Resultado do Modelo 1
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("Regressão Linear:")
print(f"MSE: {mse_lr:.2f}")
print(f"R²: {r2_lr:.2f}")

# Modelo 2: Regressão com Árvores de Decisão
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

# Resultado do Modelo 2
mse_dt = mean_squared_error(y_test, y_pred_dt)
r2_dt = r2_score(y_test, y_pred_dt)

print("\nÁrvore de Decisão:")
print(f"MSE: {mse_dt:.2f}")
print(f"R²: {r2_dt:.2f}")
