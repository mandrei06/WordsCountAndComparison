import string

def print_index(f_obj):
    fd = open("lab_main_words.txt")
    MAIN_WORDS = get_words(fd)

    """"# 1. create an empty dictionary and call it index_dict"""
    index_dict = dict()
    """# 2. create a variable named line_no and set its value to 0"""
    line_no=0

    for line in f_obj:
        line_no += 1
        line = line.strip()
        word_list = line.split()
        # 3. use for loop to go through word_list list
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            # 4. check if the word in the MAIN_WORDS
            if word in MAIN_WORDS:
                if word in index_dict:
                    index_dict[word]+=line_no
                else:
                    index_dict[word]=line_no
                # 4.1 if so, check if word is in the dictionary you created in step 1
                # 4.2 if it is, then use the word as the key and the line to key as its value
                # 4.3 otherwise, add a new key and value the dictionary, key is the word and value is the line

    pretty_print_dict(index_dict)

# This function receives a dictionary containint word indices
# and print them to the screen
def pretty_print_dict(index_dict):
    index_lst = [item for item in index_dict.items()]
    index_lst.sort()
    print(index_lst)
    for word, line_set in index_lst:
        print(word,line_set)
        line_lst = [l for w,l in index_lst]
        line_lst.sort()
        line_str = str(line_lst[0])
        for line_no in line_lst[1:]:
            line_str += ", {}".format(line_no)
        print("{:12s}:".format(word), line_str)


def get_words(file_obj):
    result_set = set()
    for line in file_obj:
        line = line.strip()
        word_lst = line.split()
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        for w in word_lst:
            if w:
                result_set.add(w)
    return result_set

def compare_files(file1, file2):
    f1_words, f2_words = get_words(file1), get_words(file2)
    # complete the rest
    # 1 define total_words variable that has as value the
    # length of f1_words is subset of f2_words
    total_words=len(f1_words.union(f2_words))
    print(total_words)
    # 2 define total_common variable that has as value the
    # length of f1_words is superset of f2_words
    total_common=len(f1_words.intersection(f2_words))
    print(total_common)
    # 3 print the values of total_words and total_common


def main():
    # test the index function
    print("Test of print_index:")
    file_obj1 = open("lab_gettys_burg.txt")
    print_index(file_obj1)
    file_obj1.close()
    print()

    # test the compare_files function
    print("Test of compare_files")
    f1 = open("lab_gettys_burg.txt")
    f2 = open("lab_declaration_of_Ind.txt")
    compare_files(f1, f2)
    f1.close()
    f2.close()
main()

