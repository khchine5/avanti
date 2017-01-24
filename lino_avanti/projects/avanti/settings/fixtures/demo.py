# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""General demo data for Lino Avanti.

- Change name of persons and create a client MTI child for them.
- Course providers and courses

"""

from __future__ import unicode_literals
from django.conf import settings
from lino.utils import mti
from lino.utils.ssin import generate_ssin
from lino.utils import Cycler, join_words
# from lino.utils.instantiator import create_row
from lino.api import rt, dd, _

from lino.utils import demonames as demo

def get_last_names():
    yield demo.LAST_NAMES_MUSLIM
    yield demo.LAST_NAMES_RUSSIA
    yield demo.LAST_NAMES_AFRICAN

def get_male_first_names():
    yield demo.MALE_FIRST_NAMES_MUSLIM
    yield demo.MALE_FIRST_NAMES_RUSSIA
    yield demo.MALE_FIRST_NAMES_AFRICAN

def get_female_first_names():
    yield demo.FEMALE_FIRST_NAMES_MUSLIM
    yield demo.FEMALE_FIRST_NAMES_RUSSIA
    yield demo.FEMALE_FIRST_NAMES_AFRICAN

LAST_NAMES = Cycler(get_last_names())
MALES = Cycler(get_male_first_names())
FEMALES = Cycler(get_female_first_names())


def mtichild(p, model, **kw):
    c = mti.insert_child(p, model)
    for k, v in kw.items():
        setattr(c, k, v)
    c.save()
    return model.objects.get(pk=p.pk)

def objects():

    Person = rt.models.contacts.Person
    Client = rt.models.avanti.Client
    # Translator = rt.models.avanti.Translator
    TranslatorTypes = rt.actors.avanti.TranslatorTypes
    ClientStates = rt.actors.avanti.ClientStates
    # CourseProvider = rt.models.courses.CourseProvider
    Line = rt.models.courses.Line
    
    TT = Cycler(TranslatorTypes.objects())
    
    # def translator(name, **kwargs):
    #     kwargs.setdefault('translator_type', TT.pop())
    #     return Translator(name=name, **kwargs)

    def provider(name, **kwargs):
        # kwargs.setdefault('translator_type', TT.pop())
        return CourseProvider(name=name, **kwargs)

    # def series(name, cp, **kwargs):
    #     return Line(name=name, provider=cp, **kwargs)

    def series(name, **kwargs):
        return Line(name=name, **kwargs)

    # dist = BelgianDistribution()
    
    count = 0
    for person in Person.objects.all():
        count += 1
        if count % 7 and person.gender and not person.birth_date:
            # most persons, but not those from humanlinks and thos
            # with empty gender field, become clients and receive a
            # new exotic name. Youngest client is 16; 170 days between
            # each client
            birth_date = settings.SITE.demo_date(-170 * count - 16 * 365)
            national_id = generate_ssin(birth_date, person.gender)

            client = mtichild(
                person, Client, 
                national_id=national_id,
                birth_date=birth_date)

            if count % 2:
                client.client_state = ClientStates.coached
            elif count % 5:
                client.client_state = ClientStates.newcomer
            else:
                client.client_state = ClientStates.former

            # Dorothée is three times in our database
            if client.first_name == "Dorothée":
                client.national_id = None
                client.birth_date = ''
            else:
                p = client
                p.last_name = LAST_NAMES.pop()
                if p.gender == dd.Genders.male:
                    p.first_name = MALES.pop()
                    FEMALES.pop()
                else:
                    p.first_name = FEMALES.pop()
                    MALES.pop()
                p.name = join_words(p.last_name, p.first_name)

            
            if count % 4:
                client.translator_type = TT.pop()

            # client.full_clean()
            # client.save()
            yield client
        else:
            pass
            # yield mtichild(
            #     person, Translator, translator_type=TT.pop())

    # yield translator("Foo")
    # yield translator("Bar")
    # yield translator("Baz")

    # yield provider("Hinz")
    # yield provider("Kunz")
    # yield provider("Funz")

    # CP = Cycler(CourseProvider.objects.all())

    yield series(_("Citizen"))
    yield series(_("Alphabetisation"))
    yield series(_("German for beginners"))
    yield series(_("German A1+"))
    yield series(_("German A2"))
    yield series(_("German A2 (women)"))
        