import requests,json

cookies = {
    '__ac_nonce': '066e7972200199a5db35c',
    '__ac_signature': '_02B4Z6wo00f01KKv-YgAAIDBffQKxXFHfLCij.0AAE5R20',
    'tt_webid': '7415061383597311542',
    'gfkadpd': '24,6457',
    'ttcid': '295848c3db9e4e86ad17e2840e1edf6646',
    'x-web-secsdk-uid': '14fdc185-bd9d-4736-b3d7-e96afdb5b9a2',
    'local_city_cache': '%E4%B8%8A%E6%B5%B7',
    'csrftoken': '6566114275a3711f9e610cd06b2aa79c',
    's_v_web_id': 'verify_m14dv2iw_JoftyPzf_lfAq_4hog_8HSD_fhBDe23DgUee',
    '_ga': 'GA1.1.324523827.1726453542',
    'passport_csrf_token': 'aaac461451bcfaab8c27caa398d3b4de',
    'passport_csrf_token_default': 'aaac461451bcfaab8c27caa398d3b4de',
    'd_ticket': '9431814ea0770fefcec6e4978662510c862eb',
    'n_mh': 'tbzMH1aRHaYmU6IQWW11BODEOer0G1sx-y7BF80labY',
    'sso_auth_status': '3942eae7142d25333c9a7effe2ded3c3',
    'sso_auth_status_ss': '3942eae7142d25333c9a7effe2ded3c3',
    'sso_uid_tt': '4e869185a6a109e3af3f962d82808d7b',
    'sso_uid_tt_ss': '4e869185a6a109e3af3f962d82808d7b',
    'toutiao_sso_user': 'd38f0e8cb4c98158b048514a6fd14557',
    'toutiao_sso_user_ss': 'd38f0e8cb4c98158b048514a6fd14557',
    'sid_ucp_sso_v1': '1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw',
    'ssid_ucp_sso_v1': '1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw',
    'passport_auth_status': '137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8',
    'passport_auth_status_ss': '137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8',
    'sid_guard': '4f355d119a299ee03a0b508729723c0e%7C1726453597%7C5184001%7CFri%2C+15-Nov-2024+02%3A26%3A38+GMT',
    'uid_tt': 'a93381ffb927659ddd0e50fd904a9ab0',
    'uid_tt_ss': 'a93381ffb927659ddd0e50fd904a9ab0',
    'sid_tt': '4f355d119a299ee03a0b508729723c0e',
    'sessionid': '4f355d119a299ee03a0b508729723c0e',
    'sessionid_ss': '4f355d119a299ee03a0b508729723c0e',
    'is_staff_user': 'false',
    'sid_ucp_v1': '1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ',
    'ssid_ucp_v1': '1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ',
    'store-region': 'cn-sh',
    'store-region-src': 'uid',
    'odin_tt': '2cfe9998fcff7af65b451bf9b4683a67817dc319de034de1b920291615abf2cbc97eb32a868b09d188db7abd50161758',
    'tt_anti_token': 'd5R26iXoAB5WHMW-81044b1c0158e5d9c858805a64c3b4d61a1d2e11fea5d137c644e7d885d432b7',
    'tt_scid': '3gwlMxyjtz2Kmp3uQZKKbie23--342-KKPfQPwGGzjC0jcXlxfWTTfnxSt-3O4.z0d3d',
    'ttwid': '1%7C-Sq9SSKaskcsTBcdas8asekNOJfCnyNBk6ptMe5Nyy4%7C1726454216%7C5ba18eaf6206ec8c9913d16cf4b525781da0475f23a1e46ffb7d01a1706170b5',
    '_ga_QEHZPBE5HH': 'GS1.1.1726453541.1.1.1726454343.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': '__ac_nonce=066e7972200199a5db35c; __ac_signature=_02B4Z6wo00f01KKv-YgAAIDBffQKxXFHfLCij.0AAE5R20; tt_webid=7415061383597311542; gfkadpd=24,6457; ttcid=295848c3db9e4e86ad17e2840e1edf6646; x-web-secsdk-uid=14fdc185-bd9d-4736-b3d7-e96afdb5b9a2; local_city_cache=%E4%B8%8A%E6%B5%B7; csrftoken=6566114275a3711f9e610cd06b2aa79c; s_v_web_id=verify_m14dv2iw_JoftyPzf_lfAq_4hog_8HSD_fhBDe23DgUee; _ga=GA1.1.324523827.1726453542; passport_csrf_token=aaac461451bcfaab8c27caa398d3b4de; passport_csrf_token_default=aaac461451bcfaab8c27caa398d3b4de; d_ticket=9431814ea0770fefcec6e4978662510c862eb; n_mh=tbzMH1aRHaYmU6IQWW11BODEOer0G1sx-y7BF80labY; sso_auth_status=3942eae7142d25333c9a7effe2ded3c3; sso_auth_status_ss=3942eae7142d25333c9a7effe2ded3c3; sso_uid_tt=4e869185a6a109e3af3f962d82808d7b; sso_uid_tt_ss=4e869185a6a109e3af3f962d82808d7b; toutiao_sso_user=d38f0e8cb4c98158b048514a6fd14557; toutiao_sso_user_ss=d38f0e8cb4c98158b048514a6fd14557; sid_ucp_sso_v1=1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw; ssid_ucp_sso_v1=1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw; passport_auth_status=137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8; passport_auth_status_ss=137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8; sid_guard=4f355d119a299ee03a0b508729723c0e%7C1726453597%7C5184001%7CFri%2C+15-Nov-2024+02%3A26%3A38+GMT; uid_tt=a93381ffb927659ddd0e50fd904a9ab0; uid_tt_ss=a93381ffb927659ddd0e50fd904a9ab0; sid_tt=4f355d119a299ee03a0b508729723c0e; sessionid=4f355d119a299ee03a0b508729723c0e; sessionid_ss=4f355d119a299ee03a0b508729723c0e; is_staff_user=false; sid_ucp_v1=1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ; ssid_ucp_v1=1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ; store-region=cn-sh; store-region-src=uid; odin_tt=2cfe9998fcff7af65b451bf9b4683a67817dc319de034de1b920291615abf2cbc97eb32a868b09d188db7abd50161758; tt_anti_token=d5R26iXoAB5WHMW-81044b1c0158e5d9c858805a64c3b4d61a1d2e11fea5d137c644e7d885d432b7; tt_scid=3gwlMxyjtz2Kmp3uQZKKbie23--342-KKPfQPwGGzjC0jcXlxfWTTfnxSt-3O4.z0d3d; ttwid=1%7C-Sq9SSKaskcsTBcdas8asekNOJfCnyNBk6ptMe5Nyy4%7C1726454216%7C5ba18eaf6206ec8c9913d16cf4b525781da0475f23a1e46ffb7d01a1706170b5; _ga_QEHZPBE5HH=GS1.1.1726453541.1.1.1726454343.0.0.0',
    'priority': 'u=1, i',
    'referer': 'https://www.toutiao.com/article/7415046224102867482/?log_from=f2ae21a4ccb3b_1726454216133',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
}

