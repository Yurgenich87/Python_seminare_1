#Задача 42: Узнать какая максимальная households в зоне минимального значения population.
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
minimum_population = df[df['population'] == df['population'].min()]
print(f"Минимальное значение 'population' = {df['population'].min()}")
print(f"Максимальная значение 'households' в зоне минимального значения 'population' = "
      f"{minimum_population['households'].max()}")
