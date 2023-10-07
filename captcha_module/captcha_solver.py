import os

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '2cdbd038b6bb82fb81ddbd87cd945d8c')

solver = TwoCaptcha(api_key)


def solve_captcha():
    print("################ STARTED SOLVING CAPTCHA ###################")
    try:
        result = solver.recaptcha(
            sitekey='6LfInyAbAAAAAF1xOpsR39DIvMT11L5Pig9aQgL_',
            url='https://vipdrive.net/auth/login')
    except Exception as e:
        print(e)
    else:
        return result['code']

