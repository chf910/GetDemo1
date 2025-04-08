import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 模拟生成样本数据
# 假设你已经有了特征矩阵 X 和对应的标签向量 y
# 这里我们简单模拟一个样本不平衡的数据集
X, y = make_classification(n_samples=151, n_features=10, n_informative=5,
                           n_redundant=0, n_clusters_per_class=1,
                           weights=[0.84, 0.16], random_state=42)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化 SMOTE 类
smote = SMOTE(random_state=42)

# 进行过采样
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 初始化逻辑回归模型
model = LogisticRegression(random_state=42)

# 在过采样后的数据上训练模型
model.fit(X_train_resampled, y_train_resampled)

# 进行预测
y_pred = model.predict(X_test)

# 输出分类评估报告
report = classification_report(y_test, y_pred)
print(report)