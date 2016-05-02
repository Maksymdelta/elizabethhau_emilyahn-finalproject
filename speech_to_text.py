#import audiotools as at
from pocketsphinx.pocketsphinx import *
from os import environ, path, listdir
import sys
import time
__author__ = 'Emily Ahn and Elizabeth Hau'

MODELDIR = "/home/sravana/applications/pocketsphinx-python/pocketsphinx/model"
DATADIR = "/home/sravana/data/cslu_fae_corpus/cs349"

hmmd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/en-us'
lmd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/en-us.lm.bin'
dictd = '/home/sravana/applications/pocketsphinx-python/pocketsphinx/model/en-us/cmudict-en-us.dict'

# create a decoder
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))

def write_hypothesis(outfile, segments):
    # writes the hypothesis file and calculates accuracy
    with open(outfile, 'w') as o:
        for word in segments:       
            o.write(word+' ')  
    o.close()  
    
def decode(datadir, filename):
    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    
    # different audio files to test
    #stream = open('FAR00083.wav', 'rb')
    #stream = open('filler_words.wav', 'rb')
    #stream = open('common_sents.wav', 'rb')
    #datadir = '/home/sravana/data/cslu_fae_corpus/eahn-hhau'
    #stream = open(path.join(DATADIR, 'numbers.raw'), 'rb')
    stream = open(path.join(datadir,filename),'rb')
    
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
    decoder.end_utt()
    segments = [seg.word for seg in decoder.seg()]
    f = 'hypothesis-'+filename.split('.')[0]+'.txt'
    print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    write_hypothesis(f, segments)
    return segments
    

    ''' *************** DISCOVERY SO FAR 4/14/2016 ***************************
        The filler words seem to be marked as [SPEECH] in the hypothesis
        *********************************************************************
    '''
    
if __name__=='__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument("datadir", help="directory where dataset is located", type=str)
    #parser.add_argument("filename", help="n for n-gram model", type=str)
    ##parser.add_argument("unit", help="word or character level model?", type=str, choices=['word', 'character'])
    ##parser.add_argument("lam", help="linear interpolation scaling factor between 0 and 1", type=float)
    #args = parser.parse_args()
    
    #print '\n\n***********************************************'
    #print '\ndata directory=', args.datadir, 'filename:', args.filename
    
    #datadir = "/home/sravana/data/cslu_fae_corpus/cs349"
    
    global filename
    start = time.time()
    # if one argument provided, it's a filename or a directory
    # and assume the data directory is the default data directory
    if len(sys.argv)== 2:
        #if ".wav" in sys.argv[1]:
        filename = sys.argv[1]
        decode(DATADIR, filename)
        #else: # directory name provided, decode every file in the data directory
        #    for f in os.listdir(DATADIR):
        #        if not f.startswith('.') and os.path.isfile(os.path.join(DATADIR, f)):
        #            decode(DATADIR, f)
    elif len(sys.argv)==3:
        # if two arguments provided, the first argument will be the data directory and the second the filename
        datadir = sys.argv[1]
        filename = sys.argv[2]
        decode(datadir, filename)
    else:
        # if no args provided, ask for a filename and assume the datadir is the default data directory
        #f = raw_input('Enter a filename: ')
        #decode(DATADIR, f)
        for f in listdir(DATADIR):
            if not f.startswith('.') and path.isfile(path.join(DATADIR, f)):
                decode(DATADIR, f)
        
    
    end = time.time()
    print 'time elapsed:', (end - start)
