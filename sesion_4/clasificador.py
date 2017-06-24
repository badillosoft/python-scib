from sklearn.neural_network import MLPClassifier

# Otaku: 1
# Godinez: 2
# Darks: 3

X = [
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 1]
]

Y = [
    1,
    2,
    3,
    2,
    3,
    2,
    1,
    3,
    2,
    3,
    3,
    2,
    3,
    2,
    3,
    3,
    1,
    1,
    2,
    1,
    2,
    3
]

print len(X), len(Y)

# Crea un clasificador de tipo MLP
clf = MLPClassifier()

# Ajusta los datos de entramiento para aprender
clf.fit(X, Y)

# En base a su aprendizaje predecimos
# que pasa con el X = [1, 0, 1, 1]
# (La respuesta fue [2] - Godinez)
print clf.predict([1, 0, 1, 1])

T = [
    ([1, 0, 0, 0], 3),
    ([1, 0, 1, 0], 2),
    ([1, 1, 0, 0], 1),
    ([1, 1, 0, 0], 1),
    ([1, 0, 1, 0], 3),
    ([1, 0, 1, 1], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 0, 1], 3),
    ([1, 0, 0, 0], 1),
    ([1, 1, 0, 0], 2),
    ([1, 0, 0, 0], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 0, 0], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 1, 1], 2),
    ([1, 0, 1, 1], 2),
    ([1, 1, 1, 1], 2),
    ([1, 1, 1, 1], 1),
    ([1, 0, 1, 1], 2),
    ([1, 0, 0, 0], 3),
    ([1, 0, 0, 0], 1),
]

def rol(i):
    if i == 1:
        return "Otaku"
    elif i == 2:
        return "Godinez"
    else:
        return "Dark"

for (x, y) in T:
    