import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

# 1. Load the new Weekly Dataset
df = pd.read_csv('Kandivali_Borivali_Weekly_Full.csv')

# 2. Convert text to numbers (Label Encoding)
le_stop = LabelEncoder()
le_day = LabelEncoder()
le_time = LabelEncoder()
le_weather = LabelEncoder()
le_traffic = LabelEncoder() # Added Traffic encoder
le_route_type = LabelEncoder() # Added Route (East/West/LinkRd) encoder

# Fit and Transform the data
df['stop_id'] = le_stop.fit_transform(df['Stop_Name'])
df['day_id'] = le_day.fit_transform(df['Day'])
df['time_id'] = le_time.fit_transform(df['Time_Slot'])
df['weather_id'] = le_weather.fit_transform(df['Weather'])
df['traffic_id'] = le_traffic.fit_transform(df['Traffic'])
df['route_type_id'] = le_route_type.fit_transform(df['Route'])

# 3. Select Features (Inputs) and Target (Output)
X = df[['Bus_No', 'route_type_id', 'stop_id', 'day_id', 'time_id', 'weather_id', 'traffic_id']]
y = df['Delay_Mins']

# 4. Train the Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save the Model and Encoders
with open('bus_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# We save all encoders in a dictionary so the App can use them later
encoders = {
    'stop': le_stop,
    'day': le_day,
    'time': le_time,
    'weather': le_weather,
    'traffic': le_traffic,
    'route_type': le_route_type
}

with open('encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)

print("------------------------------------------------")
print(" Model Trained Successfully on Weekly Data!")
print(f" Accuracy Score (R²): {model.score(X, y):.4f}")
print(" Files saved: 'bus_model.pkl' and 'encoders.pkl'")
print("------------------------------------------------")