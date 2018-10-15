# import urllib.request
from openload import OpenLoad
from time import sleep

# Define Functions

def find_id(string1):
    index = 0
    string2 = 'openload.co/f/'
    sl = 14  # sl = set lenght of distance from the openload.co/f/ string we have to obtain

    while sl < len(string1):
        if string1[index:sl] == string2:
            return sl  # Ricorda di implementarlo
        index = index + 1
        sl = sl + 1
    return -1


def cut_id(string1, sl):
    start_index = sl
    while sl < len(string1):
        if string1[sl] == '/':
            return string1[start_index:sl]
        sl = sl + 1
    return -1


def download(file_id):  # file_id = 'Id of the file will be downloaded'

    # Get a download ticket and captcha url.
    preparation_resp = ol.prepare_download(file_id)
    ticket = preparation_resp.get('ticket')

    # Sometimes no captcha is sent in openload.co API response.
    captcha_url = preparation_resp.get('captcha_url')

    if captcha_url:
        # Solve captcha.
        captcha_response = ''  # solve_captcha(captcha_url)
    else:
        captcha_response = ''

    download_resp = ol.get_download_link(file_id, ticket, captcha_response)
    direct_download_url = download_resp.get('url')

    # Process download url.
    print(direct_download_url)


# Data Part

ol = OpenLoad('bf97043b1e26e3aa', 'FTDZRy_v')

account_info = ol.account_info()
print(account_info)

# Instr. Set
i = 0
while i >= 0:
    try:
        sleep(360)
        download('9ZZOeA1yYzI')
        i = -1
    except Exception as e:
        i = i + 1
        print(e)
        print('Retry... #', i)

print('OK')
