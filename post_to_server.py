import urllib
import urllib2

"""
based on the ptsv2.com site, get a particular url
and send to it a dict interpretation of a parsed dict.txt file
the file must contain the <key : val> format (w/o '<' and '>')
the dict is then POST'ed to the url
don't forget to get confirmation from destination server
"""


def main():
    # for user input: filepath = raw_input("Enter Filepath: ")
    file_path = "dict.txt"

    url = "http://ptsv2.com/t/blablabla/post"
    data = store_text_file_data(file_path)
    post_to_server(url, data)


def post_to_server(url, dict_data):
    encoded_data = urllib.urlencode(dict_data)
    print encoded_data
    req = urllib2.Request(url=url, data=encoded_data)
    fp = urllib2.urlopen(req)
    confirmation = fp.read()
    print confirmation


def store_text_file_data(text_file_path):
    ret = {}
    with open(text_file_path, "rb") as fp:
        for line in fp:
            (key, assign, val) = line.split()
            ret[key] = val
    fp.close()
    return ret


if __name__ == '__main__':
    main()
