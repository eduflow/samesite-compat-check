samesite-compat-check
=====================

[![Latest PyPI version](https://img.shields.io/pypi/v/samesite-compat-check.svg)](https://pypi.python.org/pypi/samesite-compat-check)
[![Latest Travis CI build status](https://travis-ci.org/peergradeio/samesite-compat-check.png)](https://travis-ci.org/peergradeio/samesite-compat-check)

This is a port of the [Chromium project's browser compatibility check] for `SameSite=None`-cookies.

You probably already know what `SameSite`-cookies are -- if not, I recommend you
read <https://web.dev/samesite-cookies-explained/> at the very least.

`SameSite=None`-cookies are mostly relevant to people who serve content inside
iframes. So if you don't use iframes or `SameSite=None` for other reasons you
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

    from samesite_compat_check import should_send_same_site_none

    if should_send_same_site_none(user_agent):
        # Set cookie with `SameSite=None`
    else:
        # Set cookie without any `SameSite` attribute

### Django

    if should_send_same_site_none(request.META['HTTP_USER_AGENT']):
        response.cookies['my_precious_cookie']['samesite'] = 'None'
    else:
        pass

Setting `response.set_cookie(..., samesite='none')` will be allowed from
Django 3.1 and onwards. Currently only `lax` and `strict` are allowed in
`response.set_cookie()`. Django only allows lowercase values for `samesite`.
Accoring to the spec lowercase/uppercase should not matter, however I have not
tested that particular detail in a browser.

### Flask

    from flask import request

    kwargs = {}
    if should_send_same_site_none(request.headers.get('User-Agent')):
        kwargs['samesite'] = 'None'

    # Requires Werkzeug>=1.0.0 (a Flask dependency) in order to use `samesite` 
    response.set_cookie(
        'my_precious_cookie', value='123abc', secure=True, **kwargs
    )


Installation
------------

    pip install samesite-compat-check

Requirements
------------

Python

Compatibility
-------------

Licence
-------
Apache 2.0

Authors
-------
`samesite-compat-check` was written by `Malthe Jørgensen <malthe.jorgensen@gmail.com>`,
and is a port of Chromium's pseudocode for checking browsers incompatible with `SameSite=None` cookies
which can be found here.
<https://www.chromium.org/updates/same-site/incompatible-clients>

That pseudocode is Copyright 2019 Google LLC. and released under the Apache 2.0
license.

The tests use a sample of User-Agent strings from <https://developers.whatismybrowser.com/useragents/>.