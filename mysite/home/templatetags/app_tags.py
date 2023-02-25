from hashlib import md5
from django import template

# https://brobin.me/blog/2016/07/super-simple-django-gravatar/

# A "gravatar" is a globally recognized avatar that is based on email address
# People must register their email address and then upload a gravatar
# If an email address has no gravatar, a generic image is put in its place

# To use the gravatar filter in a template include
# {% load app_tags %}

register = template.Library()

@register.filter(name='gravatar')
def gravatar(user, size=35):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
    return url.format(email_hash, size)


@register.filter(name='multipler')
def multiply(value):
    value = float(value)
    value = value * 100
    return "{}".format(round(value))


@register.filter(name='bgcolor')
def background(num):
    background = ['#07FFD2', '#07B0FF', '#0734FF', '#5607FF', '#D207FF', '#FF07B0']
    return background[num]