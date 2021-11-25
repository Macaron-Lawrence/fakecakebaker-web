from os import truncate
from django import db
from django.shortcuts import render
from .models import Article
import datetime


dbtext_forum = {
    "name": "test_article",
    "title": "「红松林」|活动即将开启",
    "time": "2021|10|10",
    "classify": True,
    "form": "text",
    "content": """###[活动预告]故事集「红松林」即将开启
{{{20211014_2_1.JPG
<b>一、故事集「红松林」限时开启</b>
<b>关卡开放时间：</b>10月15日 16:00 - 10月22日 03:59
<br>
<b>【兑奖处】兑换奖励：</b><red>时装【巫异盛宴 - 安息处的怪盗 - 卡达】、家具【灰毫的收件箱】、家具【远牙的风铃】、事相碎片、</red>家具零件、作战记录、招聘许可、高级素材等"""
}

dbimage_forum = {
    "name": "test_image",
    "title": "「特定干员|限时出率上升",
    "time": "2021|10|10",
    "classify": True,
    "form": "image",
    "content": "main.bmp"
}

image_forum = {
    "form": "image",
    "title": "特定干员|限时出率上升",
    "image": "20211014_2_2.JPG"
}

text_forum = {
    "form": "text",
    "title": "「红松林」|活动即将开启",
    "time": "2021年10月10",
    "text_in_line": [
        {"form": "title",
         "content": "[活动预告]故事集「红松林」即将开启"},
        {"form": "image",
         "content": "20211014_2_1.JPG"},
        {"form": "p",
         "content": "<b>一、故事集「红松林」限时开启</b>"},
        {"form": "br",
         "content": "<br>"},
        {"content": "<b>【兑奖处】兑换奖励：</b><red>时装【巫异盛宴 - 安息处的怪盗 - 卡达】、家具【灰毫的收件箱】、家具【远牙的风铃】、事相碎片、</red>家具零件、作战记录、招聘许可、高级素材等"}
    ]
}


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