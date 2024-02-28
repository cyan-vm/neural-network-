import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Read the data
datos = pd.read_excel("~/Downloads/salidas.xlsx")

# print(datos.head())


# Define mapping for encoding
encoding_mapping = {
    'Hombre': 1, 'Mujer': 0,  # Gender
    'No': 0, 'Si': 1           # Other binary features
}

datos_encoded = datos.replace(encoding_mapping)

# Randomly assign 0 or 1 to the 'depresion' feature
datos_encoded['depresion'] = np.random.randint(0, 2, size=len(datos_encoded))

x  = np.arange(10).reshape(-1, 1)
x
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])


# print(datos_encoded)

