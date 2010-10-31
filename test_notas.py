#coding:utf-8
from nose.tools import *
from notas import conta_notas

def test_quando_digita_100_reais_deve_retornar_uma_nota_de_100():
	"Quando a entrada for 100, a saída deve ser uma nota de 100 reais"
	assert_equals(conta_notas(100), { '100' : 1 })

def test_quando_digita_60_reais_deve_retornar_uma_nota_de_50_e_uma_de_10():
	assert_equals(conta_notas(60), { '50' : 1, '10': 1 })

def test_quando_digita_50_reais_deve_retornar_uma_nota_de_50():
	assert_equals(conta_notas(50), { '50' : 1 })

def test_quando_digita_10_reais_deve_retornar_uma_nota_de_10():
	assert_equals(conta_notas(10), { '10' : 1 })

def test_quando_digita_200_reais_deve_retornar_duas_notas_de_100():
	assert_equals(conta_notas(200), { '100' : 2})

def test_quando_digita_25_reais_deve_retornar_uma_nota_de_20_e_uma_nota_de_5():
	assert_equals(conta_notas(25), { '20' : 1, '5' : 1})

def test_quando_digita_577_reais_deve_retornar_cinco_notas_de_100_uma_nota_de_50_uma_de_20_uma_de_5_e_uma_de_dois():
	assert_equals(conta_notas(577), { '100' : 5, '50' : 1, '20' : 1, '5' : 1, '2' : 1})

def test_quando_digita_578_reais_deve_retornar_cinco_notas_de_100_uma_nota_de_50_uma_de_20_uma_de_5_uma_de_dois_e_uma_de_um():
	assert_equals(conta_notas(578), { '100' : 5, '50' : 1, '20' : 1, '5' : 1, '2' : 1, '1' : 1})

def test_quando_digita_0_reais_deve_retornar_nada():
	assert_equals(conta_notas(0), {})

@raises(ValueError)
def test_quando_digita_menos_1_reais_deve_lancar_uma_excecao():
	conta_notas(-1)
