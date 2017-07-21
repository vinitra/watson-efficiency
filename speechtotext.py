import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username= "94f0b588-a25c-4b16-be77-e289cda0eabb",
    password= "pCtYl22okSFs",
    x_watson_learning_opt_out=False
)

print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), '/Users/antara.palit@ibm.com/Downloads/911_Call.wav'),
          'rb') as audio_file:
    s = (json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', 

        #timestamps=True,
        #word_confidence=True
        ),
        indent=2))
s = s.split()
for word in s:
	if word == '"transcript"':
   		print ("test")
   		beg = s.index(word)
   		end = s.index('"', beg + 16)
   		final = (s.substring(beg + 15, end))

f = open("text_transcript.txt", "w")
f.write(final)
f.close()

   		

