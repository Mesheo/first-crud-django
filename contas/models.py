from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data = models.DateTimeField()
    tipo_de_transacao = models.ForeignKey(Categoria, on_delete=models.CASCADE)   
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao
