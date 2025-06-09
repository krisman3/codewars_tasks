def read_file(file_path):
    words = {}

    with open(file_path) as f:
        curr_text = f.read()
        split_words = curr_text.split()
        for i in split_words:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

    max_word = None
    max_count = 0
    for word, count in words.items():
        if count > max_count:
            max_word = word
            max_count = count
    return max_word
    # In case you'd like to see the most common word + its count:

    # return max_word, max(words.values())


print(read_file('C:\\Users\\KIliev\\PycharmProjects\\Python_Tasks\\test_file.txt'))
