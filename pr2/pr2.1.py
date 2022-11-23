import numpy as np
import pandas as pd



def pr21():
    a = int(input())
    summary = a
    squarenumber = 0 + abs(a ** 2)
    while summary != 0:
        a = int(input())
        summary = summary + a
        squarenumber = squarenumber + abs(a) ** 2
        if summary == 0:
            break
    print(squarenumber)


def pr22():
    N = int(input())
    l1 = []
    for i in range(1, N + 1):
        l1 += str(i) * i
    for i in range(N):
        print(l1[i], end=' ')


def pr23():
    x = int(input('Введите размерность квадратной матрицы: '))
    matrix = np.random.rand(x, x)
    lst = []
    print("Исходная матрица: ")
    print(matrix)
    print("\nМатрица построчно: ")
    for i in range(x):
        for j in range(x):
            lst.append(matrix[i, j])
    vctr = np.array(lst)
    print(vctr)


def pr24():
    a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    newMass = []
    newMass.append(b[0])
    check = False
    for i in range(len(b)):
        for j in range(len(newMass)):
            if b[i] != newMass[j]:
                check = True
            else:
                check = False
                break
        if check:
            newMass.append(b[i])
    dict = {}
    for i in range(len(newMass)):
        sum = 0
        for j in range(len(b)):
            if newMass[i] == b[j]:
                sum += a[j]
        dict.update({newMass[i]: sum})
    print(dict)


def pr25():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(data.data)


def pr26():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab)


def pr27():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab.info())


def pr28():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab.isna().sum())


def pr29():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab.loc[(newtab.HouseAge > 50) & (newtab.Population > 2500)].to_string())


def pr210():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab.MedHouseVal.max())
    print(newtab.MedHouseVal.min())


def find_mean(x):
    mean = x.mean()
    print(x.name, mean)
    return x


def pr211():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    medvalue = pd.DataFrame({data.target_names[0]: data.target})
    newtab = pd.concat([data.data, medvalue], axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    print(newtab.apply(find_mean, axis=0))


pr211()