digg_cookies = {
    '__ac_signature': '_02B4Z6wo00f01KKv-YgAAIDBffQKxXFHfLCij.0AAE5R20',
    'tt_webid': '7415061383597311542',
    'gfkadpd': '24,6457',
    'ttcid': '295848c3db9e4e86ad17e2840e1edf6646',
    'x-web-secsdk-uid': '14fdc185-bd9d-4736-b3d7-e96afdb5b9a2',
    'local_city_cache': '%E4%B8%8A%E6%B5%B7',
    'csrftoken': '6566114275a3711f9e610cd06b2aa79c',
    's_v_web_id': 'verify_m14dv2iw_JoftyPzf_lfAq_4hog_8HSD_fhBDe23DgUee',
    '_ga': 'GA1.1.324523827.1726453542',
    'passport_csrf_token': 'aaac461451bcfaab8c27caa398d3b4de',
    'passport_csrf_token_default': 'aaac461451bcfaab8c27caa398d3b4de',
    'd_ticket': '9431814ea0770fefcec6e4978662510c862eb',
    'n_mh': 'tbzMH1aRHaYmU6IQWW11BODEOer0G1sx-y7BF80labY',
    'sso_auth_status': '3942eae7142d25333c9a7effe2ded3c3',
    'sso_auth_status_ss': '3942eae7142d25333c9a7effe2ded3c3',
    'sso_uid_tt': '4e869185a6a109e3af3f962d82808d7b',
    'sso_uid_tt_ss': '4e869185a6a109e3af3f962d82808d7b',
    'toutiao_sso_user': 'd38f0e8cb4c98158b048514a6fd14557',
    'toutiao_sso_user_ss': 'd38f0e8cb4c98158b048514a6fd14557',
    'sid_ucp_sso_v1': '1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw',
    'ssid_ucp_sso_v1': '1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw',
    'passport_auth_status': '137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8',
    'passport_auth_status_ss': '137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8',
    'sid_guard': '4f355d119a299ee03a0b508729723c0e%7C1726453597%7C5184001%7CFri%2C+15-Nov-2024+02%3A26%3A38+GMT',
    'uid_tt': 'a93381ffb927659ddd0e50fd904a9ab0',
    'uid_tt_ss': 'a93381ffb927659ddd0e50fd904a9ab0',
    'sid_tt': '4f355d119a299ee03a0b508729723c0e',
    'sessionid': '4f355d119a299ee03a0b508729723c0e',
    'sessionid_ss': '4f355d119a299ee03a0b508729723c0e',
    'is_staff_user': 'false',
    'sid_ucp_v1': '1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ',
    'ssid_ucp_v1': '1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ',
    'store-region': 'cn-sh',
    'store-region-src': 'uid',
    'odin_tt': '2cfe9998fcff7af65b451bf9b4683a67817dc319de034de1b920291615abf2cbc97eb32a868b09d188db7abd50161758',
    '_ga_QEHZPBE5HH': 'GS1.1.1726458771.2.0.1726458771.0.0.0',
    'tt_anti_token': 'BD7Azw89lSbW2CE-eb724a86b9cb921af60271d5afaad4cae51da49bde6854ce20f13eb4fbb8f5d9',
    'ttwid': '1%7C-Sq9SSKaskcsTBcdas8asekNOJfCnyNBk6ptMe5Nyy4%7C1726458771%7C666668e5bb2ac6cfb12a089077762c69bba5e6a53d9e964d01109893a393d4ef',
    'tt_scid': 'bfbH6VHhXiLX.iOSIrvciZ4Re2mMm4liR9kGSYllrmkYBG-Ir7qSjw8Uy7fc9Ung502b',
}

