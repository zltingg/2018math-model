#导入数值计算库
import numpy as np
#导入科学计算库
import pandas as pd


def convertStrToNumber(name, data):
    mapping_keys = data[name].drop_duplicates().values
    mapping = {}
    for i in range(len(mapping_keys)):
        mapping[mapping_keys[i]] = i
    return data[name].map(mapping), mapping


train_path = "to_veirify_no_mapping.csv"
train = pd.read_csv(train_path,
                    header=0)

train.pop("iyear")

# ids = train.pop("eventid") 不要丢弃id
what = train.pop("Unnamed: 0")

# 处理省份信息provstate
train["provstate"], provstate_mapping = convertStrToNumber("provstate", train)

# 处理犯罪集团的名称gname
train["gname"], gname_mapping = convertStrToNumber("gname", train)

# 处理实体的名称corp1
train["corp1"], corp1_mapping = convertStrToNumber("corp1", train)

# 查看省份字符串到数字的映射
print(provstate_mapping)
# 查看犯罪集团字符串到数字的映射
print(gname_mapping)
# 查看实体字符串到数字的映射
print(corp1_mapping)



train.to_csv("to_verify.csv")
