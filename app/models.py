from django.db import models

# Create your models here.
class Empresa(models.Model):
  id = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=150)
  razao = models.CharField(max_length=150)
  cnpj = models.CharField(max_length=150)
  telefone = models.CharField(max_length=150)
  segmento = models.CharField(max_length=100)
  

  def __str__(self):
      return self.nome + " - " 
      
class Produto(models.Model):
  id = models.IntegerField(primary_key=True)
  nomep = models.CharField(max_length=100)
  tipo = models.CharField(max_length=100)
  preco = models.CharField(max_length=100)
  qtdade = models.IntegerField()
  fornecedor = models.CharField(max_length=100)
  empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
