from sklearn.naive_bayes import CategoricalNB
from sklearn import preprocessing
# Data
chills = ['Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'Y']
running_nose = ['N', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y']
headache = ['mild', 'no', 'strong', 'mild', 'no', 'strong', 'strong', 'mild']
fever = ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y']
has_flu = ['N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y']
# Encode and train
le = preprocessing.LabelEncoder()
features = list(zip(le.fit_transform(chills),
                    le.fit_transform(running_nose),
le.fit_transform(headache),
le.fit_transform(fever)))
label = le.fit_transform(has_flu)
model = CategoricalNB()
model.fit(features, label)
# Predict
predicted = model.predict([[1, 0, 0, 1]]) # Y, N, mild, Y
print("Prediction:", le.inverse_transform(predicted)[0])
print("Accuracy:", model.score(features, label))
