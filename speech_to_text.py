#import audiotools as at
from pocketsphinx.pocketsphinx import *
from os import environ, path

MODELDIR = "/home/sravana/applications/pocketsphinx-python/pocketsphinx/model"
DATADIR = "/home/sravana/applications/pocketsphinx-python/pocketsphinx/test/data"
#E.g:
#http://www.repository.voxforge1.org/downloads/Main/Trunk/AcousticModels/Sphinx/voxforge-en-r0_1_3.tar.gz
#hmmd = '/<your_path>/models/voxforge-en-r0_1_3/model_parameters/voxforge_en_sphinx.cd_cont_3000'
hmmd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/en-us'
# http://sourceforge.net/projects/cmusphinx/files/Acoustic and Language Models/US English HUB4 Language Model/HUB4_trigram_lm.zip
#lmd = '/<your_path>/models/language_model.arpaformat.DMP'
lmd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/en-us.lm.bin'
# http://downloads.sourceforge.net/project/cmusphinx/Acoustic and Language Models/US English HUB4 Language Model/cmudict.hub4.06d.dict.zip
#dictd = '/<your_path>/models/cmudict.hub4.06d.dict'
dictd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/cmudict-en-us.dict'

# create a decoder
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))

#decoder = Decoder(config)
#make sure that your audio file has a wav format, sample format 16 bit PCM mono 
#wavFile = open('seashells.raw', 'rb')
#wavFile.seek(44)
'''
speechRec.decode_raw(wavFile)
result = speechRec.get_hyp()
print type(result)
print 'result is', result

print result[0]
'''
# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()

# different audio files to test
#stream = open('FAR00083.wav', 'rb')
#stream = open('filler_words.wav', 'rb')
#stream = open('common_sents.wav', 'rb')

#stream = open(path.join(DATADIR, 'numbers.raw'), 'rb')
stream = open('/home/sravana/data/cslu_fae_corpus/eahn-hhau/09-educate.mp3','rb')
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

#actual for FR file
#actual = "well let\'s see this is gonna be a little bit easier here i work as a computer consultant with a company called kpmg peat marwick and i\'ve been there for about two and a half years now that\'s gone pretty well i\'m thinking about doing some different things like getting into the multimedia area and let\'s see"

#actual for common sents
#actual = "she bought a skirt for him to wear to the party I want something hot to drink she is very busy he can be counted on I don\'t want to fail my exams"
actual = "um I want something hot to drink so I went to a coffee shop and ordered um hot coffee and hot chocolate then i felt better"
actual_list = actual.split()

print 'Actual:', actual_list
''' *************** DISCOVERY SO FAR 4/14/2016 ***************************
    The filler words seem to be marked as [SPEECH] in the hypothesis
    *********************************************************************
'''
'''
decoder.start_utt()
stream = wavFile
while True:
    buf = stream.read(1024)

    if buf:
 #       print '\nbuf was true'
        decoder.process_raw(buf, False, False)
    else:
        break
    decoder.end_utt()
    hypothesis = decoder.hyp()
  #  print type(hypothesis)
   # print hypothesis
    logmath = decoder.get_logmath()
    print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))

    print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

# Access N best decodings.
print ('Best 10 hypothesis: ')
for best, i in zip(decoder.nbest(), range(10)):
        print (best.hypstr, best.score)

        stream = open(path.join(DATADIR, 'goforward.mfc'), 'rb')
        stream.read(4)
        buf = stream.read(13780)
        decoder.start_utt()
        decoder.process_cep(buf, False, True)
        decoder.end_utt()
        hypothesis = decoder.hyp()
        print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", hypothesis.prob)
'''
