import networkx as nx
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
	removido=False
	for vertice in grafo.nodes():

		if vertice.degree()==1:

			removerVertice=True
			for hab in vertice['skills']:

				if hab in T:

					removerVertice=False
					break

				else:

					continue
			if removerVertice:
				grafo.remove_node(vertice)
				removido=True
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