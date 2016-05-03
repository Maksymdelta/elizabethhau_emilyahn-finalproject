from __future__ import division
from pocketsphinx.pocketsphinx import *
from os import environ, path, listdir
import sys
import time
from analyze_text import *

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
    # writes the hypothesis file
    with open(outfile, 'w') as o:
        for word in segments:       
            o.write(word+' ')  
    o.close()  
    
def decode(datadir, filename):
    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    
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
        
if __name__=='__main__':
    global filename
    start = time.time()
    # if one argument provided, it's a filename 
    # and assume the data directory is the default data directory
    print "LENGTH OF SYS ARGV:", len(sys.argv)
    
    if len(sys.argv)== 2:
        filename = sys.argv[1]
        segments = decode(DATADIR, filename)
        new_list = preprocess_segments(segments)
        #print 'new list is:', new_list
        filler_words(new_list)
    elif len(sys.argv)==3:
        # if two arguments provided, the first argument will be the data directory and the second the filename
        datadir = sys.argv[1]
        filename = sys.argv[2]
        segments = decode(datadir, filename)
        new_list = preprocess_segments(segments)
        #print 'new list is:', new_list
        print '% of ums:', filler_words(new_list)
    else:
        # if no args provided, run the decoder on all files in the default DATADIR
        for f in listdir(DATADIR):
            if not f.startswith('.') and path.isfile(path.join(DATADIR, f)):
                decode(DATADIR, f)
    end = time.time()
    print 'time elapsed:', (end - start)
