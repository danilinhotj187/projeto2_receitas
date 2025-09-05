 # receitas/views.py 
from django.shortcuts import render, get_object_or_404 # Importe 
from .models import Receita # <--- Importe o seu modelo Receita 
 
# Esta é a view que já existe para a página inicial 
def home(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/home.html',{'receitas': receitas}) 
 
# Nova view para exibir os detalhes de uma receita específica 
def receita_detail(request, id): # 'id' é o parâmetro que vem da URL 
    # Busca a receita no banco de dados usando o ID fornecido. 
    # Se a receita não for encontrada, ele automaticamente levanta um erro Http404. 
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})
 
def pesquisar_receitas(request): 
    query = request.GET.get('q''')  # pega o que foi digitado no campo de busca 
    resultados = [] 
    if query:
# filtra receitas que contenham o termo no nome (sem case-sensitive)
     resultados = Receita.objects.filter(title__icontains=query)
    return render(request,'receitas/pesquisa.html', {'query': query,'resultados': resultados})
