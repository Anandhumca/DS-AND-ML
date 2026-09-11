#Load sklearn Libraries
#import libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error, r2_score
#Load Data
#load diabetes dataset
diabetesX,diabetesY=datasets.load_diabetes(return_X_y=True)
#split datasets
diabetesX = diabetesX[:,np.newaxis,2]
#split the data into training/testing sets
diabetesXtrain=diabetesX[:-20]
diabetesXtest=diabetesX[-20:]
#split the targets into training/testing sets
diabetesYtrain=diabetesY[:-20]
diabetesYtest=diabetesY[-20:]
#Creating the model
#create linear regression object
regr=linear_model.LinearRegression()
#train the model using training sets
regr.fit(diabetesXtrain,diabetesYtrain)
#Make prediction
#make predictions using the testing set
diabetesYpred=regr.predict(diabetesXtest)
#finding coefficients and mean square error
#coefficients
print("Coefficients:\n",regr.coef_)
#mean squared error
print("Mean squared error:\n",mean_squared_error(diabetesYtest,diabetesYpred))
#coefficient of determination:1 is perfect prediction
print("Coefficient of determination:",r2_score(diabetesYtest,diabetesYpred))
plt.scatter(diabetesXtest,diabetesYtest,color='black')
plt.plot(diabetesXtest,diabetesYpred,color='blue',linewidth=3)
plt.xticks()
plt.yticks()
plt.show()
