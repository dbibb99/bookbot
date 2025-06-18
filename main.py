from stats import get_num_words

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_num_words(file_contents))     

if __name__=="__main__":
    main()
