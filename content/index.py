config = {
    "template": "landing.j2",
    "title": "Urmila Bade | Architect",
    "content": """ [% md
    [Projects](projects)  |  [About]([% pylink /about.py %])  |  [Contact]([% pylink /contact.py %])
    %]
    """,
}
