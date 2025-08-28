 # receitas/views.py 
from django.shortcuts import render, get_object_or_404 # Importe 
get_object_or_404 
from .models import Receita # <--- Importe o seu modelo Receita 
 
# Esta é a view que já existe para a página inicial 
def home(request): 
    # No futuro, você pode querer buscar as últimas receitas aqui para exibir na home 
    return render(request, 'receitas/home.html') 
 
# Nova view para exibir os detalhes de uma receita específica 
def receita_detail(request, id): # 'id' é o parâmetro que vem da URL 
    # Busca a receita no banco de dados usando o ID fornecido. 
    # Se a receita não for encontrada, ele automaticamente levanta um erro Http404. 
    receita = get_object_or_404(Receita, pk=id) # 'pk' significa Chave Primária (Primary Key), que é o ID 
 
    # Prepara o contexto para passar os dados da receita para o template 
    context = { 
        'receita': receita, # Passamos o objeto 'receita' inteiro para o template 
    } 
    return render(request, 'receitas/receita_detail.html', context) 
def pesquisar_receitas(request): 
    query = request.GET.get('q')  # pega o que foi digitado no campo de busca 
    resultados = [] 
    if query: 
# filtra receitas que contenham o termo no nome (sem case-sensitive)
        resultados = Receita.objects.filter(title__icontains=query) 
    context = { 
        'query': query, 
        'resultados': resultados, 
    } 
    return render(request, 'receitas/pesquisa.html', context)