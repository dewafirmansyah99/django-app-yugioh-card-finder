from django.shortcuts import render, redirect
from .forms import TableForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pathlib import Path
from django.contrib import messages
import requests
from card.models import CardDatabase, CardClassic, CardByNumber, CardByName, CardBySpell, CardByTrap
from django.core.exceptions import ObjectDoesNotExist
import json
import os
import time
import base64
import io
import random
import logging

global_list = []
fav_card = []
flag_error = {
    "error": 1
}

def _insert_to_db(id_images, name_images, type_images, desc_images, card_images):
    CardDatabase(
        id_image=id_images,
        name_image=name_images,
        type_image=type_images,
        desc_image=desc_images,
        card_image=card_images
    ).save()

def _insert_classic_to_db(
        id_images,
        name_images,
        type_images,
        race_images,
        level_images,
        desc_images,
        card_images_small,
        card_images_ori,
    ):
    try:
        x = CardClassic.objects.filter(id_image=id_images)
        if x.exists():
            logging.info("SUDAH ADA DI DATABASE")
        else:
            CardClassic(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
    except ObjectDoesNotExist:
        CardClassic(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
        y = CardClassic.objects.filter(id_image=id_images)
        for yy in y:
            logging.info("{} {}".format(yy.name_image, "SUDAH DI MASUKKAN KE DATABASE"))

def _insert_by_number_to_db(
        id_images,
        name_images,
        type_images,
        race_images,
        level_images,
        desc_images,
        card_images_small,
        card_images_ori,
    ):
    try:
        x = CardByNumber.objects.filter(id_image=id_images)
        if x.exists():
            logging.info("{} {}".format(x, "SUDAH ADA DI DATABASE"))
        else:
            CardByNumber(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
    except ObjectDoesNotExist:
        CardByNumber(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
        y = CardByNumber.objects.filter(id_image=id_images)
        for yy in y:
            logging.info("{} {}".format(yy.name_image, "SUDAH DI MASUKKAN KE DATABASE"))

def _insert_by_name_to_db(
        id_images,
        name_images,
        type_images,
        race_images,
        level_images,
        desc_images,
        card_images_small,
        card_images_ori,
    ):
    try:
        x = CardByName.objects.filter(id_image=id_images)
        if x.exists():
            logging.info("{} {}".format(x, "SUDAH ADA DI DATABASE"))
        else:
            CardByName(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
    except ObjectDoesNotExist:
        CardByName(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
        y = CardByName.objects.filter(id_image=id_images)
        for yy in y:
            logging.info("{} {}".format(yy.name_image, "SUDAH DI MASUKKAN KE DATABASE"))

def _insert_by_spell_to_db(
        id_images,
        name_images,
        type_images,
        race_images,
        level_images,
        desc_images,
        card_images_small,
        card_images_ori,
    ):
    try:
        x = CardBySpell.objects.filter(id_image=id_images)
        if x.exists():
            logging.info("{} {}".format(x, "SUDAH ADA DI DATABASE"))
        else:
            CardBySpell(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
    except ObjectDoesNotExist:
        CardBySpell(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
        y = CardBySpell.objects.filter(id_image=id_images)
        for yy in y:
            logging.info("{} {}".format(yy.name_image, "SUDAH DI MASUKKAN KE DATABASE"))

def _insert_by_trap_to_db(
        id_images,
        name_images,
        type_images,
        race_images,
        level_images,
        desc_images,
        card_images_small,
        card_images_ori,
    ):
    try:
        x = CardByTrap.objects.filter(id_image=id_images)
        if x.exists():
            logging.info("{} {}".format(x, "SUDAH ADA DI DATABASE"))
        else:
            CardByTrap(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
    except ObjectDoesNotExist:
        CardByTrap(
            id_image=id_images,
            name_image=name_images,
            type_image=type_images,
            race_image=race_images,
            level_image=level_images,
            desc_image=desc_images,
            card_image_small=card_images_small,
            card_image_ori=card_images_ori
        ).save()
        y = CardByTrap.objects.filter(id_image=id_images)
        for yy in y:
            logging.info("{} {}".format(yy.name_image, "SUDAH DI MASUKKAN KE DATABASE"))


def _access_api_number(number):
    for _ in range(1, number+1, 1):
        url = "https://db.ygoprodeck.com/api/v7/randomcard.php"
        response = requests.get(url)
        data_json = response.json()["data"][0]
        name_images = data_json.get("name")
        logging.info("{} {}".format(name_images, "MASUK KE DATABASE"))
        id_images = data_json.get("id")
        type_images = data_json.get("type")
        race_images = data_json.get("race")
        level_images = data_json.get("level")
        desc_images = data_json.get("desc")
        card_images = data_json.get("card_images")[0]["image_url_small"]
        card_images_ori = data_json.get("card_images")[0]["image_url"]
        _insert_by_number_to_db(
            id_images,
            name_images,
            type_images,
            race_images,
            level_images,
            desc_images,
            card_images,
            card_images_ori
        )
    global global_list
    data = CardByNumber.objects.all().values('id')
    data_random = random.sample(list(data), number)
    global_list = CardByNumber.objects.filter(id__in=[item['id'] for item in data_random]).order_by('id')


def _access_api_name(name):
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?fname=" + name
    response = requests.get(url)
    data_json = response.json()
    if response.status_code == 400:
        flag_error["error"] = 0
    else:
        i = 1
        for _ in data_json["data"]:
            name_images = _.get("name")
            id_images = _.get("id")
            type_images = _.get("type")
            race_images = _.get("race")
            level_images = _.get("level")
            desc_images = _.get("desc")
            card_images = _.get("card_images")[0]["image_url_small"]
            card_images_ori = _.get("card_images")[0]["image_url"]
            _insert_by_name_to_db(
                id_images,
                name_images,
                type_images,
                race_images,
                level_images,
                desc_images,
                card_images,
                card_images_ori
            )
            global global_list
            global_list = CardByName.objects.filter(name_image__icontains=name).order_by('id')


def _access_api_combine_monster(type_monster, race_monster, level_monster):
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?"
    len_data_monster = []
    params = ()
    if type_monster:
        len_data_monster.append("&type={}".format(type_monster))
    if level_monster:
        len_data_monster.append("&level={}".format(int(level_monster)))
    if race_monster:
        len_data_monster.append("&race={}".format(race_monster))
    if len_data_monster:
        for lenght in len_data_monster:
            url += lenght
        response = requests.get(url.replace('?&', '?'))
        data_json = response.json()
        if response.status_code == 400:
            flag_error["error"] = 0
        else:
            for _ in data_json["data"]:
                name_images = _.get("name")
                id_images = _.get("id")
                type_images = _.get("type")
                race_images = _.get("race")
                level_images = _.get("level")
                desc_images = _.get("desc")
                card_images = _.get("card_images")[0]["image_url_small"]
                card_images_ori = _.get("card_images")[0]["image_url"]
                _insert_classic_to_db(
                    id_images,
                    name_images,
                    type_images,
                    race_images,
                    level_images,
                    desc_images,
                    card_images,
                    card_images_ori
                )
                global global_list
                if type_monster:
                    global_list = CardClassic.objects.filter(type_image=type_images).order_by('id')
                if level_monster:
                    global_list = CardClassic.objects.filter(level_image=level_images).order_by('id')
                if race_monster:
                    global_list = CardClassic.objects.filter(race_image=race_images).order_by('id')
    else:
        flag_error["error"] = 0


def _access_api_combine_spell(race_spell):
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?type=spell card&" + "race={}".format(race_spell)
    response = requests.get(url)
    data_json = response.json()
    if response.status_code == 400:
        flag_error["error"] = 0
    else:
        i = 1
        for _ in data_json["data"]:
            name_images = _.get("name")
            id_images = _.get("id")
            type_images = _.get("type")
            race_images = _.get("race")
            level_images = False
            desc_images = _.get("desc")
            card_images = _.get("card_images")[0]["image_url_small"]
            card_images_ori = _.get("card_images")[0]["image_url"]
            _insert_by_spell_to_db(
                id_images,
                name_images,
                type_images,
                race_images,
                level_images,
                desc_images,
                card_images,
                card_images_ori
            )
            global global_list
            global_list = CardBySpell.objects.filter(race_image=race_spell).order_by('id')


def _access_api_combine_trap(race_trap):
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?type=trap card&" + "race={}".format(race_trap)
    response = requests.get(url)
    data_json = response.json()
    if response.status_code == 400:
        flag_error["error"] = 0
    else:
        for _ in data_json["data"]:
            name_images = _.get("name")
            id_images = _.get("id")
            type_images = _.get("type")
            race_images = _.get("race")
            level_images = False
            desc_images = _.get("desc")
            card_images = _.get("card_images")[0]["image_url_small"]
            card_images_ori = _.get("card_images")[0]["image_url"]
            _insert_by_trap_to_db(
                id_images,
                name_images,
                type_images,
                race_images,
                level_images,
                desc_images,
                card_images,
                card_images_ori
            )
            global global_list
            global_list = CardByTrap.objects.filter(race_image=race_trap).order_by('id')


def _search_id(x):
    response = requests.get("{}{}".format("https://db.ygoprodeck.com/api/v7/cardinfo.php?id=", x))
    data_json = response.json()
    name_images = data_json["data"][0].get("name")
    id_images = data_json["data"][0].get("id")
    type_images = data_json["data"][0].get("type")
    desc_images = data_json["data"][0].get("desc")
    card_images = data_json["data"][0].get("card_images")
    converting_card = requests.get(card_images[0]["image_url_small"])
    return [
        id_images, name_images, type_images, desc_images, card_images
    ]


def index(request):
    ctx = {}
    messages.warning(request, 'Your Card is not found')
    global global_list
    # ctx["loop_card_link"] = global_list
    if request.method != 'POST' and 'page' in request.GET:
        if 'card-yugi' in request.session:
            request.POST = request.session['card-yugi']
    if request.method == 'POST':
        global_list = []
        form = TableForm(request.POST)
        request.session['card-yugi'] = request.POST
        if form.is_valid():
            number = form.cleaned_data['number']
            char = form.cleaned_data['char']
            monster = form.cleaned_data['monster']
            level = form.cleaned_data['level']
            race_monster = form.cleaned_data['race_monster']
            race_spell = form.cleaned_data['race_spell']
            race_trap = form.cleaned_data['race_trap']
            ctx["form"] = form
            ctx["number"] = number
            ctx["char"] = char
            ctx["monster"] = monster
            ctx["level"] = level
            ctx["race_monster"] = race_monster
            ctx["race_spell"] = race_spell
            ctx["race_trap"] = race_trap
            if not global_list:
                if number:
                    _access_api_number(number)
                if char:
                    _access_api_name(char)
                if monster or race_monster or level:
                    _access_api_combine_monster(monster, race_monster, level)
                if race_spell:
                    _access_api_combine_spell(race_spell)
                if race_trap:
                    _access_api_combine_trap(race_trap)
        return redirect("/card")
    else:
        form = TableForm()
        ctx["form"] = form
    object_list = global_list
    page_num = request.GET.get('page')
    paginator = Paginator(object_list, 6)
    try:
        ctx["page_obj"] = paginator.page(page_num)
    except PageNotAnInteger:
        ctx["page_obj"] = paginator.page(1)
    except EmptyPage:
        ctx["page_obj"] = paginator.page(paginator.num_pages)
    for t in ctx["page_obj"].object_list:
        logging.info("{} {}".format(t.name_image, "?"*30))
    ctx["style_base"] = 'card/css/style_base.css'
    ctx["bg_image"] = 'card/img/bg.jpg'
    ctx["icon_image"] = 'card/img/icon.png'
    ctx["svg_card"] = 'card/img/Card-Pixel.svg'
    ctx["svg_love"] = 'card/img/Love-Pixel.svg'
    ctx["svg_eye"] = 'card/img/Eye-Pixel.svg'
    ctx["svg_trash"] = 'card/img/Trash-Pixel.svg'
    ctx["frog_gif"] = 'card/img/frog.gif'
    ctx["js_toast"] = 'card/js/toast.js'
    ctx["js_cond_form"] = 'card/js/condition_form.js'
    ctx["js_cond_after_submit_form"] = 'card/js/condition_form_after_submit.js'
    ctx["pop_over"] = 'card/js/pop_over.js'
    ctx["delete_card"] = 'card/js/delete_card.js'
    ctx["favorite_card"] = 'card/js/favorite_card.js'
    ctx["modal_error"] = 'card/js/modal_error.js'
    ctx["js_bootpag"] = 'card/js/jquery.bootpag.js'
    ctx["error"] = flag_error["error"]
    ctx["pixel_font"] = "card/font/Pixellari.ttf"
    ctx["fav_card"] = []
    ctx["len_card"] = count_dicts(CardDatabase.objects.all().values())
    ctx["fav_card"] = CardDatabase.objects.all().values()
    return render(request, 'card.html', ctx)


def count_dicts(dictionary):
    return dictionary.count()


def another_page(request):
    arg = {}
    arg["name"] = request.GET.get("name")
    return render(request, 'pindah.html', arg)


def insert_favorite_to_bucket(request):
    number = request.GET.get("favorite")
    id_images, name_images, type_images, desc_images, card_images = _search_id(number)
    _insert_to_db(
        id_images,
        name_images,
        type_images,
        desc_images,
        card_images[0]["image_url"]
        
    )
    return redirect("/card")


def delete_favorite_from_bucket(request):
    number = request.GET.get("delete")
    CardDatabase.objects.filter(id_image=number).delete()
    time.sleep(3)
    return redirect("/card")
