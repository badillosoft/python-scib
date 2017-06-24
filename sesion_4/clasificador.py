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
print clf.predict([[1, 0, 1, 1]])

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

oc = 0
oic = 0
gc = 0
gic = 0
dc = 0
dic = 0

for (x, y) in T:
    yp = clf.predict([x])[0]
    if y == 1:
        if y == yp:
            oc += 1
        else:
            oic += 1
    elif y == 2:
        if y == yp:
            gc += 1
        else:
            gic += 1
    else:
        if y == yp:
            dc += 1
        else:
            dic += 1

def porcentaje(c, ic):
    return 100 * float(c) / (c + ic)

print "Otakus %d | %d (%.2f%%)" % (oc, oic, porcentaje(oc, oic))
print "Godinez %d | %d (%.2f%%)" % (gc, gic, porcentaje(gc, gic))
print "Darks %d | %d (%.2f%%)" % (dc, dic, porcentaje(dc, dic))
print "Total: %d | %d (%.2f%%)" % ((oc + gc + dc), (oic + gic + dic), porcentaje(oc + gc + dc, oic + gic + dic))