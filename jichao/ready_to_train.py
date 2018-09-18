#导入科学计算库
import numpy
import pandas as pd
from sklearn.cluster import AffinityPropagation
from sklearn.preprocessing import Imputer
from collections import Counter

train_path = "after_mapping.csv"
train = pd.read_csv(train_path,
                    header=0)

train.pop("Unnamed: 0")

print(train.head())
print(train.keys())

ids = train.pop("eventid")

train = train.loc[(train["gname"] == 0)]

train.pop("gname")

X = train

impute = Imputer()
iris_X_prime = impute.fit_transform(X)
X = iris_X_prime

# imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
# imp.fit(X)
#
# print("完成fit")
#
# X = imp.transform(X)

print(X)

print("完成transform")

# 使用KNN近邻扩散进行聚类
# Compute Affinity Propagation
af = AffinityPropagation().fit(X)

print("完成AffinityPropagation().fit(X)")


# 找出五个最高的并输出
centers = af.cluster_centers_
labels = af.labels_
counter = Counter(labels)
five_top = counter.most_common(5)

print("最高的六个点")
print(five_top)


# 挑出这五个中心点
five_center = [
    af.cluster_centers_[five_top[0][0]],
    af.cluster_centers_[five_top[1][0]],
    af.cluster_centers_[five_top[2][0]],
    af.cluster_centers_[five_top[3][0]],
    af.cluster_centers_[five_top[4][0]]
]

print(five_center)


# cluster_centers_indices = af.cluster_centers_indices_
# n_clusters_ = len(cluster_centers_indices)


verify_path = "to_verify.csv"
verify = pd.read_csv(verify_path, header=0)
verify.pop("eventid")
verify.pop("Unnamed: 0")
verify.pop("gname")

impute2 = Imputer()
impute2 = impute2.fit(X)
verify_nan = impute.transform(verify)
verify = verify_nan


for i in range(0, 10):
    print("=====第 " + str(i) + "点")
    item = verify[i]
    for center in five_center:

        print("===item===")
        print(item)
        print("===center===")
        print(center)

        dist = numpy.sqrt(numpy.sum(numpy.square(item - center)))
        print(dist)

# print("predict")
# print(af.predict(verify))

# result = pairwise_distances_argmin_min(verify, five_center)



# cluster_centers_indices = af.cluster_centers_indices_
# labels = af.labels_
#
# n_clusters_ = len(cluster_centers_indices)



# print('Estimated number of clusters: %d' % n_clusters_)
#
# print("===af.affinity===")
# print(af.affinity)
#
# print("===af.affinity_matrix_===")
# print(af.affinity_matrix_)
#
# print("===af.cluster_centers_===")
# print(af.cluster_centers_)
#
# print("===af.cluster_centers_indices_===")
# print(af.cluster_centers_indices_)
#
# print("===af.convergence_iter===")
# print(af.convergence_iter)
#
# print("===af.damping===")
# print(af.damping)
#
# print("===labels===")
# print(labels)









