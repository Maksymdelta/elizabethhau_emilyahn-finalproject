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
    
    We tried running pocketsphinx on the .raw files provided, .wav files we recorded ourselves, and .raw files converted from our .wav files. The transcriptions from the .raw files provided were fairly accurate, but this is not the case for our .wav files or .raw files. For example, in `seashells.wav`, Emily said `She sells seashells on the seashore` but the transcript we get back is the following:     
    `['<s>', 'sneaker', 'or', '<sil>', 'the(2)', 'shares', 'on', '<sil>', 'your(2)', 'own', '</s>']`. 

    Even when we convert `seashells.wav` to `seashells.raw`, the same transcript is returned. We also tried running pocketsphinx on a 20 second phone call `FAR00083.wav`. The outputted result is: `['<s>', 'up', '<sil>', 'on', '<sil>', 'that', '<sil>', '<sil>', 'one(2)', '<sil>', 'top(2)', '<sil>', 'that(2)', '<sil>', '<sil>', 'i', 'cannot', 'cut', 'out', 'all', 'right', '<sil>', 'but', 'pot', 'her', 'to(2)', '<sil>', 'but', '<sil>', '<sil>', 'the(2)', 'man', 'on', 'a', 'pole', '</s>']` whereas the actual transcription is `well let's see this is gonna be a little bit easier here i work as a computer consultant with a company called kpmg peat marwick and i've been there for about two and a half years now that's gone pretty well i'm thinking about doing some different things like getting into the multimedia area and let's see`.


- Are the results satisfactory? If they aren't, what do you plan to modify/add?
    
    No, the results were not satisfactory. 
    1. research file formats and what sphinx needs
    2. try pocketsphinx on .mp3 files
    3. modify the acoustic model to keep filler words

- Updates to your project plan, like goals and techniques that have changed since your proposal.
    
    The overall idea of the project has not changed. However, we did not anticipate to get such poor results from querying the sound files that we have created. Especially considering we will be providing most of our own sound files while running the system, our focus right now is to make sure we get a decent transcription when we provide an audio file to pocketsphinx.

- Difficulties or questions that I can help you with. If you're having code-related problems, note the file name and line numbers.

    Sound file conversions and file compressions-- is there something we are missing when we're either creating or converting our files that is causing the bad transcriptions?


