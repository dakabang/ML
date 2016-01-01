import csv
import random

def loadCsv(filename):
    lines = csv.reader(open(filename, 'rb'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def separateByClass(dataset):
    seperated = []
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in seperated):
            seperated[vector[-1]] = []
        seperated[vector[-1]].append(vector)
    return seperated



if __name__ == "__main__":
    filename = "data.csv"
    dataset = loadCsv(filename)
    print("Load data file {0} with {1} rows").format(filename, len(dataset))
