import artist_filter as dbH
import requests
import os


def init_img_repo():
    if not os.path.isdir("images"):
        os.mkdir("images")
    else:
        os.rmdir("images")
        init_img_repo()


def download_images():
    DB = dbH.DB_handler()

    with open('data/target_artists.txt', "r", encoding="utf-8") as f:
        artists = f.readlines()


    for artist in artists:
        artist = artist.strip("\n")
        response = DB.get_paints_by_author(artist)

        if not os.path.isdir(f"images/{artist}"):
            os.mkdir(f"images/{artist}")
        
        for piece in response:
            url = piece["ThumbnailURL"]
            title = piece["Title"]
            title = ''.join(ch for ch in title if ch.isalnum())

            req = requests.get(url, allow_redirects=True)
            with open(f"images/{artist}/{title}.jpg", 'wb') as doc:
                doc.write(req.content)
            


if __name__ == "__main__":
    init_img_repo()
    download_images()