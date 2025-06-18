from stats import get_num_words, get_num_char, get_char_list
import sys

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path) as f:
            file_contents = f.read()
            num_words = get_num_words(file_contents)
            num_char = get_num_char(file_contents)
            sorted_num_char = get_char_list(num_char)  

            print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n------------ Word Count ------------\nFound {num_words} total words\n------------ Character Count ------------")
            for dict in sorted_num_char:
                print(f"{dict['char']}: {dict['num']}")
            print("============ END ============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__=="__main__":
    main()
