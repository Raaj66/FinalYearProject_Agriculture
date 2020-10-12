import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
dataset = pd.read_excel('Agri_Fertilizers_Used.xls')

dataset = dataset.values

Y = dataset[0:, 3:4]
X = dataset[:, [1,3,4,5]]



X=list(X)
print(X)


X_trian, X_test, Y_train, Y_test = train_test_split(X, Y,  random_state=42)



model = LinearRegression()
model.fit(X_trian, Y_train)

X_test=list(X_test)
#print(X_test)
df=pd.DataFrame(X_test,columns=["Crop", "A", "B","C"])
df.sort_values('Crop')
#print(df)
final_df = df.sort_values(by=['Crop'], ascending=False)
print("final df",final_df)

final_df=np.array(final_df)
predict = model.predict(final_df)
print("Final Predict",predict)
predict=list(predict)
Tea=predict[0:4]  #tea 0.9
print("Tea",Tea)  # 4
Oilseeds=predict[5:7]   #0.8
print("Oil",Oilseeds)
###8,10
# sugercane=predict[11,16]   ##0.6
# print("sugercane",sugercane)
Millets=predict[17,21]      #0.5
print("millets",Millets)
Maize=predict[22,24]     #0.4
print("Maize",Maize)
Rice=predict[25,30]
print("Rice",Rice)     #0.3
Groundnut=predict[31,41]
print("Ground",Groundnut) #0.2
print("dddd")
Bajra=predict[42,47]
print("Bajra",Bajra)  #0.12
Sorghum=predict[48,54]
print("Sorghum",Sorghum) #0.11
Wheat=predict(55,70)
print("Wheat",Wheat)  #0.10
