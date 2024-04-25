import entidades

print("Programa que aplica filtros em uma imagem")

utilidades = entidades.Util()
meu_programa = entidades.Main(utilidades)

URL_EXEMPLO = 'https://raw.githubusercontent.com/armandossrecife/teste/main/space_picasso.jpeg' 
# extrai nome e extensao do arquivo apontado pela URL
nome_imagem, extensao_imagem = meu_programa.utilidades.extrair_nome_extensao_url(URL_EXEMPLO)

# Cria um recurso que aponta para uma imagem
imagem1 = meu_programa.get_recurso_imagem(minha_url=URL_EXEMPLO)

# Aplica filtros na imagem apontada e cria novas imagens de acordo com cada filtro
meu_programa.aplica_filtro_grayscale(minha_imagem=imagem1, nome=nome_imagem)
meu_programa.aplica_filtro_black_and_white(minha_imagem=imagem1, nome=nome_imagem)
meu_programa.aplica_filtro_edges(minha_imagem=imagem1, nome=nome_imagem)
