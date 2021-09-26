from django.forms import ModelForm
from app.models import Empresa, Produto

# Create the form class.
class EmpresaForm(ModelForm):
  class Meta:
    model = Empresa
    fields = ['nome', 'razao', 'cnpj', 'telefone', 'segmento']

class ProdutoForm(ModelForm):
  class Meta:
    model = Produto
    fields = ['nomep', 'tipo', 'preco', 'qtdade', 'fornecedor', 'empresa']
    

