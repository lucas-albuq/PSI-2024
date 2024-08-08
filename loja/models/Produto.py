from loja.models import *

class Produto(models.Model):
    Produto = models.CharField(null=False, max_length=100)
    destaque = models.BooleanField(default=True)
    promocao = models.BooleanField(default=True)
    msgPromocao = models.CharField(null=True,max_length=100, blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, null=True, related_name = "categoria", on_delete=models.SET_NULL)
    fabricante = models.ForeignKey(Fabricante, null=True, related_name = "fabricante", on_delete=models.SET_NULL)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.Produto}"