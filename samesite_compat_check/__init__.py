# -*- encoding: utf-8 -*-
"""samesite-compat-check - A port of Chrome's browser compatibility check for SameSite=None cookies"""

__author__ = 'Malthe Jørgensen <malthe.jorgensen@gmail.com>'
__all__ = []

from .__version__ import __version__  # noqa: F401
from .check import should_send_same_site_none  # noqa: F401
