from samesite_compat_check import should_send_same_site_none


'''
User-Agent strings below are sampled from https://developers.whatismybrowser.com/useragents/

Let's reiterate -- the following browsers should not receive a `SameSite=None`
cookie:
* Chrome 51 to Chrome 66 -- inclusive on both ends
  (Doesn't apply on iOS, since Chrome on iOS is actually Webkit/Safari)
* UC Browser on Android prior to version 12.13.2
* Safari and embedded browsers on MacOS 10.14
* All browsers on iOS 12 (this includes Chrome!)
'''


def test_unknown():
    '''An unknown User-Agent string is allowed to receive the `SameSite=None`
    cookie'''
    assert should_send_same_site_none('abcdefghijklmn') is True


WINDOWS_CHROME_60 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
MACOSX_10_12_6_CHROME_80 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

IPHONE_6 = 'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3'


def test_macosx_10_12_6_chrome_80():
    assert should_send_same_site_none(MACOSX_10_12_6_CHROME_80) is True


def test_windows_chrome_60():
    assert should_send_same_site_none(WINDOWS_CHROME_60) is False


def test_iphone_6():
    assert should_send_same_site_none(IPHONE_6) is True


###########
# Android #
###########


####################
# macOS / Mac OS X #
####################
# fmt: off

# Embedded browsers
MACOSX_10_12_6_WEKBIT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko)'
MACOSX_10_13_6_WEKBIT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)'
MACOSX_10_14_4_WEKBIT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko)'
MACOSX_10_14_5_WEKBIT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)'
MACOSX_10_15_WEKBIT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko)'

# Safari
MACOSX_10_12_6_SAFARI_10_1_2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
MACOSX_10_13_6_SAFARI_12_0_1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15'
MACOSX_10_14_4_SAFARI_12_0 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
MACOSX_10_14_5_SAFARI_12_1_1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
MACOSX_10_14_6_SAFARI_12_1_2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'
MACOSX_10_14_6_SAFARI_13_0_4 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'
MACOSX_10_15_2_SAFARI_13_0_4 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'

# Chrome
MACOSX_10_12_3_CHROME_56 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
MACOSX_10_12_4_CHROME_57 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
MACOSX_10_12_6_CHROME_61 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
MACOSX_10_13_3_CHROME_65 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
MACOSX_10_12_6_CHROME_67 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
MACOSX_10_14_1_CHROME_70 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
MACOSX_10_14_5_CHROME_74 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'


# Firefox
MACOSX_10_12_FIREFOX_57 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0'
MACOSX_10_13_FIREFOX_60 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
MACOSX_10_13_FIREFOX_62 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'
MACOSX_10_14_FIREFOX_67 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0'
# fmt: on


def test_macosx():
    '''Test that Safari and embedded browsers on macOS 10.14 shouldn't get the
    `SameSite=None`-cookie'''

    # Embedded browsers
    assert should_send_same_site_none(MACOSX_10_12_6_WEKBIT) is True
    assert should_send_same_site_none(MACOSX_10_13_6_WEKBIT) is True
    assert should_send_same_site_none(MACOSX_10_14_4_WEKBIT) is False
    assert should_send_same_site_none(MACOSX_10_14_5_WEKBIT) is False
    assert should_send_same_site_none(MACOSX_10_15_WEKBIT) is True

    # Safari
    assert should_send_same_site_none(MACOSX_10_12_6_SAFARI_10_1_2) is True
    assert should_send_same_site_none(MACOSX_10_13_6_SAFARI_12_0_1) is True
    assert should_send_same_site_none(MACOSX_10_14_4_SAFARI_12_0) is False
    assert should_send_same_site_none(MACOSX_10_14_5_SAFARI_12_1_1) is False
    assert should_send_same_site_none(MACOSX_10_14_6_SAFARI_12_1_2) is False
    assert should_send_same_site_none(MACOSX_10_14_6_SAFARI_13_0_4) is False
    assert should_send_same_site_none(MACOSX_10_15_2_SAFARI_13_0_4) is True

    # Chrome
    assert should_send_same_site_none(MACOSX_10_12_3_CHROME_56) is False
    assert should_send_same_site_none(MACOSX_10_12_4_CHROME_57) is False
    assert should_send_same_site_none(MACOSX_10_12_6_CHROME_61) is False
    assert should_send_same_site_none(MACOSX_10_13_3_CHROME_65) is False
    assert should_send_same_site_none(MACOSX_10_12_6_CHROME_67) is True
    assert should_send_same_site_none(MACOSX_10_14_1_CHROME_70) is True
    assert should_send_same_site_none(MACOSX_10_14_5_CHROME_74) is True

    # Firefox
    assert should_send_same_site_none(MACOSX_10_12_FIREFOX_57) is True
    assert should_send_same_site_none(MACOSX_10_13_FIREFOX_60) is True
    assert should_send_same_site_none(MACOSX_10_13_FIREFOX_62) is True
    assert should_send_same_site_none(MACOSX_10_14_FIREFOX_67) is True


