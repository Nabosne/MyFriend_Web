from os import name
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class TipoLocal(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'TipoLocal'
        verbose_name_plural = "Tipos de Local"

class Local(models.Model):
    AUX_CHOICES = (
        (0, "O"),
        (1, "A"),
    )
    beacon_local = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tipo_local = models.ForeignKey(TipoLocal, on_delete=CASCADE)
    auxiliar = models.IntegerField(max_length=1, choices=AUX_CHOICES, blank=False, null=False)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'Local'
        verbose_name_plural = "Local"
        ordering = ("nome", "beacon_local")

class Espaco(models.Model):
    AUX_CHOICES = (
        (0, "O"),
        (1, "A"),
    )
    local = models.ForeignKey("Local", on_delete=models.CASCADE, related_name='espacos')
    beacon_espaco  = models.BigIntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    auxiliar = models.IntegerField(max_length=1, choices=AUX_CHOICES, blank=False, null=False)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'Espaco'
        verbose_name_plural = "Espaços"
        ordering = ("nome", "beacon_espaco")

class Destino(models.Model):
    espaco_inicio = models.ForeignKey("Espaco", on_delete=models.CASCADE, related_name='origem',null=False)
    espaco_final = models.ForeignKey("Espaco", on_delete=models.CASCADE, related_name='destino',null=False)

    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Destino'
        verbose_name_plural = "Destinos"

class Percurso(models.Model):
    destino = models.ForeignKey("Destino", on_delete=models.CASCADE, related_name='percursos')
    espaco_inicio = models.ForeignKey("Espaco", on_delete=models.CASCADE, related_name='espaco_inicio',null=False)
    espaco_fim = models.ForeignKey("Espaco", on_delete=models.CASCADE, related_name='espaco_fim',null=False)
    sequencia = models.IntegerField()
    instrucao = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Percurso'
        verbose_name_plural = "Percursos"

class Beacon(models.Model):
    beacon_local = str
    beacon_espaco = str

class LocalApp(models.Model):
    beacon_local = str
    nome = str
    telefone = str
    texto = str
    def __init__(self, local: Local):
        O_A = ["O", "A"]
        o_a = ["o", "a"]
        self.nome = local['nome']
        self.beacon_local = local['beacon_local']
        self.telefone = local['telefone']
        self.texto = O_A[local['auxiliar']]+" "+local['nome']+" fica localizad"+o_a[local['auxiliar']]+" em "+local['cidade']+ " "+ local['estado']+ " no endereço "+ local['endereco']+ " número "+ str(local['numero'])


