import requests
import json
import os

requests.packages.urllib3.disable_warnings()
SCKEY = os.environ.get('SCKEY')
TG_BOT_TOKEN = os.environ.get('TGBOT')
TG_USER_ID = os.environ.get('TGUSERID')


def checkin(email=os.environ.get('EMAIL'), password=os.environ.get('PASSWORD'),
            base_url=os.environ.get('BASE_URL'), ):
    email = email.split('@')
    email = email[0] + '%40' + email[1]
    session = requests.session()
    session.get(base_url, verify=False)
    login_url = base_url + '/auth/login'
    headers = {
                'authority': 'kp.m-team.cc',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://kp.m-team.cc',
                'referer': 'https://kp.m-team.cc/login.php',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
                        
    #post_data = 'email=' + email + '&passwd=' + password + '&code='
    #post_data = post_data.encode()
    data = {
                'username': email,
                'password': password
    }

    response = session.post(login_url, data, headers=headers, verify=False)
    response = json.loads(response.text)
    print(response)



result = checkin()

