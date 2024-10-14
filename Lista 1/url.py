import requests
from bs4 import BeautifulSoup
from collections import deque

# Função para extrair todos os links de uma página da web
def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()  # Usar um set para evitar duplicatas
        
        # Extrair todos os links
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            # Verifica se o link é válido (ignora links que não são URLs)
            if link.startswith('http'):
                links.add(link)
        
        return links
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return set()

# Função para encontrar o caminho de links de uma URL inicial para uma URL objetivo
def find_link_path(start_url, target_url):
    queue = deque([(start_url, [start_url])])  # Fila contendo URLs e o caminho até elas
    visited = set([start_url])  # Conjunto de URLs já visitadas
    
    while queue:
        current_url, path = queue.popleft()
        print(f"Visitando: {current_url}")
        
        # Obter todos os links da página atual
        for link in get_links(current_url):
            if link == target_url:
                return path + [link]  # Caminho completo encontrado
            if link not in visited:
                visited.add(link)
                queue.append((link, path + [link]))  # Adiciona o novo caminho
    
    return None  # Caso não haja caminho

# Teste da função
def test_link_path():
    start_url = 'https://exemplo.com/pagina_inicial'  # Substituir por uma URL real
    target_url = 'https://exemplo.com/pagina_objetivo'  # Substituir por uma URL real
    path = find_link_path(start_url, target_url)
    
    if path:
        print("Caminho encontrado:")
        for url in path:
            print(url)
    else:
        print("Nenhum caminho encontrado.")

# Executar o teste
test_link_path()
