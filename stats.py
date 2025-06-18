def get_num_words(file_contents):
        content_list = file_contents.split()
        return(len(content_list))

def get_num_char(file_contents):
        char_count = {}
        for char in file_contents:
                char = char.lower()
                if char in char_count:
                        char_count[char] += 1
                else:
                        char_count[char] = 1
        return char_count

def get_char_list(char_dict):
        char_list = []
        for char in char_dict:
                if char.isalpha():
                        new_dict = {}
                        new_dict['char'] = char
                        new_dict['num'] = char_dict[char]
                        char_list.append(new_dict)
        return sorted(char_list, key=lambda d: d['num'], reverse=True)

