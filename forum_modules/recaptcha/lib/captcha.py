# -*- coding: utf-8 -*-

import urllib2, urllib

API_SSL_SERVER="https://www.google.com/recaptcha/api"
API_SERVER="http://www.google.com/recaptcha/api"
VERIFY_SERVER="www.google.com"

class RecaptchaResponse(object):
    def __init__(self, is_valid, error_code=None):
        self.is_valid = is_valid
        self.error_code = error_code

def displayhtml (public_key):

    return """
    <div class="g-recaptcha" data-sitekey="6LduhFAUAAAAALSAedOBurjIsSjdM7SVAVJwVcsX"></div>

""" % {
        'PublicKey' : public_key,
        }


def submit (recaptcha_response_field,
            private_key,
            remoteip):

    if not (recaptcha_response_field and len (recaptcha_response_field)):
        return RecaptchaResponse (is_valid = False, error_code = 'incorrect-captcha-sol')


    def encode_if_necessary(s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s

    params = urllib.urlencode ({
        'secret': encode_if_necessary(private_key),
        'remoteip' :  encode_if_necessary(remoteip),
        'response' :  encode_if_necessary(recaptcha_response_field),
        })

    request = urllib2.Request (
        url = "http://%s/recaptcha/api/verify" % VERIFY_SERVER,
        data = params,
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "reCAPTCHA Python"
        }
    )

    httpresp = urllib2.urlopen(request)

    return_values = httpresp.read().splitlines()
    httpresp.close()

    return_code = return_values[0]

    if return_code == "true":
        return RecaptchaResponse(is_valid = True)
    else:
        return RecaptchaResponse(is_valid = False, error_code = return_values[1])
