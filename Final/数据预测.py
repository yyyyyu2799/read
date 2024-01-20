from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
mpl.use('TkAgg')    #指示 Matplotlib 在其后续的图表渲染中使用 'TkAgg' 后端

# 导入数据集
df = pd.read_excel("Pokemon_data.xlsx", engine='openpyxl')  


# 数据清洗
df['type1'].replace(['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
                     'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison',
                     'Psychic', 'Rock', 'Steel', 'Water'],
                    list(range(1, 19)), inplace=True)

# 标准化并划分数据集
#数据筛选与标准化
target = 'is_legendary'     
X = df.iloc[:, 2:].drop(columns=[target,'type2','classfication','abilities'])  
X = (X - np.mean(X)) / np.std(X) 
Y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=18)
'''将数据集X和Y分成训练集和测试集,test_size=0.5表示50%的数据为训练集,另外50%为测试集'''


# 使用不同的预测模型精灵宝可梦是否为传奇精灵，并查看预测的正确率
machine_name = np.array(['rbf_svm', 'linear_svm', 'KNN'])
machine_x = np.array([1, 2, 3])
machine_score = np.array([])


# 1. rbf svm
model = SVC(kernel='rbf', C=1, gamma=0.1)
model.fit(X_train, y_train)
y_svmpred = model.predict(X_test)
machine_score = np.append(machine_score, metrics.accuracy_score(y_svmpred,y_test))

# 2. linear svm
model = SVC(kernel='linear', C=1, gamma=0.1)
model.fit(X_train, y_train)
y_lsvmpred = model.predict(X_test)
machine_score = np.append(machine_score, metrics.accuracy_score(y_lsvmpred, y_test))

# 3. KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X_train, y_train)
y_KNCpred = model.predict(X_test)
machine_score = np.append(machine_score, metrics.accuracy_score(y_KNCpred, y_test))


# 绘制三种算法预测正确率折线图

plt.plot(machine_x, machine_score*100)
plt.scatter(machine_x, machine_score*100, marker='*', color='red', s=80)
for x, y in zip(machine_x, machine_score*100):
    plt.text(x-0.07, y+0.3, '%.2f' % y, ha='left')
plt.title('The accuracy of three algorithms in predicting ' + target )
plt.xlabel('algorithm / model')
plt.xticks(machine_x, machine_name)
plt.ylabel('Accuracy(%) ')
plt.ylim(90, 100)
plt.show()



#改变test_size的取值，观察对正确率的影响
knn = KNeighborsClassifier()
y_list = np.array([])												# 存储正确率
test_list = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])	# 不同的test_size
for i in range(9):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_list[i], random_state=18)	# 划分数据集
    knn.fit(X_train, y_train.values.ravel())						# 训练
    y_KNCpred = knn.predict(X_test)									# 计算正确率
    y_list = np.append(y_list, [metrics.accuracy_score(y_KNCpred, y_test) * 100])
for i, v in enumerate(y_list):                                      # 添加点值
    plt.text(test_list[i]*100-0.8, v+0.1, '%.2f' % v)
plt.plot(test_list * 100, y_list, 'b-o')							# 绘制折线图
plt.title('Forecast of ' + target + ' when changing test_size')
plt.xlabel('test_size ( % )')
plt.ylabel('Accuracy ( % )')
plt.ylim(90, 100)
plt.show()


# 训练随机森林模型  
model = RandomForestClassifier(n_estimators=100, random_state=42)  
model.fit(X_train, y_train)  

# 输出特征重要性  
importance = model.feature_importances_  
indices = np.argsort(importance)[::-1] 

#绘制散点图显示每个特征的重要性
importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': model.feature_importances_})
print(importance_df)  
plt.scatter(X.columns, importance,s= list(map(lambda x: x * 1000, importance))  )  
plt.xlabel('Feature')  
plt.ylabel('Importance')
plt.xticks(rotation=90, fontsize=10)
plt.title('the importance of each feature on RandomForestClassifier')
plt.show()
