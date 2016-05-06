from __future__ import division
import sys
import os

__author__ = 'Emily Ahn and Elizabeth Hau'

def read_file(filename):
    """ Takes in a file name and reads it in as a list of words """
    with open(filename, 'r') as f:
        return f.read().split()
        
def preprocess_segments(segments):
    """ Preprocesses the segments to remove numbers after words, <sil>, <s>, </s>,
        [NOISE] and return a new list with the cleaned up data
    """
    new_list = []
    for word in segments:
        if not (word == '<sil>' or word == '<s>' or word == '</s>' or word == '[NOISE]'):
            if "(" in word:
                new_list.append(word.split("(")[0])
            else:
                new_list.append(word)
    return new_list

def filler_words(segments, filler='[SPEECH]'):
    """ Takes in a filler word to search for and a list of the hypothesis 
        segments and returns the % of the filler word's occurence . 
        The filler word parameter is optional, the default filler word to
        search for is 'um'
    """
    new_list = []
    if not filler == '[SPEECH]':
        filler = filler.lower()
    for word in segments:
        if "(" in word:
            new_list.append(word.split("(")[0])
        else:
            new_list.append(word)
    num_filler = new_list.count(filler)
    assert len(new_list) == len(segments)
    total_words = len(new_list)
    print 'total_words:', total_words
    print 'number of ', filler,'said:', num_filler
    percent = num_filler/total_words
    print 'percent of filler words', percent
    print 'compared to TED standard (0.005589%)', compare_to_standard(percent, 0.005589)
    return percent
    
def compare_to_standard(percent, standard):
    if percent < standard:
        print 'GOOD JOB. You don\'t use many filler words.'
    else:
        print 'Keep practicing! You still use too many filler words'

if __name__=='__main__':
    DATADIR = sys.argv[1]
    for f in os.listdir(DATADIR):
        if not f.startswith('.') and os.path.isfile(os.path.join(DATADIR, f)):
            print 'file is:', f
            filename = os.path.join(DATADIR, f)
            read = read_file(filename)
            preprocessed = preprocess_segments(read)
            print '*********** FILE: ', f, '****************'
            ums = filler_words(preprocessed)
            likes = filler_words(preprocessed, 'like')
            silences = filler_words(read, '<sil>')
            print '% of "um"s said ([\'SPEECH\'])', ums
            print '% of "like"s said', likes
            print '% of "<sil>"', silences