# Write the code to turn some 15+ word sentence into a list of words ...
my_sentence = "Write the code to turn some 15+ word sentence into a list of words ..."
def sentence2list(sentence):
    sentence_list = sentence.split()
    print(sentence_list)
sentence2list(my_sentence)