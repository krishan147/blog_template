def meInfo():
    import json

    parsed = json.load(open('me.json')) # change to add_your_about_info_here.json

    return parsed