digg_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__ac_signature=_02B4Z6wo00f01KKv-YgAAIDBffQKxXFHfLCij.0AAE5R20; tt_webid=7415061383597311542; gfkadpd=24,6457; ttcid=295848c3db9e4e86ad17e2840e1edf6646; x-web-secsdk-uid=14fdc185-bd9d-4736-b3d7-e96afdb5b9a2; local_city_cache=%E4%B8%8A%E6%B5%B7; csrftoken=6566114275a3711f9e610cd06b2aa79c; s_v_web_id=verify_m14dv2iw_JoftyPzf_lfAq_4hog_8HSD_fhBDe23DgUee; _ga=GA1.1.324523827.1726453542; passport_csrf_token=aaac461451bcfaab8c27caa398d3b4de; passport_csrf_token_default=aaac461451bcfaab8c27caa398d3b4de; d_ticket=9431814ea0770fefcec6e4978662510c862eb; n_mh=tbzMH1aRHaYmU6IQWW11BODEOer0G1sx-y7BF80labY; sso_auth_status=3942eae7142d25333c9a7effe2ded3c3; sso_auth_status_ss=3942eae7142d25333c9a7effe2ded3c3; sso_uid_tt=4e869185a6a109e3af3f962d82808d7b; sso_uid_tt_ss=4e869185a6a109e3af3f962d82808d7b; toutiao_sso_user=d38f0e8cb4c98158b048514a6fd14557; toutiao_sso_user_ss=d38f0e8cb4c98158b048514a6fd14557; sid_ucp_sso_v1=1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw; ssid_ucp_sso_v1=1.0.0-KGU1N2M0NGNiNTVhNzQ5ZDJhMjdmNjg2MjYxYjMyYWNjY2U0YzNlN2EKHAiNtejbyAIQ3a6etwYYGCAMMNvo1YIGOAJA8QcaAmhsIiBkMzhmMGU4Y2I0Yzk4MTU4YjA0ODUxNGE2ZmQxNDU1Nw; passport_auth_status=137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8; passport_auth_status_ss=137418c2d55643c1111cf505ef8859ee%2C5479477d86d7c1ab80bf2e468d2602f8; sid_guard=4f355d119a299ee03a0b508729723c0e%7C1726453597%7C5184001%7CFri%2C+15-Nov-2024+02%3A26%3A38+GMT; uid_tt=a93381ffb927659ddd0e50fd904a9ab0; uid_tt_ss=a93381ffb927659ddd0e50fd904a9ab0; sid_tt=4f355d119a299ee03a0b508729723c0e; sessionid=4f355d119a299ee03a0b508729723c0e; sessionid_ss=4f355d119a299ee03a0b508729723c0e; is_staff_user=false; sid_ucp_v1=1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ; ssid_ucp_v1=1.0.0-KDFkY2U5NTM3YWNlNWVlNjk1NmRjNzg2MzU2OGYzNjlhMzI0ZjJkYjcKFgiNtejbyAIQ3a6etwYYGCAMOAJA8QcaAmxxIiA0ZjM1NWQxMTlhMjk5ZWUwM2EwYjUwODcyOTcyM2MwZQ; store-region=cn-sh; store-region-src=uid; odin_tt=2cfe9998fcff7af65b451bf9b4683a67817dc319de034de1b920291615abf2cbc97eb32a868b09d188db7abd50161758; _ga_QEHZPBE5HH=GS1.1.1726458771.2.0.1726458771.0.0.0; tt_anti_token=BD7Azw89lSbW2CE-eb724a86b9cb921af60271d5afaad4cae51da49bde6854ce20f13eb4fbb8f5d9; ttwid=1%7C-Sq9SSKaskcsTBcdas8asekNOJfCnyNBk6ptMe5Nyy4%7C1726458771%7C666668e5bb2ac6cfb12a089077762c69bba5e6a53d9e964d01109893a393d4ef; tt_scid=bfbH6VHhXiLX.iOSIrvciZ4Re2mMm4liR9kGSYllrmkYBG-Ir7qSjw8Uy7fc9Ung502b',
    'origin': 'https://www.toutiao.com',
    'priority': 'u=1, i',
    'referer': 'https://www.toutiao.com/article/7415022103491002880',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tt-anti-token': 'BD7Azw89lSbW2CE-eb724a86b9cb921af60271d5afaad4cae51da49bde6854ce20f13eb4fbb8f5d9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'x-csrftoken': '6566114275a3711f9e610cd06b2aa79c',
}


