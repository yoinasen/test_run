
def main():
    filepath = raw_input("Enter Filepath: ")
    print store_text_file_data(filepath)


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
