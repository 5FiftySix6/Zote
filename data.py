import json
import datetime
import time


def load():
    _frame = [
        "general",
        "ref",
        "meme",
        "speedrunning",
        "mods",
        "ignored",
        "silenced",
        "precept#",
        "precepts"
    ]
    _oldframe = [
        "general",
        "meme",
        "safememe",
        "supermeme",
        "reference",
        "speedrunning",
        "ignored",
        "silenced",
        "modonly",
        "mods",
        "ignoreList",
        "precept#",
        "numbers",
        "precepts"
    ]
    out = {}

    with open('config.json', 'r') as f:
        data = json.load(f)
        for key in _frame:
            out[key] = data[key]
    return out


def save():
    with open('config.json', 'w') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)


def log(name, ctx):
    try:
        u_name = ctx.message.author.name
        ch_name = ctx.message.channel.name
        time_formatted = datetime.datetime.fromtimestamp(time.time()).strftime('%c')
        s = "{0}, {1}, #{2}, {3}".format(u_name, name, ch_name, time_formatted)
        print(s)
        with open('log.zote', 'a') as f:
            f.write(s)
            f.write("\n")
    except UnicodeEncodeError as e:
        print("ERROR CODE 420. Unable to log command due to super dank name.")

config = load()