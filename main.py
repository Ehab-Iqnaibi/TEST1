input_text = """
One day a rabbit was boasting about,how fast he could run.
He was laughing at the turtle for being so slow. Much to the
rabbit’s surprise, the turtle challenged him to a race. The rabbit
thought this was a good joke and accepted the challenge. The fox
was to be the umpire of the race. As the race began, the rabbit
raced way ahead of the turtle, just like everyone thought.
The rabbit got to the halfway point and could not see the turtle
anywhere. He was hot and tired and decided to stop and take a short
nap. Even if the turtle passed him, he would be able to race to the
finish line ahead of him. All this time the turtle kept walking step
by step by step. He never quit no matter how hot or tired he got.
He just kept going.
However, the rabbit slept longer than he had thought and woke up.
He could not see the turtle anywhere! He went at full speed to
the finish line but found the turtle there waiting for him.
""".lower()
"""
TODO:
1. unify case, i.e., ==> lower done
2. remove irrelevant words, the, a, is, was,
3. remove propositions
"""
irrelevant_words = {".", "," , "\n", " the ", " a ", " and ",
" is ", " was ", " he ", " at ", " to ", " for ", " can ", " this ", " we ", " you "
                    , " or ", " i ", " an ", " but ", " so ", " yes ", " no "}
for iw in irrelevant_words:
  input_text = input_text.replace(iw, " ")
print(input_text)
word_list = input_text.split(" ")
print(word_list)
word_histogram = {
}
for word in word_list:
  if word not in word_histogram.keys():
    word_histogram[word] = 1
  else:
    word_histogram[word] = word_histogram[word] + 1
word_histogram.pop("")
print(word_histogram)