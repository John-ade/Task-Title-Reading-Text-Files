# Task-Title-Reading-Text-Files


# Read text from a file, and count the occurence of words in that text

# Read text from a file, and count the occurence of words in that text

f = open("story.txt", "r")
print(f.read())

# Read & count file content

def read_file_content(file):
    text = open("story.txt", "r")
    reader = text.read()

    for line in reader:
        line = line.strip()
        line = line.lower()
        line = line.strip("/n,.?")
    words = reader.split(" ")
    return words
    #print(words)
#read_file_contect()

def count_word():
    text = read_file_content("story.txt")
    counts ={}
    for word in text:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    for key in list(counts.keys()):
        print(key,":", counts[key])
print(count_word())
#