#######
# iOS #
#######


IOS_10_3_3_WEBKIT = 'Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60'
IOS_11_4_WEBKIT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79'
IOS_12_0_1_WEBKIT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A404'
IOS_12_0_1_WEBKIT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366'
IOS_12_1_WEBKIT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92'
IOS_12_1_4_WEBKIT = 'Mozilla/5.0 (iPad; CPU OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57'
IOS_12_3_WEBKIT = 'Mozilla/5.0 (iPad; CPU OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
IOS_13_3_WEBKIT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

IOS_6_0_SAFARI_6 = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'
IOS_9_3_5_SAFARI_9 = 'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1'
IOS_10_3_3_SAFARI_10 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1'
IOS_11_4_1_SAFARI_11 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'
IOS_12_4_1_SAFARI_12_1 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'
IOS_13_1_3_SAFARI_13 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1'

IOS_9_3_5_CHROME_63 = 'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/63.0.3239.73 Mobile/13G36 Safari/601.1.46'
IOS_11_2_6_CHROME_65 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) CriOS/65.0.3325.152 Mobile/15D100 Safari/604.1'
IOS_11_4_1_CHROME_68 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) CriOS/68.0.3440.83 Mobile/15G77 Safari/604.1'
IOS_12_0_CHROME_69 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1'
IOS_12_0_CHROME_70 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/70.0.3538.75 Mobile/15E148 Safari/605.1'
IOS_12_1_CHROME_70 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/70.0.3538.75 Mobile/15E148 Safari/605.1'
IOS_12_3_CHROME_75 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/75.0.3770.103 Mobile/15E148 Safari/605.1'
IOS_13_1_CHROME_77 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/77.0.3865.103 Mobile/15E148 Safari/605.1'
IOS_13_2_CHROME_78 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/78.0.3904.84 Mobile/15E148 Safari/604.1'
IOS_13_3_CHROME_79 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/79.0.3945.73 Mobile/15E148 Safari/604.1'


def test_ios():
    '''Test that iOS 12 shouldn't get the SameSite cookie, but iOS 9, 10, 11 and 13 should'''
    # Safari on iOS
    assert should_send_same_site_none(IOS_6_0_SAFARI_6) is True
    assert should_send_same_site_none(IOS_9_3_5_SAFARI_9) is True
    assert should_send_same_site_none(IOS_10_3_3_SAFARI_10) is True
    assert should_send_same_site_none(IOS_11_4_1_SAFARI_11) is True
    assert should_send_same_site_none(IOS_12_4_1_SAFARI_12_1) is False
    assert should_send_same_site_none(IOS_13_1_3_SAFARI_13) is True

    # Chrome on iOS
    assert should_send_same_site_none(IOS_9_3_5_CHROME_63) is True
    assert should_send_same_site_none(IOS_11_2_6_CHROME_65) is True
    assert should_send_same_site_none(IOS_11_4_1_CHROME_68) is True
    assert should_send_same_site_none(IOS_12_0_CHROME_69) is False
    assert should_send_same_site_none(IOS_12_0_CHROME_70) is False
    assert should_send_same_site_none(IOS_12_1_CHROME_70) is False
    assert should_send_same_site_none(IOS_12_3_CHROME_75) is False
    assert should_send_same_site_none(IOS_13_1_CHROME_77) is True
    assert should_send_same_site_none(IOS_13_2_CHROME_78) is True
    assert should_send_same_site_none(IOS_13_3_CHROME_79) is True

    # Other in-app browsers
    assert should_send_same_site_none(IOS_10_3_3_WEBKIT) is True
    assert should_send_same_site_none(IOS_11_4_WEBKIT) is True
    assert should_send_same_site_none(IOS_12_0_1_WEBKIT) is False
    assert should_send_same_site_none(IOS_12_1_WEBKIT) is False
    assert should_send_same_site_none(IOS_12_1_4_WEBKIT) is False
    assert should_send_same_site_none(IOS_12_3_WEBKIT) is False
    assert should_send_same_site_none(IOS_13_3_WEBKIT) is True
