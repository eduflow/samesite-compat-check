samesite-compat-check
=====================

[![Latest PyPI version](https://img.shields.io/pypi/v/samesite-compat-check.svg)](https://pypi.python.org/pypi/samesite-compat-check)
[![Latest Travis CI build status](https://travis-ci.org/peergradeio/samesite-compat-check.png)](https://travis-ci.org/peergradeio/samesite-compat-check)

This is a Python port of the [Chromium project's browser compatibility check] for `SameSite=None`-cookies.

samesite-compat-check exposes a single function `should_send_same_site_none`
which takes a `User-Agent` string and returns `True` if `SameSite=None` is
supported by the browser with the given `User-Agent` and `False` if not.

If `User-Agent` is `None` then `should_send_same_site_none` returns `True`.  
_This is the only addition on top of the pseudocode from the Chromium project_

The reason for this added behavior is to handle the case where the
`User-Agent`-header is not sent. The logic is that only  browsers that
specifically mishandle `SameSite=None` should have the attribute omitted. You
can safely send `SameSite=None`-attribute to a browser that doesn't recognize
the attribute (e.g. an older browser). As in that case `SameSite` will be
ignored, and you'll automatically get the behavior you intended, as cookies
before the `SameSite`-attibute were introduced worked as similar to
`SameSite=None`.

SameSite cookies
----------------
You probably already know what `SameSite`-cookies are -- if not, I recommend you
read <https://web.dev/samesite-cookies-explained/> at the very least.

`SameSite=None`-cookies are mostly relevant to people who needs cookies on CORS
requests or need cookies inside an iframe. So if you don't use cookies when
doing CORS or in iframes (or use `SameSite=None` for some other reason) you
can safely ignore this package.

You may say -- who uses iframes nowadays? Well, plenty of things do!
Youtube Embeds, the Intercom widget, that new little "Log in with Google"
popover on sites like Medium.

Well, if you're one those people who need `SameSite=None`, you'll find that a
good portion of your users have browsers that are incompatible with `SameSite`
cookies that have the value `None`.

That's where this library comes in. It checks the `User-Agent` string, and returns
whether it is from a browser that is incompatible. 

Recommendation is to just not use `SameSite` for those browsers. Since the
browsers are "old" and don't enforce the `SameSite`-rules for cookies where
the flag is not present, they will have the right behavior when you don't send
`SameSite=None`.

You'll need to pass in the value of the `User-Agent`-header from the library
you're using (Django, Flask...) and then either set or not set `SameSite=None`
on the cookie.

[Chromium project's browser compatibility check]: https://www.chromium.org/updates/same-site/incompatible-clients

Usage
-----
General use:

```python
from samesite_compat_check import should_send_same_site_none

if should_send_same_site_none(user_agent):
    # Set cookie with `SameSite=None`
else:
    # Set cookie without any `SameSite` attribute
```

### Django

```python
if should_send_same_site_none(request.META['HTTP_USER_AGENT']):
    response.cookies['my_precious_cookie']['samesite'] = 'None'
else:
    pass
```

Setting `response.set_cookie(..., samesite='none')` will be allowed from
Django 3.1 and onwards. Currently only `lax` and `strict` are allowed in
`response.set_cookie()`. Django only allows lowercase values for `samesite`.
Accoring to the spec lowercase/uppercase should not matter, however I have not
tested that particular detail in a browser.

### Flask

```python
from flask import request

kwargs = {}
if should_send_same_site_none(request.headers.get('User-Agent')):
    kwargs['samesite'] = 'None'

# Requires Werkzeug>=1.0.0 (a Flask dependency) in order to use `samesite` 
response.set_cookie(
    'my_precious_cookie', value='123abc', secure=True, **kwargs
)
```

Requirements
------------
`samesite-compat-check` has no dependencies and is tested on
Python 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, and PyPy 3.

Installation
------------

    pip install samesite-compat-check
    
Useful references
----------------
* <https://github.com/jotes/django-cookies-samesite>  
  This package serves as a good example of implementing the SameSite cookie in Django.  
  However, only checks for Chrome/Chromium version 51-66, not iOS, macOS, and UC Browser.
  However 
* <https://github.com/GoogleChromeLabs/samesite-examples>  
  This repo has examples for setting a cookie with the SameSite-attribute in Python and in Flask,
  but does not implement any of the browser incompatibility checks.
* <https://github.com/linsight/should-send-same-site-none>  
  A Javascript package similar to this one.
* <https://itnext.io/user-agent-sniffing-only-way-to-deal-with-upcoming-samesite-cookie-changes-6f79a18e541>  
  An alternative implementation in Javascript that isn't based off the Chromium project pseudocode.

Authors
-------
`samesite-compat-check` was written by `Malthe Jørgensen <malthe.jorgensen@gmail.com>` at Peergrade Inc.,
and is a port of Chromium's pseudocode for checking browsers incompatible with `SameSite=None` cookies
which can be found here:
<https://www.chromium.org/updates/same-site/incompatible-clients>

That pseudocode is Copyright 2019 Google LLC. and released under the Apache 2.0
license.

The tests use a sample of User-Agent strings from <https://developers.whatismybrowser.com/useragents/>.
