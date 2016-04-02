#import audiotools as at
from pocketsphinx.pocketsphinx import *
from os import environ, path

MODELDIR = "/home/sravana/applications/pocketsphinx-python/pocketsphinx/model"

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

decoder = Decoder(config)
#make sure that your audio file has a wav format, sample format 16 bit PCM mono 
wavFile = open('test-hello.wav', 'rb')
#wavFile.seek(44)
'''
speechRec.decode_raw(wavFile)
result = speechRec.get_hyp()
print type(result)
print 'result is', result

print result[0]
'''

decoder.start_utt()
stream = wavFile
while True:
    buf = stream.read(1024)
    print buf
    if buf:
        print '\nbuf was true'
        decoder.process_raw(buf, False, False)
    else:
        break
    decoder.end_utt()
    hypothesis = decoder.hyp()
    print type(hypothesis)
    print hypothesis
    logmath = decoder.get_logmath()
    print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))

    print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
'''
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
