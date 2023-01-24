from typing import Union

from fastapi import FastAPI

import uvicorn
import pytube


app = FastAPI()

@app.get("/streams/{url}")
def read_item(url: str):
    result={}
    try:
        yt = pytube.YouTube("https://www.youtube.com/watch?v="+url,proxies={"https":"127.0.0.1:7890","http":"127.0.0.1:7890"})
    except Exception as e:
        return {"error": str(e)}
    result["title"] = yt.title
    result["streams"] = []
    result["pic"] = yt.thumbnail_url
    result["views"] = yt.views
    result["keyword"] = yt.keywords
    temp={}
    for i in yt.streams.filter(file_extension='mp4',progressive=True):
        temp["itag"] = i.itag
        try:
            temp["resolution"] = i.resolution
        except:
            temp["resolution"] = "None"
        temp["fps"] = i.fps
        temp["vcodec"] = i.video_codec
        temp["filesize"] = i.filesize_mb
        temp["download_url"] = i.url
        result["streams"].append(temp.copy())
    return result
    # return {"url": url}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)