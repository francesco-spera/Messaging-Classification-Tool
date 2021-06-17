import pandas as pd
import numpy as np
import pickle as p


def testing(csv_path):
	try:
		f = open('serialization/brain.pickle', 'rb')
		brain = p.load(f)
		f.close()
	except:
		print('deserialization problem ')

	input_test = pd.read_csv(csv_path)
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
		f.close()
	except:
		print('serialization problem post')

	rate_a = "{0:.2f}".format(count_a * 100 / len(input_test))
	rate_f = "{0:.2f}".format(count_f * 100 / len(input_test))
	rate_i = "{0:.2f}".format(count_i * 100 / len(input_test))
	rate_v = "{0:.2f}".format(count_v * 100 / len(input_test))
	rate_u = "{0:.2f}".format(count_u * 100 / len(input_test))

	audio_p = str(rate_a) + '% audio '
	file_p = str(rate_f) + '% file'
	image_p = str(rate_i) + '% image'
	video_p = str(rate_v) + '% video'
	unk_p = str(rate_u) + '% unknown'

	return audio_p, file_p, image_p, video_p, unk_p, len(input_test)
