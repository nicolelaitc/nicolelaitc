import requests
import random, re
from favourites import favourites


def generate():
    playlist = favourites()
    favourite_ids = random.randint(0, len(playlist) - 1)
    video = playlist[favourite_ids]

    # get the thumbnails images
    match = re.match(r"https://youtu.be/([\w-]+)", video)
    video_id = match.group(1)
    image_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

    # get the youtube video title
    response = requests.get("https://www.youtube.com/watch?v={}".format(video_id))

    if response.status_code == 200:
        data = response.text
        match = re.search(r"<title>(.*?)</title>", data)
    if match:
        title = match.group(1)
        f = open("README.md", "w")
        f.write(
            " - 👋 Hi, I’m @yuiasora1024. \n - 💻 I am a junior back-end developer that has 1+ years of experience in Golang, Python and SQL. \n - 🌿 I hope to be a more advanced developer and create things that benefit people! \n - 👀 My recent favourites: \n"
        )
        f.write(
            f"""<p align="center">
            <a href="{video}">{title}</a><br>
        <img src="{image_url}">
        
    </p>
    """
        )
        f.close()

    return
