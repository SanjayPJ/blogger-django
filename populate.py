
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'blogger.settings')

import django
django.setup()

import random
from django.template.defaultfilters import slugify
from article.models import Article
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_title = fakegen.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    fake_slug = slugify(fake_title)
    fake_body = fakegen.paragraph(nb_sentences=40, variable_nb_sentences=True, ext_word_list=None)
    user1 = Article.objects.get_or_create(title = fake_title, slug = fake_slug, body = fake_body)