#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt

# 设置中文字体，防止图表乱码
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

print("配置好了！")


# In[3]:


# 读取文件并存入变量 df
df = pd.read_excel("餐厅订单信息.xlsx")

# 展示前 5 行数据给我们看
df.head()


# In[5]:


# 第一步：把每天的金额加起来
# 因为同一天有很多笔订单，如果不加起来，柱状图会叠在一起很难看
daily_data = df.groupby('日期')['消费金额'].sum().reset_index()

# 第二步：开始画图
plt.figure(figsize=(10, 6))
plt.bar(daily_data['日期'], daily_data['消费金额'], color='skyblue')

# 第三步：设置标题（记得把括号里换成你自己的信息）
plt.title('环国2501班-42号-吴东隅')
plt.xlabel('2026.4.6')
plt.ylabel('消费总额')

# 第四步：显示图表
plt.show()


# In[6]:


# 1. 还是用我们之前算好的每日总额数据 daily_data
plt.figure(figsize=(10, 6))

# 2. 把之前的 plt.bar 改成 plt.plot 就能画折线了
# marker='o' 是在折点上加个小圆圈，看着更清楚
plt.plot(daily_data['日期'], daily_data['消费金额'], marker='o', color='red', linestyle='-')

# 3. 设置标题和标签
plt.title('2501环国-42号-吴东隅')
plt.xlabel('2025.4.6')
plt.ylabel('消费总额')

plt.show()


# In[7]:


# 1. 先按“菜品类别”把金额加起来
category_data = df.groupby('菜品类别')['消费金额'].sum()

# 2. 开始画饼
plt.figure(figsize=(8, 8))
# autopct='%1.1f%%' 是为了让电脑自动算出百分比并显示在饼上
plt.pie(category_data, labels=category_data.index, autopct='%1.1f%%', startangle=140)

# 3. 设置标题
plt.title('2501环国-42号-吴东隅')

plt.show()


# In[8]:


import numpy as np

# 我们拿“消费金额”和“成本”这两列来做对比
actual = df['消费金额']
target = df['成本']

# 1. 相关系数 (Correlation Coefficient)
# 衡量两组数据是不是“同步变化”
corr = actual.corr(target)

# 2. 均方根误差 (RMSE)
# 衡量实际值偏离目标的程度
rmse = np.sqrt(((actual - target) ** 2).mean())

# 3. 标准化平均偏差 (NMB)
nmb = (actual - target).sum() / target.sum()

# 4. 标准化平均误差 (NME)
nme = (actual - target).abs().sum() / target.sum()

print(f"相关系数: {corr:.2f}")
print(f"均方根误差 (RMSE): {rmse:.2f}")
print(f"标准化平均偏差 (NMB): {nmb:.2f}")
print(f"标准化平均误差 (NME): {nme:.2f}")


# In[9]:


plt.figure(figsize=(8, 6))
plt.scatter(df['成本'], df['消费金额'], alpha=0.5, color='purple')
plt.title('2501环国-42号-吴东隅(散点图)')
plt.xlabel('成本')
plt.ylabel('消费金额')
plt.show()


# In[10]:


plt.figure(figsize=(8, 6))
plt.boxplot(df['消费金额'])
plt.title('2501环国-42号-吴东隅 (箱型图)')
plt.ylabel('金额')
plt.show()


# In[ ]:




