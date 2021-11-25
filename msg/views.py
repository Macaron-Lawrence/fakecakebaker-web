from os import truncate
from django import db
from django.shortcuts import render
from .models import Article
import datetime


def fromDBtoObj(obj):
    output = {}
    if obj["form"] == "text":
        output["form"] = "text"
        output["title"] = obj["title"].replace("|", "")
        time = obj["time"].split("|")
        prased_time = '%s年%s月%s日' % (time[0], time[1], time[2])
        output["time"] = prased_time
        content = obj["content"]
        content = content.split('\n')
        output["text_in_line"] = []
        for line in content:
            if line[0:3] == "###":
                output["text_in_line"].append(
                    {"form": "title", "content": line[3:]})
            elif line[0:3] == "{{{":
                output["text_in_line"].append(
                    {"form": "image", "content": obj['name'] + "/" + line[3:]})
            elif line == "<br>":
                output["text_in_line"].append({"form": "br", "content": line})
            else:
                output["text_in_line"].append({"form": "p", "content": line})
    elif obj["form"] == "image":
        output["form"] = "image"
        output["title"] = obj["title"].replace("|", "")
        output["image"] = obj['name'] + "/" + obj["content"]
    return output


def index(request):
    db_index = Article.objects.filter(is_active = True).values()
    sample = []
    for i in db_index:
        sample.append(
        {
            "name" : i["name"],
            "title" : i["title"].split("|"),
            "time" : i["time"].split("|")[1:3],
            "classify":i["classify"],
        }
        )
    return render(request, 'index.html', {"index": sample, "ifBR" : list(request.COOKIES.keys())})



def article(request, name):
    db_article = Article.objects.filter(name=name, is_active = True).values()[0]
    sample = {
        "name": name,
        "title": db_article["title"],
        "time": db_article["time"],
        "form": db_article["form"],
        "content": db_article["content"]
    }
    obj = fromDBtoObj(sample)
    if obj["form"] == "text":
        backup = render(request, 'article_text.html', {'obj': obj})
        backup.set_cookie(name,value = "unBR",max_age=60*60*24*180)
        return backup
    elif obj["form"] == "image":
        backup = render(request, 'article_image.html', {'obj': obj})
        backup.set_cookie(name,value = "unBR",max_age=60*60*24*180)
        return backup
    return None