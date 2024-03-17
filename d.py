import re
import requests

urls = [
    [
        "https://cdn.discordapp.com/icons/314103695568666625/a_2218d0b6249c84b129b66aed0fc7ad54.gif?size=56",
        "Cosmoteer"
    ],
    [
        "https://cdn.discordapp.com/emojis/402314812698394634.webp?size=96&quality=lossless",
        ":ActuallyNevermind:"
    ],
]

for url_entry in urls:
    print(f"loading {url_entry}")
    
    url = url_entry[0]
    name = url_entry[1]
    name = f"Discord emoji - {name.replace(":", "")}"

    url_filename_match_res = re.search(r".+\/(.*)\?", url)
    if not url_filename_match_res:
        raise Exception("cannot extract filename from url: " + url)
    
    extension = url_filename_match_res.group(1).split(".")[1]

    img_data = requests.get(url).content
    with open(f"result/{name}.{extension}", "w+b") as handler:
        handler.write(img_data)
