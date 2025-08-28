# receitas/models.py 
from django.db import models 
 
class Receita(models.Model): 
    title = models.CharField(max_length=200) 
    description = models.TextField() 
    ingredients = models.TextField() 
    instructions = models.TextField() 
    # Campo para a imagem da receita 
    # upload_to='receitas/images/' significa que as imagens serão salvas em media/receitas/images/ 
    image = models.ImageField(upload_to='receitas/images/', blank=True, 
null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
 
    def __str__(self): 
        return self.title 
 
    class Meta: 
        verbose_name = "Receita" 
        verbose_name_plural = "Receitas" 
        ordering = ['-created_at'] # Ordena as receitas pela data de criação (mais novas primeiro)