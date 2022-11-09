import pandas as pd
import requests
from pandas import DataFrame
import csv


df = DataFrame(data=None,columns=["专业名称","专业代码","专业大类","专业小类","操作"])
for i in range(1,4):
    url='http://kaoshi.edu.sina.com.cn/college/majorlist/'
     #必须加utf-8，否则乱码
    df_new= pd.read_html(url, encoding='utf-8')[1]
    # 删除行
    df_new=df_new.drop(index=0)
     #新的df添加列名
    df_new.columns=["专业名称","专业代码","专业大类","专业小类","操作"]

     #数据合并
    df = pd.concat([df,df_new])
    print("第{page}页抓取完成".format(page = i))


#修改列数据类型
df["专业代码"] = df["专业代码"].astype(int)
#重置
df=df.reset_index(drop=True)

#输出csv
#df.to_csv('./major.csv',encoding='gbk',index=0)
print(df)


