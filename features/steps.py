# -*- coding: utf-8 -*-
from lettuce import step, world
from nose.tools import assert_equals
from notas import conta_notas

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Quando eu solicito "(.*)" reais')
def quando_eu_solicito_group1_reais(step, group1):
    world.valor = int(group1)

@step(u'Então eu devo obter "(.*)"')
def entao_eu_devo_obter_group1(step, group1):
	assert conta_notas(world.valor) == eval(group1)
