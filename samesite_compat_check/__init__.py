# -*- encoding: utf-8 -*-
"""samesite-compat-check - A port of Chrome's browser compatibility check for SameSite=None cookies"""

__version__ = '0.1.0'
__author__ = 'Malthe Jørgensen <malthe.jorgensen@gmail.com>'
__all__ = []

from .check import should_send_same_site_none  # noqa: F401
