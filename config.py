# Define configuration as Python data structure
config = {
    "directories": {
        "content": "content",
        "template": "templates",
        "script": "scripts",
        "style": "styles",
        "media": "media",
        "output": "docs",
    },
    "default_template": "base.j2",
    "baseURL": "https://example.com",
    "languageCode": "en-us",
    "title": "My Website",
    "description": "This is my website",
    "author": "Urmila Bade",
    "keywords": "website, blog, portfolio",
    "copyright": "© Urmila Bade",
    "menu": [
        {"name": "Urmila Bade", "url": "[% pylink / %]"},
        {"name": "Projects", "url": "[% pylink /projects %]"},
        {"name": "About", "url": "[% pylink /about.py %]"},
        {"name": "Contact", "url": "[% pylink /contact.py %]"},
    ],
    "social": {
        "twitter": "ample",
        "github": "urmibade",
        "linkedin": "urmibade",
        "email": "urmibade@gmail.com",
    },
}
