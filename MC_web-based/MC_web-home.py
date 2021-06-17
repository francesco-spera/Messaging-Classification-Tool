import os
import multilayer_perceptron as nn
import pandas as pd
import numpy as np
import random as rd
import pickle as p
from werkzeug.utils import secure_filename
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

app.config['CSV_UPLOADS'] = #inserire path assoluto della cartella 'csv' in modo da fare l'upload del file preso in input
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    		return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST", "GET"])
def index():
	if request.method == "POST":
		layers = request.form.get("layers")
		
		if 'csv' not in request.files:
			print('No file part')
			return redirect(request.url)
            
		csv_file = request.files['csv']
		
		if csv_file.filename == '':
			print('No selected file')
			return redirect(request.url)
		
		if csv_file and allowed_file(csv_file.filename):
			filename = secure_filename(csv_file.filename)
			csv_file.save(os.path.join(app.config['CSV_UPLOADS'], filename))
		
		if not layers:
			try:
				f = open('serialization/brain.pickle', 'rb')
				brain = p.load(f)
			except:
				print('serialization problem')
			
			with open(os.path.join(app.config['CSV_UPLOADS'], csv_file.filename)) as f:
				input_test = pd.read_csv(f)
			
			dummies_target_TAG = pd.get_dummies(input_test.TAG)
			merged = pd.concat([input_test, dummies_target_TAG], axis='columns')
			
			if input_test['TAG'][1] == 'I':
				final = merged.drop(columns=['TAG', 'I'], axis='columns')
			elif input_test['TAG'][1] == 'V':
				final = merged.drop(columns=['TAG', 'V'], axis='columns')
			elif input_test['TAG'][1] == 'A':
				final = merged.drop(columns=['TAG', 'A'], axis='columns')
			elif input_test['TAG'][1] == 'F':
				final = merged.drop(columns=['TAG', 'F'], axis='columns')
				
			input_test = final.to_numpy()
			
			count_a = 0
			count_f = 0
			count_i = 0
			count_v = 0
			count_u = 0
			
			for index in range(len(input_test)):
				outputs, hidden_matrix = brain.feed_forward(input_test[index])
				max_index = np.argmax(outputs)
				if max_index == 0:
					count_a += 1
				elif max_index == 1:
					count_f += 1
				elif max_index == 2:
					count_i += 1
				elif max_index == 3:
					count_v += 1
				else:
					count_u += 1
			
			try:
				f = open('serialization/brain.pickle', 'wb')
				p.dump(brain, f)
			except:
				print('serialization problem')
				
			rate_a = "{0:.2f}".format(count_a*100/len(input_test))
			rate_f = "{0:.2f}".format(count_f*100/len(input_test))
			rate_i = "{0:.2f}".format(count_i*100/len(input_test))
			rate_v = "{0:.2f}".format(count_v*100/len(input_test))
			rate_u = "{0:.2f}".format(count_u*100/len(input_test))

			audio_p = str(rate_a) + '% audio'
			file_p = str(rate_f) + '% file'
			image_p = str(rate_i) + '% image'
			video_p = str(rate_v) + '% video'
			unk_p = str(rate_u) + '% unknown'
			
			len_in = len(input_test)
			len_in = str(len_in) + 'rows'
			
			return render_template('MC_web-home.html', flag0 = 1, audio_p=audio_p, file_p=file_p, image_p=image_p, video_p=video_p, unk_p=unk_p, )
		else:
			nodes = request.form.get("nodes")
			epochs = request.form.get("epochs")
			
			with open(os.path.join(app.config['CSV_UPLOADS'], csv_file.filename)) as f:
				training_targets = pd.read_csv(f)
			
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
        	
			return render_template('MC_web-home.html', flag1 = 1, output_train="THE NEURAL NETWORK HAS BEEN TRAINED")
	else:
		return render_template('MC_web-home.html')
