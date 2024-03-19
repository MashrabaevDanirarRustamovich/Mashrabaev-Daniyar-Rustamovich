



class AuthPageWithCode(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://my.rt.ru/'
        super().__init__(web_driver, url)

    email = object(id='address')

    code0 = object(id='rt-code-0')
    code1 = object(id='rt-code-1')
    code2 = object(id='rt-code-2')
    code3 = object(id='rt-code-3')
    code4 = object(id='rt-code-4')
    code5 = object(id='rt-code-5')

    btn_code = object(id='otp_get_code')

    standard_auth_btn = object(id='standard_auth_btn')

    repeat_code = object(css_selector='button.code-input-container__resend')

    timeout_input_code = object(css_selector='span.code-input-container__timeout')

    reset_back = object(id='reset-back')
