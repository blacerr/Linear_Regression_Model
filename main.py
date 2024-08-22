import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Veriyi yukle
data = pd.read_csv('linear_regression.csv')

X = data[['X']] #Bagimsiz degisken
Y = data[['Y']] #Bagimli degisken

# Egitim ve test olarak ayir
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, test_size=0.33)

# Model olustur ve egit
lr = LinearRegression()
lr.fit(x_train, y_train)

# Tahminler
tahmin_train = lr.predict(x_train)
tahmin_test = lr.predict(x_test)

# Egitim ve test verilerini 'data' ya ekle
data['Tahminler'] = pd.NA
data.loc[x_train.index, 'Tahminler'] = tahmin_train
data.loc[x_test.index, 'Tahminler'] = tahmin_test

#Tahmin edilen ve gercek olan veriyi yazdir
print(data)
