# Public Speaking Feedback Tool

Wellesley cs349 Final Project

Spring 2016

Elizabeth Hau & Emily Ahn

## Project Update 4/4

- Did you meet your first milestone? Did you change your milestone?

  1. Achieve successful queries into Pocketsphinx? **YES**
  2. Acquire a batch of gold standard audio files? 10 files for 20 mins each
    
    No we did not change our milestone.

- What have you finished so far? Include background reading, development, brainstorming, and results.

    We were able to successfully query pocketsphinx, pass in an audio file, and get the best hypotheses (transcription). Along the way, we had a lot of trouble working with the Decoder class and knowing what methods are available pocketsphinx in python. Ultimately, even though queries were successful, we had issues getting accurate (recognizable) transcriptions from audio files that we created. Our hypthesis for the poor transcriptions is that the sound quality of the files gets lost in the conversion between .wav and .raw files or that our sound files are not in the correct audio format.


- You should aim to have *some* results by the update. Describe them.
    
    We tried running pocketsphinx on the .raw files provided, .wav files we recorded ourselves, and .raw files converted from our .wav files. The transcriptions from the .raw files provided were fairly accurate, but this is not the case for our .wav files or .raw files.


- Are the results satisfactory? If they aren't, what do you plan to modify/add?

    

- Updates to your project plan, like goals and techniques that have changed since your proposal.
    1. research file formats and what sphinx needs
    2. try pocketsphinx on .mp3 files
    3. modify the acoustic model to keep filler words

- Difficulties or questions that I can help you with. If you're having code-related problems, note the file name and line numbers.


