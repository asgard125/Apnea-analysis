from .model import *

def calc():
    model = ApnoeModel()
    X, y = model.X, model.y

    scores = crossval_neunet(
        X, y, 4, [20, 20, 10], "relu", "sigmoid", "binary_crossentropy", "adam", 80, 5
    )
    mean_metric = sum(scores[i] for i in range(len(scores))) / len(scores)

    scores = crossval_forest(X, y, 4)
    mean_metric = sum(scores[i] for i in range(len(scores))) / len(scores)

    scores = crossval_catboost(X, y, 4)
    mean_metric = sum(scores[i] for i in range(len(scores))) / len(scores)
    
    res = "Вероятность наличния апноэ: "
    res += str(model.predict(1))

    return res 

