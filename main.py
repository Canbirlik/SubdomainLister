import requests

target_input = input("Please, enter the main domain: ")

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "https://" + word + "." + target_input
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print(url + " is not available.")
        else:
            print(url + " " + str(response.status_code) + " => OK")

