from houses import houses

def master_list():
    house_urls_and_names = {}
    for item in houses:
        house_url = item["url"]
        house_name = item["name"]
        house_urls_and_names[house_url] = house_name
    return house_urls_and_names

print(master_list())