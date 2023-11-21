import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import joblib

# Carregar o dataset
arquivo = 'credit.csv'
colunas = [
    'class', 'balance','duration','paymentStatus','purpose','amount','savings','currentEmployment','instalment','marital','guarantors','durationAddress','asset','age',
    'concurrentCredits','typeApartment','numberofCredits','occupation','dependents','telephone','worker'
]

data = pd.read_csv(arquivo, names=colunas)
# Codificação de rótulos (Label Encoding)
label_encoders = {}
for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Criar e treinar o modelo LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# Salvar o modelo e os encoders
joblib.dump(lda, 'lda_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')