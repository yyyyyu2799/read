import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_excel("Pokemon_data.xlsx", engine='openpyxl')  

# 数据清洗
df['type1'].replace(['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire',
                     'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison',
                     'Psychic', 'Rock', 'Steel', 'Water'],
                    list(range(1, 19)), inplace=True)


X = df.iloc[:, 2:].drop(columns=['type2','classfication','abilities'])
#标准化处理
X = (X - np.mean(X)) / np.std(X)


#计算相关系数
corr=X.corr()
corr=corr[['is_legendary']]
corr=corr.drop('is_legendary')

#取绝对值排序
corr=corr.apply(lambda x: abs(x))
corr=corr.sort_values('is_legendary',ascending=0)

print('采用的特征提取法：相关系数法\n')
print('is_legendary最相关的几个特征:\n', corr.head)

plt.figure(figsize=(10,10))
sns.heatmap(X.corr(), cmap='coolwarm', annot=False, fmt='.2f', xticklabels=1, yticklabels=1, linewidths=0.5)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.show()

