
def handle_file(file_path, date):
    cookies_hashmap = {}
    with open(file_path, "r") as f:
        # skip first line
        f.readline()
        for line in f.readlines():
            cookie, date_time = line.split(",")
            if date_time[:10] == date:
                cookies_hashmap[cookie] = cookies_hashmap.get(cookie, 0) + 1

        if len(cookies_hashmap) == 0:
            print(f"No cookie on '{date}'")
            return

        print_most_active_cookies(cookies_hashmap)


def print_most_active_cookies(cookies_hashmap):
    max_value = -1
    item_list = []
    for key, value in cookies_hashmap.items():
        if value > max_value:
            max_value = value
            item_list = [key]
        elif value == max_value:
            item_list.append(key)
    for item in item_list:
        print(item)
