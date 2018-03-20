# -*- coding: utf-8 -*-

import json
import locale
import sys
from watson_developer_cloud import SpeechToTextV1

reload(sys)
sys.setdefaultencoding('utf8')

IBM_USERNAME = "73ebdc08-4ec6-4804-ba17-9131cfcff54a"
IBM_PASSWORD = "ve2B5p4W6SBy"
URL = "https://stream.watsonplatform.net/speech-to-text/api"

locale.setlocale(category=locale.LC_ALL, locale="French")

stt = SpeechToTextV1(username=IBM_USERNAME, password=IBM_PASSWORD, url=URL)
audio_file = open("test.ogg", "rb")


with open('transcript_result.json', 'w') as fp:
    print("OUI")
    result = stt.recognize(audio_file,
                        content_type="audio/ogg;codecs=vorbis",
                        timestamps=True,
                        model="fr-FR_BroadbandModel",
                        max_alternatives=2,
                        word_confidence=True)
    print("OK")
    json.dump(result, fp, indent=4, ensure_ascii=False)