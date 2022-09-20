import math


def softmax(outputs):
    exponentiols = []
    for item in outputs:
        exponentiols.append(math.exp(item))
    sum_exponentiols = sum(exponentiols)
    probabilities = []
    for item in exponentiols:
        probabilities.append(item / sum_exponentiols)
    return probabilities


print(softmax([9, 7]))

# -------- LOSS -------


def loss_function(probs, labels):
    loss = 0
    if len(probs) != len(labels):
        raise IndexError("Labels and probabilities are to lang")
    for i in range(len(probs)):
        error = (labels[i]-probs[i])
        squardError = error**2
        loss += squardError
    return loss


outputs = [9, 7]
labels = [1, 0]
probs = [0.8, 0.2]

print(loss_function(softmax(outputs), labels))


'''
de Loss functie controleerd hoe veel zit je van de waardheid of
'''
