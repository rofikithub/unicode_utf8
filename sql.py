import json

from ftfy import fix_encoding  # pip install ftfy

def json_file_print(url):
    with open(url, 'r') as f:
        data = json.load(f)

    for i in range(len(data)):
        # print(data[i]["id"]+"="+fix_encoding(data[i]["name"]))
        id     = data[i]["id"]
        name   = fix_encoding(data[i]["name"])
        text_1 = fix_encoding(data[i]["pi_bi_square"])
        text_2 = fix_encoding(data[i]["pi_bi_circle"])
        text_3 = fix_encoding(data[i]["pi_bi_triangle"])

        update_sql = "UPDATE `competency` SET `name`='"+str( name )+"',`pi_bi_square`='"+str( text_1 )+"',`pi_bi_circle`='"+str( text_2 )+"',`pi_bi_triangle`='"+str( text_3 )+"' WHERE `id`="+str( id )+""+";"

        print(update_sql)


def main():
    json_file_print("localhost.json")


if __name__ == "__main__":
    main()
