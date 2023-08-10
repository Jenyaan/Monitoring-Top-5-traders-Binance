import requests


def rank_profile():
    cookies = {
        'bnc-uuid': 'f6416fe5-2712-4aa7-b9b4-baccb9424704',
        'BNC_FV_KEY': '33d2c5d8c87ba192a490c02060916a368304bf92',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'se_sd': '1EbVRAx0JHMBBQRwFWxQgZZBhDhYAEWW1YMZdUUR1FRVQDFNXW0c1',
        'se_gd': 'gsBCBBlwLFEEh0N4RGhggZZAgFARVBWW1UPZdUUR1FRVQDVNXWYd1',
        'se_gsd': 'BjAkBUJ5IickDRUvISYhBRAnBlYbAQcHUllGVVVXWlFXDVNS1',
        'd1og': 'web.248634473.2E0D58AF82EEDF657E2BB6564F1ACF00',
        'r2o1': 'web.248634473.0FE5A512E1B09D5AA1846FED66D60E07',
        'f30l': 'web.248634473.8780CA333F786B53EC3C7ECDDD0DB2E7',
        'BNC-Location': 'BINANCE',
        '__BNC_USER_DEVICE_ID__': '{"b5193ee9ff62c0a7b0d38ff798e20c12":{"date":1690561607907,"value":"16905616081360MovjpyGUx2IInvNDBN"}}',
        'p20t': 'web.248634473.E45297735DA3F4E0F394C01DB8E6F18D',
        'userPreferredCurrency': 'USD_USD',
        'fiat-prefer-currency': 'EUR',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22248634473%22%2C%22first_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5OWQ1MWM5MjRhYzgtMGMyMWI2NDE1MTFlOGQtMjYwMzFjNTEtMjA3MzYwMC0xODk5ZDUxYzkyNWU3MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0ODYzNDQ3MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22248634473%22%7D%2C%22%24device_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%7D',
        '_ga': 'GA1.1.1230781862.1691148931',
        'BNC_FV_KEY_T': '101-jd7ymCypgp6qADxrYKWN7Dr3ryKvtVSgsvPuyOKQyfFnCXMdXNGH0MoaVQxLsgyQEx%2FfkiHG2z6FgAMHNr1O4Q%3D%3D-iZh3ud%2FU5X8T03khCLMHxg%3D%3D-59',
        'BNC_FV_KEY_EXPIRE': '1691631307042',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Aug+09+2023+22%3A35%3A07+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=a1f94e0f-db34-4682-a0f9-f4d2a6703350&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A0%2CC0002%3A1&AwaitingReconsent=false',
        '_ga_3WP50LGEEC': 'GS1.1.1691609706.3.1.1691609729.37.0.0',
        'lang': 'en',
        'theme': 'dark',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,uk;q=0.7',
        'bnc-uuid': 'f6416fe5-2712-4aa7-b9b4-baccb9424704',
        'clienttype': 'web',
        'content-type': 'application/json',
        # 'cookie': 'bnc-uuid=f6416fe5-2712-4aa7-b9b4-baccb9424704; BNC_FV_KEY=33d2c5d8c87ba192a490c02060916a368304bf92; source=referral; campaign=www.binance.com; se_sd=1EbVRAx0JHMBBQRwFWxQgZZBhDhYAEWW1YMZdUUR1FRVQDFNXW0c1; se_gd=gsBCBBlwLFEEh0N4RGhggZZAgFARVBWW1UPZdUUR1FRVQDVNXWYd1; se_gsd=BjAkBUJ5IickDRUvISYhBRAnBlYbAQcHUllGVVVXWlFXDVNS1; d1og=web.248634473.2E0D58AF82EEDF657E2BB6564F1ACF00; r2o1=web.248634473.0FE5A512E1B09D5AA1846FED66D60E07; f30l=web.248634473.8780CA333F786B53EC3C7ECDDD0DB2E7; BNC-Location=BINANCE; __BNC_USER_DEVICE_ID__={"b5193ee9ff62c0a7b0d38ff798e20c12":{"date":1690561607907,"value":"16905616081360MovjpyGUx2IInvNDBN"}}; p20t=web.248634473.E45297735DA3F4E0F394C01DB8E6F18D; userPreferredCurrency=USD_USD; fiat-prefer-currency=EUR; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22248634473%22%2C%22first_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5OWQ1MWM5MjRhYzgtMGMyMWI2NDE1MTFlOGQtMjYwMzFjNTEtMjA3MzYwMC0xODk5ZDUxYzkyNWU3MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0ODYzNDQ3MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22248634473%22%7D%2C%22%24device_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%7D; _ga=GA1.1.1230781862.1691148931; BNC_FV_KEY_T=101-jd7ymCypgp6qADxrYKWN7Dr3ryKvtVSgsvPuyOKQyfFnCXMdXNGH0MoaVQxLsgyQEx%2FfkiHG2z6FgAMHNr1O4Q%3D%3D-iZh3ud%2FU5X8T03khCLMHxg%3D%3D-59; BNC_FV_KEY_EXPIRE=1691631307042; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Aug+09+2023+22%3A35%3A07+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=a1f94e0f-db34-4682-a0f9-f4d2a6703350&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A0%2CC0002%3A1&AwaitingReconsent=false; _ga_3WP50LGEEC=GS1.1.1691609706.3.1.1691609729.37.0.0; lang=en; theme=dark',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA0MCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUiLCJ0aW1lem9uZSI6IkdNVCszIiwidGltZXpvbmVPZmZzZXQiOi0xODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTE1LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImY4NjkwMGFjIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEFNRCkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBTUQsIFJhZGVvbiBSWCA1ODAgU2VyaWVzIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL0tpZXYiLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTE1LjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiZDMwYjI0ZmZmNjYyZTU4NTRhMDUxMjU1NjAyOTE2M2IiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIxNjkwNTYxNjA4MTM2ME1vdmpweUdVeDJJSW52TkRCTiJ9',
        'dnt': '1',
        'fvideo-id': '33d2c5d8c87ba192a490c02060916a368304bf92',
        'lang': 'en',
        'origin': 'https://www.binance.com',
        'referer': 'https://www.binance.com/en/futures-activity/leaderboard/futures',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-passthrough-token': '',
        'x-trace-id': '2f02410a-fd99-4080-b935-0b05875f49da',
        'x-ui-request-trace': '2f02410a-fd99-4080-b935-0b05875f49da',
    }

    json_data = {
        'tradeType': 'PERPETUAL',
        'statisticsType': 'ROI',
        'periodType': 'WEEKLY',
        'isShared': True,
        'isTrader': False,
    }

    response = requests.post(
        'https://www.binance.com/bapi/futures/v3/public/future/leaderboard/getLeaderboardRank',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    list_r = response.get('data')

    # Finding the nickname and ID of the top 5 traders
    for i in range(5):
        profile_info(list_r[i]["encryptedUid"], list_r[i]["nickName"])

def profile_info(id_user,name_user):
    cookies = {
        'bnc-uuid': 'f6416fe5-2712-4aa7-b9b4-baccb9424704',
        'BNC_FV_KEY': '33d2c5d8c87ba192a490c02060916a368304bf92',
        'source': 'referral',
        'campaign': 'www.binance.com',
        'se_sd': '1EbVRAx0JHMBBQRwFWxQgZZBhDhYAEWW1YMZdUUR1FRVQDFNXW0c1',
        'se_gd': 'gsBCBBlwLFEEh0N4RGhggZZAgFARVBWW1UPZdUUR1FRVQDVNXWYd1',
        'se_gsd': 'BjAkBUJ5IickDRUvISYhBRAnBlYbAQcHUllGVVVXWlFXDVNS1',
        'd1og': 'web.248634473.2E0D58AF82EEDF657E2BB6564F1ACF00',
        'r2o1': 'web.248634473.0FE5A512E1B09D5AA1846FED66D60E07',
        'f30l': 'web.248634473.8780CA333F786B53EC3C7ECDDD0DB2E7',
        'BNC-Location': 'BINANCE',
        '__BNC_USER_DEVICE_ID__': '{"b5193ee9ff62c0a7b0d38ff798e20c12":{"date":1690561607907,"value":"16905616081360MovjpyGUx2IInvNDBN"}}',
        'p20t': 'web.248634473.E45297735DA3F4E0F394C01DB8E6F18D',
        'userPreferredCurrency': 'USD_USD',
        'fiat-prefer-currency': 'EUR',
        '_ga': 'GA1.1.1230781862.1691148931',
        'BNC_FV_KEY_T': '101-jd7ymCypgp6qADxrYKWN7Dr3ryKvtVSgsvPuyOKQyfFnCXMdXNGH0MoaVQxLsgyQEx%2FfkiHG2z6FgAMHNr1O4Q%3D%3D-iZh3ud%2FU5X8T03khCLMHxg%3D%3D-59',
        'BNC_FV_KEY_EXPIRE': '1691631307042',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22248634473%22%2C%22first_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5OWQ1MWM5MjRhYzgtMGMyMWI2NDE1MTFlOGQtMjYwMzFjNTEtMjA3MzYwMC0xODk5ZDUxYzkyNWU3MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0ODYzNDQ3MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22248634473%22%7D%2C%22%24device_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%7D',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+10+2023+01%3A10%3A14+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=a1f94e0f-db34-4682-a0f9-f4d2a6703350&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A0%2CC0002%3A1&AwaitingReconsent=false',
        'lang': 'en',
        'theme': 'dark',
        '_ga_3WP50LGEEC': 'GS1.1.1691619011.5.1.1691619365.58.0.0',
    }

    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8,uk;q=0.7',
        'bnc-uuid': 'f6416fe5-2712-4aa7-b9b4-baccb9424704',
        'clienttype': 'web',
        'content-type': 'application/json',
        # 'cookie': 'bnc-uuid=f6416fe5-2712-4aa7-b9b4-baccb9424704; BNC_FV_KEY=33d2c5d8c87ba192a490c02060916a368304bf92; source=referral; campaign=www.binance.com; se_sd=1EbVRAx0JHMBBQRwFWxQgZZBhDhYAEWW1YMZdUUR1FRVQDFNXW0c1; se_gd=gsBCBBlwLFEEh0N4RGhggZZAgFARVBWW1UPZdUUR1FRVQDVNXWYd1; se_gsd=BjAkBUJ5IickDRUvISYhBRAnBlYbAQcHUllGVVVXWlFXDVNS1; d1og=web.248634473.2E0D58AF82EEDF657E2BB6564F1ACF00; r2o1=web.248634473.0FE5A512E1B09D5AA1846FED66D60E07; f30l=web.248634473.8780CA333F786B53EC3C7ECDDD0DB2E7; BNC-Location=BINANCE; __BNC_USER_DEVICE_ID__={"b5193ee9ff62c0a7b0d38ff798e20c12":{"date":1690561607907,"value":"16905616081360MovjpyGUx2IInvNDBN"}}; p20t=web.248634473.E45297735DA3F4E0F394C01DB8E6F18D; userPreferredCurrency=USD_USD; fiat-prefer-currency=EUR; _ga=GA1.1.1230781862.1691148931; BNC_FV_KEY_T=101-jd7ymCypgp6qADxrYKWN7Dr3ryKvtVSgsvPuyOKQyfFnCXMdXNGH0MoaVQxLsgyQEx%2FfkiHG2z6FgAMHNr1O4Q%3D%3D-iZh3ud%2FU5X8T03khCLMHxg%3D%3D-59; BNC_FV_KEY_EXPIRE=1691631307042; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22248634473%22%2C%22first_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5OWQ1MWM5MjRhYzgtMGMyMWI2NDE1MTFlOGQtMjYwMzFjNTEtMjA3MzYwMC0xODk5ZDUxYzkyNWU3MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjI0ODYzNDQ3MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22248634473%22%7D%2C%22%24device_id%22%3A%221899d51c924ac8-0c21b641511e8d-26031c51-2073600-1899d51c925e73%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+10+2023+01%3A10%3A14+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=a1f94e0f-db34-4682-a0f9-f4d2a6703350&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A0%2CC0002%3A1&AwaitingReconsent=false; lang=en; theme=dark; _ga_3WP50LGEEC=GS1.1.1691619011.5.1.1691619365.58.0.0',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA0MCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUiLCJ0aW1lem9uZSI6IkdNVCszIiwidGltZXpvbmVPZmZzZXQiOi0xODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTE1LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImY4NjkwMGFjIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEFNRCkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBTUQsIFJhZGVvbiBSWCA1ODAgU2VyaWVzIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL0tpZXYiLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTE1LjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiZDMwYjI0ZmZmNjYyZTU4NTRhMDUxMjU1NjAyOTE2M2IiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIxNjkwNTYxNjA4MTM2ME1vdmpweUdVeDJJSW52TkRCTiJ9',
        'dnt': '1',
        'fvideo-id': '33d2c5d8c87ba192a490c02060916a368304bf92',
        'lang': 'en',
        'origin': 'https://www.binance.com',
        'referer': f'https://www.binance.com/en/futures-activity/leaderboard/user/um?encryptedUid={id_user}',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-passthrough-token': '',
        'x-trace-id': '2490df43-b5c7-4682-a2ba-3139a3ac016c',
        'x-ui-request-trace': '2490df43-b5c7-4682-a2ba-3139a3ac016c',
    }

    json_data = {
        'encryptedUid': f'{id_user}',
        'tradeType': 'PERPETUAL',
    }

    response = requests.post(
        'https://www.binance.com/bapi/futures/v2/public/future/leaderboard/getOtherPerformance',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()

    listd = response.get('data').get('performanceRetList')

    # find Weekly ROI
    for i in listd:
        if i["periodType"] == "WEEKLY" and i["statisticsType"] == "ROI":
            print(f"{name_user} : {i['value']}")