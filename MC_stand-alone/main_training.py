import multilayer_perceptron as nn
import pandas as pd
import numpy as np
import random as rd
import pickle as p
from datetime import datetime


def training(csv_file, layers, nodes, epochs):
    training_targets = pd.read_csv(csv_file)
    training_targets_immagini = training_targets.iloc[0:2000, :]

    training_targets_video = training_targets.iloc[23725:25725, :]
    training_targets_immagini = training_targets_immagini.append(training_targets_video, ignore_index=True)

    training_targets_audio = training_targets.iloc[168701:170701, :]
    training_targets_immagini = training_targets_immagini.append(training_targets_audio, ignore_index=True)

    training_targets_file = training_targets.iloc[212240:214240, :]
    training_targets_immagini = training_targets_immagini.append(training_targets_file, ignore_index=True)

    training_targets = training_targets_immagini

    dummies_target_TAG = pd.get_dummies(training_targets.TAG)
    dummies_target_I = pd.get_dummies(training_targets.TAG)
    dummies_target_V = pd.get_dummies(training_targets.TAG)
    dummies_target_A = pd.get_dummies(training_targets.TAG)
    dummies_target_F = pd.get_dummies(training_targets.TAG)

    merged = pd.concat([training_targets, dummies_target_TAG], axis='columns')
    final = merged.drop(columns=['TAG', 'A', 'F', 'I', 'V'], axis=1)
    training_input = final.to_numpy()
    targets = dummies_target_TAG.to_numpy()

    input_neurons = len(training_input[0])
    n_hidden_layers = int(layers)
    n_hidden_nodes = int(nodes)
    hidden_layers = [n_hidden_nodes for x in range(n_hidden_layers)]
    output_neurons = 4
    epochs = int(epochs)

    try:
        f = open('serialization/brain.pickle', 'rb')
        brain = p.load(f)
    except:
        brain = nn.NeuralNetwork(input_neurons, hidden_layers, output_neurons)

    for i in range(epochs):
        rd.seed(1)
        index = rd.randint(0, len(training_input))
        brain.train(training_input[index], targets[index])

    try:
        f = open('serialization/brain.pickle', 'wb')
        p.dump(brain, f)
    except:
        print('serialization problem')
