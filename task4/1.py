import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification

# 模拟生成样本数据
# 假设你已经有了特征矩阵 X 和对应的标签向量 y
# 这里我们简单模拟一个样本不平衡的数据集
X, y = make_classification(n_samples=151, n_features=10, n_informative=5,
                           n_redundant=0, n_clusters_per_class=1,
                           weights=[0.84, 0.16], random_state=42)

# 初始化 SMOTE 类
smote = SMOTE(random_state=42)

# 进行过采样
X_resampled, y_resampled = smote.fit_resample(X, y)

# 打印采样前后的样本数量
print("采样前各类样本数量：", np.bincount(y))
print("采样后各类样本数量：", np.bincount(y_resampled))