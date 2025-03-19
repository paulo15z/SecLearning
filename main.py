print("BORA!")

import pandas as pd #•	Carregue o dataset usando a biblioteca Pandas em Python:

df = pd.read_csv('C:\DEPOSITO\MachineLearningCSV') 
                 
#•	Trate valores ausentes preenchendo-os com a mediana ou removendo linhas, se necessário:
df.fillna(df.median(), inplace=True)

#•	Converta features categóricas, como protocolo, para valores numéricos usando label encoding:
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

df["Protocol"] = label_encoder.fit_transform(df["Protocol"])




