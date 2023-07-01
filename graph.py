import networkx as nx
import matplotlib.pyplot as plt


def geraGrafo():
	#Criando um grafo g vazio
	g = nx.Graph()

	#Adicionando vertices com um conjuto de habilidades em cada vertice
	g.add_node(1, name='Pessoa 1', skills=['Habilidade 1', 'Habilidade 2'])
	g.add_node(2, name='Pessoa 2', skills=['Habilidade 2', 'Habilidade 3'])
	g.add_node(3, name='Pessoa 3', skills=['Habilidade 1', 'Habilidade 4'])
	
	# Adicionando ligaçoes
	g.add_edge(1, 2)
	g.add_edge(3, 2)
	
	# Define as posições dos vértices para plotar o grafo
	pos = nx.spring_layout(g)
	
	# Plota o grafo com as cores dos vértices definidas acima
	nx.draw(g, pos, with_labels=True)
	plt.show()


	return g 