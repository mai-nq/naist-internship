
import json
import re
import os
#read json file
def load_json(filename):
    data = []
    with open(filename) as json_file:
        json_data = json.load(json_file)
        for d in json_data:
            if d['post_body']:
                if "Message from TripAdvisor staff" not in d['post_body'][0]:
                    str = " ".join(d['post_body'])
                    data.append(str)
    return data
#end function

#remove redundancy: hyper link, not-english character, emoticon.
def remove_redundancy(posts):
    clean_posts = []
    #remove hyperlink
    for post in posts:
        p = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z-:!. \t])|(http\S+)", "", post)
        p = re.sub(' +',' ', p)
        clean_posts.append(p)
    return clean_posts

#write down in a new file
def save_file(posts, file_name):
    if __name__ == "__main__":
        f = open(file_name + '.txt', "a")
        for p in posts:
            f.write(p + "\n")

        f.close()

def main():
    src_input = '../crawler/tripadvisor_crawler/tripadvisor_crawler/data/'
    file_input = "osaka.json"
    file_name = os.path.splitext(os.path.basename(file_input))[0]
    src_output = '../data_cleaned/'

    posts = load_json(src_input + file_input)
    clean_posts = remove_redundancy(posts)
    for line in posts:
        print(line)
    save_file(clean_posts, src_output+file_name)

if __name__ == '__main__':
    main()


