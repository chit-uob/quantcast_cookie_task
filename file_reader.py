
def handle_file(file_path, date):
    cookies_hashmap = {}
    with open(file_path, "r") as f:
        # skip first line
        f.readline()

        # to store whether we have found a matching date yet
        match_flag = False

        try:
            for line in f.readlines():
                cookie, date_time = line.split(",")
                if date_time[:10] == date:
                    match_flag = True
                    cookies_hashmap[cookie] = cookies_hashmap.get(cookie, 0) + 1
                else:
                    if match_flag:
                        # At this point, there were already some matching cookies, so that if this cookies does not
                        # match, it means the following cookies will not match as well, so we break
                        break
        except:
            print("cookies file is incorrectly formatted")
            return

        if len(cookies_hashmap) == 0:
            print(f"No cookie on '{date}'")
            return

        return find_most_active_cookies(cookies_hashmap)


def find_most_active_cookies(cookies_hashmap):
    max_value = -1
    item_list = []
    for key, value in cookies_hashmap.items():
        if value > max_value:
            max_value = value
            item_list = [key]
        elif value == max_value:
            item_list.append(key)
    return item_list
