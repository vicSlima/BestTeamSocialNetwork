import graph
import skills

G=graph.geraGrafo()
T=skills.coletaSkills()

"""
Removendo vértices que não possuem habilidades necessárias
Critérios para remover:
-Ser de grau 1 (possuir apenas uma ligação)
-Não ter habilidade necessária em T
"""

def removendoVertices(grafo):
	removido = False
	for vertice in grafo.nodes():
		#remove vertices de grau 1 e remove os relentados
		if vertice.degree() in [0, 1] and not any(hab in T for hab in vertice['skills']):
			grafo.remove_node(vertice)
			removido = True
	return removido

limparGrafo=removendoVertices(G)

while limparGrafo:
	removendoVertices(G)

"""
Obtendo árvore geradora mínima
"""

g=nx.minimun_spanning_tree(G)

"""
Repetindo a 'limpeza' do grafo
"""

limparGrafo=removendoVertices(g)
while limparGrafo:
	removendoVertices(g)