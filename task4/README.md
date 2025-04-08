# 代码核心功能说明

## 一、代码功能概述
本代码实现了一个基于朴素贝叶斯算法的邮件分类器，能够对邮件进行垃圾邮件和普通邮件的分类。它通过以下步骤完成分类任务：
1. **文本预处理**：读取邮件文本，去除无效字符和长度为1的词。
2. **词库构建**：统计邮件中的高频词，构建词库。
3. **特征向量构建**：将每封邮件转换为基于词库的特征向量。
4. **模型训练**：使用朴素贝叶斯算法训练分类模型。
5. **邮件分类**：对未知邮件进行分类预测。

## 二、代码结构与功能模块

### （一）文本预处理模块
```python
def get_words(filename):
    """读取文本并过滤无效字符和长度为1的词"""
    words = []
    with open(filename, 'r', encoding='utf-8') as fr:
        for line in fr:
            line = line.strip()
            # 过滤无效字符
            line = re.sub(r'[.【】0-9、——。，！~\*]', '', line)
            # 使用jieba.cut()方法对文本切词处理
            line = cut(line)
            # 过滤长度为1的词
            line = filter(lambda word: len(word) > 1, line)
            words.extend(line)
    return words
```
- **功能**：读取邮件文件，去除无效字符（如标点符号、数字等），并使用`jieba`进行中文分词，同时过滤掉长度为1的词。
- **输入**：邮件文件路径`filename`。
- **输出**：经过预处理的词列表`words`。

### （二）词库构建模块
```python
def get_top_words(top_num):
    """遍历邮件建立词库后返回出现次数最多的词"""
    filename_list = ['邮件_files/{}.txt'.format(i) for i in range(151)]
    # 遍历邮件建立词库
    for filename in filename_list:
        all_words.append(get_words(filename))
    # itertools.chain()把all_words内的所有列表组合成一个列表
    # collections.Counter()统计词个数
    freq = Counter(chain(*all_words))
    return [i[0] for i in freq.most_common(top_num)]
```
- **功能**：遍历所有邮件文件，提取高频词，构建词库。
- **输入**：需要提取的高频词数量`top_num`。
- **输出**：出现次数最多的`top_num`个词组成的列表`top_words`。

### （三）特征向量构建模块
```python
vector = []
for words in all_words:
    word_map = list(map(lambda word: words.count(word), top_words))
    vector.append(word_map)
vector = np.array(vector)
```
- **功能**：将每封邮件转换为基于词库的特征向量。统计每封邮件中每个高频词的出现次数，形成特征向量。
- **输入**：词库`top_words`和所有邮件的词列表`all_words`。
- **输出**：特征向量矩阵`vector`。

### （四）模型训练模块
```python
# 0-126.txt为垃圾邮件标记为1；127-151.txt为普通邮件标记为0
labels = np.array([1]*127 + [0]*24)
model = MultinomialNB()
model.fit(vector, labels)
```
- **功能**：使用朴素贝叶斯算法训练邮件分类模型。
- **输入**：特征向量矩阵`vector`和对应的邮件标签`labels`。
- **输出**：训练好的分类模型`model`。

### （五）邮件分类模块
```python
def predict(filename):
    """对未知邮件分类"""
    # 构建未知邮件的词向量
    words = get_words(filename)
    current_vector = np.array(
        tuple(map(lambda word: words.count(word), top_words)))
    # 预测结果
    result = model.predict(current_vector.reshape(1, -1))
    return '垃圾邮件' if result == 1 else '普通邮件'
```
- **功能**：对未知邮件进行分类预测。
- **输入**：未知邮件文件路径`filename`。
- **输出**：预测结果，返回“垃圾邮件”或“普通邮件”。

## 三、代码运行流程
1. **文本预处理**：通过`get_words`函数对邮件文本进行预处理，提取有效词。
2. **词库构建**：调用`get_top_words`函数，提取高频词构建词库。
3. **特征向量构建**：根据词库，将每封邮件转换为特征向量。
4. **模型训练**：使用朴素贝叶斯算法训练邮件分类模型。
5. **邮件分类**：调用`predict`函数，对未知邮件进行分类预测。

## 四、代码运行结果
<img src="https://github.com/chf910/GetDemo1/blob/main/images/py41.png" width="800" alt="截图一">

# 增加模型评估指标，代码在文件1.py

<img src="https://github.com/chf910/GetDemo1/blob/main/images/py42.png" width="800" alt="截图二">