try:  
    article_id = input("请输入文章ID: ") 
    print("获取文章ID评论:", article_id)  
except ValueError:  
    print("错误：请输入一个有效的整数。")

params = {
    'aid': '24',
    'app_name': 'toutiao_web',
    'offset': '0',#第一页0 第二页20
    'count': '20',
    'group_id': article_id,
    'item_id': article_id,
    '_signature': '_02B4Z6wo00d0175drrgAAIDCYQZd9NF7oW--eaoAAIl5UrSxblrYuvzG-RcH2XIuUbhb7.IpnT7ZKV.eskMfG5ziBbAkCy.-Dx-EVaX8nLNfYvMdwqr7Bb-bR7gTq8noTD577LeeJoHOlXVu1f',
}

comments = requests.get('https://www.toutiao.com/article/v4/tab_comments/', params=params, cookies=cookies, headers=headers).json()

for item in comments["data"]:  
    # 从每个项目中获取"comment"字典  
    comment = item["comment"]  
    # 打印id和text  
    print(f"ID: {comment['id']}, Text: {comment['text']}") 


try:  
    comment_id = input("请输入评论ID: ")
    print("点赞中:", comment_id)  
except ValueError:  
    print("错误：请输入一个有效的整数。")

digg_params = {
    'aid': '24',
    'app_name': 'toutiao_web',
    '_signature': '_02B4Z6wo00901onndRQAAIDDVryGWQP2NvaJw3GAAMSqTXU6APYq-FEz8o8JlnnKB-nkJtT8vJJQawLqYqUbHUJzLbdDWejWfuNjl30q1UyrN-X-90.9NXxeCwOIa6.noRn01XNVEe3M4uvN81',
}

digg_data = {
    'comment_id': comment_id ,
    'group_id': article_id,
    'item_id': article_id,
    'action': 'digg',
}

digg_response = requests.post(
    'https://www.toutiao.com/browser/2/data/v1/comment_action/',
    params=digg_params,
    cookies=digg_cookies,
    headers=digg_headers,
    data=digg_data,
).json()

message = digg_response["message"]  
  
# 打印结果  
print(f"响应: {message}")  