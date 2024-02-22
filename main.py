import json

from ftfy import fix_encoding     # pip install ftfy

def json_file_print(url):
    with open(url, 'r') as f:
        data = json.load(f)

    for i in range(len(data)):
        print(data[i]["id"]+"="+fix_encoding(data[i]["name"]))


def main():
    json_file_print("localhost.json")


if __name__ == "__main__":
    main()
