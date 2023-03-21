#  Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
#  Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
number_of_people = df[(df['population'] > 0) & (df['population'] < 500)]
average_home_value = number_of_people['median_house_value'].mean()

print(f'Средняя стоимость дома, где кол-во людей от 0 до 500 =  {round(average_home_value, 2)}')




