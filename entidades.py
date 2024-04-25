from PIL import Image
import requests
import time
from urllib.parse import urlparse
import os
import filtros

class Download:
    def __init__(self, url, path_arquivo):
        self.url = url
        self.path_arquivo = path_arquivo

    def download_file(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            with open(self.path_arquivo, 'wb') as file:
                file.write(response.content)
            print(f"Download completo. Arquivo salvo em: {self.path_arquivo}")
        except requests.exceptions.MissingSchema:
            raise ValueError("URL inválida. Certifique-se de fornecer uma URL válida.")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Erro na conexão: {str(e)}")

class Imagem:
    minha_imagem = None
    def __init__(self, nome_arquivo, path_arquivo):
        self.nome_arquivo = nome_arquivo
        self.local_referencia = path_arquivo
        try:
            self.minha_imagem = Image.open(path_arquivo)
        except Exception as ex:
            print(f'Erro ao criar a imagem com o arquivo {nome_arquivo} na referência {path_arquivo}: {str(str)}')

    def dimensoes(self):
        return self.minha_imagem.size

    def tamanho(self):
        return os.path.getsize(self.local_referencia)

    def formato(self):
        return self.minha_imagem.format

    def conteudo(self):
        return self.minha_imagem

    def __str__(self):
        return f'Nome: {self.nome_arquivo}, Dimensoes:{self.dimensoes()}, Formato: {self.formato()}, Tamanho: {self.tamanho()} Bytes'

class Util:
  def extrair_nome_extensao_url(self,url):
    parsed_url = urlparse(url)
    caminho_arquivo = parsed_url.path
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    return nome_arquivo, extensao

  def wait_for_file(self,file_path, interval=1):
      print('Aguarde...')
      while not os.path.exists(file_path):
        time.sleep(interval)
        interval = interval + 1
        print(".", end=" ")

class Main:
  def __init__(self, utilidades):
    self.utilidades = utilidades

  def get_recurso_imagem(self, minha_url):
    try:
        print(f'URL: {minha_url}')
        nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
        arquivo = nome_arquivo + extensao_arquivo
        print(f'Arquivo: {arquivo}')
        meu_download = Download(url=minha_url, path_arquivo=arquivo)
        print(f'Inicia download...')
        meu_download.download_file()
        print(f'Download concluído!')
        self.utilidades.wait_for_file(arquivo)
        imagem_teste = Imagem(nome_arquivo=arquivo, path_arquivo=arquivo)
        return imagem_teste.conteudo()
    except Exception as ex:
      raise ValueError("{str(ex)}")

  def aplica_filtro_grayscale(self,minha_imagem, nome):
    print('Aplicando filtro grayscale...')
    grayscale_filter = filtros.GrayscaleFilter()
    filtered_image_grayscale = grayscale_filter.apply_filter(minha_imagem)
    nome = nome + '_greyscale.jpg'
    filtered_image_grayscale.save(nome)
    print(f'Filtro grayscale aplicado com sucesso! Arquivo salvo em {nome}')

  def aplica_filtro_black_and_white(self,minha_imagem, nome):
    print('Aplicando filtro BlackAndWhite...')
    black_and_white_filter = filtros.BlackAndWhiteFilter()
    filtered_image_black_and_white = black_and_white_filter.apply_filter(minha_imagem)
    nome = nome + '_black_and_white.jpg'
    filtered_image_black_and_white.save(nome)
    print(f'Filtro black_and_white aplicado com sucesso! Arquivo salvo em {nome}')

  def aplica_filtro_edges(self,minha_imagem, nome):
    print('Aplicando filtro EdgesFilter...')
    edges_filter = filtros.EdgesFilter()
    filtered_image_edges_filter = edges_filter.apply_filter(minha_imagem)
    nome = nome + '_edges.jpg'
    filtered_image_edges_filter.save(nome)
    print(f'Filtro edges aplicado com sucesso! Arquivo salvo em {nome}')
