# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

one_hot = pd.DataFrame(data['whoAmI'].apply(lambda x: {'human': [1, 0], 'robot': [0, 1]}[x]).tolist(),
                       columns=['whoAmI_human', 'whoAmI_robot'])
data = pd.concat([data, one_hot], axis=1)
data.drop('whoAmI', axis=1, inplace=True)
print(one_hot)