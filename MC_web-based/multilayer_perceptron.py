import random as rd
import numpy as np

def tanh_d(x):
    return 1 - np.tanh(x)**2

class NeuralNetwork:
    def __init__(self, input_layer, hidden_layers, output_layer):
        self.input_nodes = input_layer
        self.hidden_layers = hidden_layers
        self.output_nodes = output_layer
        self.learning_rate = 0.01

        rd.seed(1)
        #Matrice dei pesi degli archi tra input layer ed hidden layer
        self.weight_ih = [[rd.random()*2-1 for x in range(0, input_layer)] for y in range(0, hidden_layers[0])]
        
        #Matrice dei pesi degli archi tra hidden layer ed output layer
        self.weight_hh = [[rd.random()*2-1 for x in range(hidden_layers[0])] for y in range(hidden_layers[0])]
        
        #Matrice dei pesi degli archi tra hidden layer ed output layer
        self.weight_ho = [[rd.random()*2-1 for x in range(hidden_layers[len(hidden_layers) - 1])] for y in range(output_layer)]

        #Matrice dei bias relativi all'hidden layer
        self.bias_h = []
        for i in range(len(hidden_layers)):
	        self.bias_h.append([rd.random()*2-1 for x in range(hidden_layers[i])])

        #Matrice dei bias relativi all'output layer
        self.bias_o = [rd.random()*2-1 for x in range(output_layer)]
    
    def train(self, inputs, targets):
        output, hidden_matrix = self.feed_forward(inputs)
        self.back_propagation(inputs, targets, output, hidden_matrix)
        


    def feed_forward(self, inputs):
        hidden_matrix = np.dot(self.weight_ih, inputs)
        hidden_matrix = np.add(hidden_matrix, self.bias_h[0])
        for i in range(len(hidden_matrix)):
            hidden_matrix[i] = np.tanh(hidden_matrix[i])

        for j in range(1, len(self.hidden_layers)):
            hidden_matrix = np.dot(self.weight_hh, hidden_matrix)
            hidden_matrix = np.add(hidden_matrix, self.bias_h[j])
            for i in range(len(hidden_matrix)):
                hidden_matrix[i] = np.tanh(hidden_matrix[i])


        output = np.dot(self.weight_ho, hidden_matrix)
        output = np.add(output, self.bias_o)

        for i in range(len(output)):
            output[i] = np.tanh(output[i])
        return output, hidden_matrix
        
    def back_propagation(self, inputs, targets, output, hidden_matrix):
    
        #Calcolo dell'errore relativo all'output layer
        output_errors = np.subtract(targets, output)

        #Calcolo dell'output gradient
        gradients = output.copy()
        for i in range(len(gradients)):
            gradients[i] = tanh_d(gradients[i])
        gradients = np.dot(gradients, output_errors)
        gradients = np.dot(gradients, self.learning_rate)


        #Calcolo della variazione delle weight  hidden->output
        weights_ho_deltas = np.dot(gradients, np.transpose(hidden_matrix))
        
        #Adjust delle weights in base alla variazione
        self.weight_ho = np.add(self.weight_ho, weights_ho_deltas)
        #Asjustment delle variabili di bias in base alla loro variazione (gradients)
        np.add(self.bias_o, gradients)
        
        #Calcolo dell'errore relativo all'hidden layer
        hidden_errors = np.dot(np.transpose(self.weight_ho), output_errors)

        #Calcolo dell'hidden gradient
        hidden_gradient = hidden_matrix.copy()
        for i in range(len(hidden_gradient)):
            hidden_gradient[i] = tanh_d(hidden_gradient[i])
        hidden_gradient = np.dot(hidden_gradient, hidden_errors)
        hidden_gradient = np.dot(hidden_gradient, self.learning_rate)

        for j in range(0, len(self.hidden_layers) - 1):
            #Calcolo dell'errore relativo all'hidden layer
            hidden_errors = np.dot(np.transpose(self.weight_hh), hidden_errors)

            #Calcolo dell'hidden gradient
            hidden_gradient = hidden_matrix.copy()
            for i in range(len(hidden_gradient)):
                hidden_gradient[i] = tanh_d(hidden_gradient[i])
            hidden_gradient = np.dot(hidden_gradient, hidden_errors)
            hidden_gradient = np.dot(hidden_gradient, self.learning_rate)

            #Calcolo della variazione delle weight input->hidden
            weights_hh_deltas = np.dot(hidden_gradient, np.transpose(hidden_matrix))
            np.add(self.weight_hh, weights_hh_deltas)
            
        #Calcolo della variazione delle weight input->hidden
        weights_ih_deltas = np.dot(hidden_gradient, np.transpose(inputs))
        
        #Adjust delle weights in base alla variazione
        np.add(self.weight_ih, weights_ih_deltas)
        #Asjustment delle variabili di bias in base alla loro variazione (gradients)
        np.add(self.bias_h, hidden_gradient)
