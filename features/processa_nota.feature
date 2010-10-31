#language:pt-br
Funcionalidade: Processar notas
	Para poder ter grana no bolso
	Como um usuário burro que não sabe contar
	Eu gostaria de sacar dinheiro num caixa

	Esquema do Cenário: Sacando um valor
		Quando eu solicito "<valor>" reais
		Então eu devo obter "<notas>"

		Exemplos:
			| valor | notas         |
			| 200   | { '100' : 2 } |
			| 223   | { '100' : 2, '20' : 1, '2' : 1, '1' : 1 } |
