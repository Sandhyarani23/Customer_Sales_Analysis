from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Prepare features and target
X = data[['DayOfWeek']]
y = data['Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
