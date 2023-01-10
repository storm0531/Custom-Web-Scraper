import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup

# scrapping with beautiful soup
scrapping = True
page_url = input("What is the site url to scrap?place url...: ")

while scrapping:
    num_of_element = 0

    try:
        response = requests.get(page_url)
        page_text = response.text
        soup = BeautifulSoup(page_text, "html.parser")
    except MissingSchema:
        print("sorry but that is not in correct url format try again")
        continue

    tag_name = input("what is that element tag name(a p div li h1 h2 ...): ")

    # --------------------- find by selectors -----------------#
    id_to_find = input("what is element id (if none then pass): ")
    if id_to_find != "":
        id_to_find = "#" + id_to_find
    class_to_find = input("what is element class (if none then pass): ")
    if class_to_find != "":
        class_to_find = "." + class_to_find

    selected = soup.select(selector=f"{tag_name} {class_to_find} {id_to_find}")
    print(selected)

    extract_attribute = input("what attribute you want to extract from that element( href,title,class,id,text,... ): ")

    # -----------------------find by .find_all()-------------------------#
    # find_attr = input("place attribute that want to find element with from that page?(class,id,string):").lower()
    # by_attribute_values = input(
    #     "place that attribute value you want to find(if multiple values separate them by space): ")
    # extract_attribute = input("what attribute you want to extract from that element( href,title,class,id,text,... ): ")
    #
    # if find_attr == "class":
    #     selected = soup.find_all(name=tag_name, class_=by_attribute_values)
    # elif find_attr == "id":
    #     selected = soup.find_all(name=tag_name,id=by_attribute_values)
    # else:
    #     selected = soup.find_all(name=tag_name,string=by_attribute_values)

    for element in selected:
        num_of_element += 1
        extracted_part = element.get(extract_attribute)
        print(f"{num_of_element}:{extracted_part}")

    try_again_scrapping = input("are you want to do scrap this site again?(Y/N) or (end): ").upper()

    if try_again_scrapping == "N":
        page_url = input("What is the site url to scrap?place url...: ")
    elif try_again_scrapping == "END":
        scrapping = False
