#!/usr/bin/env python3
"""COnfiguration"""

class Config:
    """Class that defines default languages & TImezones"""
    LANGUAGES = ["en", "fr"]  # List of supported languages
    BABEL_DEFAULT_LOCALE = "en"  # Default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone