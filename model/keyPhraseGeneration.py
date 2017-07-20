import json
from watson_developer_cloud import ToneAnalyzerV3

toneAnalyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username="c96d2a10-470a-4d75-9b37-9885c8008fbb",
  password="kNNKuFCtV1gW"
)

with open('transcription.txt', 'r') as myfile:
    data = myfile.read().replace('\u2019', '').replace('\u2026', '')

toneJson = json.dumps(toneAnalyzer.tone(text=data), indent=2)

arrayData = json.loads(toneJson)
print(toneJson)
