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
    beacon_local = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    tipo_local = models.ForeignKey(TipoLocal, on_delete=CASCADE)
    auxiliar = models.IntegerField(max_length=1)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'Local'
        verbose_name_plural = "Local"
        ordering = ("nome", "beacon_local")

class Beacon(models.Model):
    beacon_espaco  = models.BigIntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    auxiliar = models.IntegerField(max_length=1)

    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = 'Beacon'
        verbose_name_plural = "Beacon"
        ordering = ("nome", "beacon_espaco")

class Percurso(models.Model):
    sequencia = models.IntegerField()
    proximo_destino = models.ForeignKey(Beacon, on_delete=CASCADE)
    instrucao = models.TextField()

    def __str__(self):
        return str(self.proximo_destino)

    class Meta:
        db_table = 'Percurso'
        verbose_name_plural = "Percursos"

class Destino(models.Model):
    destino_final = models.ForeignKey(Beacon, on_delete=CASCADE)
    caminho = models.ManyToManyField(Percurso)
    
    def __str__(self):
        return str(self.destino_final)

    class Meta:
        db_table = 'Destino'
        verbose_name_plural = "Destinos"

class Espacos(models.Model):
    espaco = models.ForeignKey(Beacon, on_delete=CASCADE)
    destinos = models.ManyToManyField(Destino, null=True)
    
    class Meta:
        db_table = 'Espacos'
        verbose_name_plural = "Espaços"
    
class Locais(models.Model):
    local = models.ForeignKey(Local, on_delete=CASCADE)
    espacos = models.ManyToManyField(Espacos, null=True)
    
    class Meta:
        db_table = 'Locais'
        verbose_name_plural = "Locais My Friend"



class BeaconAA(models.Model):
    beacon_local = str
    beacon_espaco = str

class LocalApp(models.Model):
    beacon_local = str
    nome = str
    telefone = str
    texto = str
    def __init__(self, local: Local):
        aux = ["O", "A"]
        aux2 = ["o", "a"]
        self.nome = local['nome']
        self.beacon_local = local['beacon_local']
        self.telefone = local['telefone']
        self.texto = aux[local['auxiliar']]+" "+local['nome']+" fica localizad"+aux2[local['auxiliar']]+" em "+local['cidade']+ " "+ local['estado']+ " no endereço "+ local['endereco']+ " número "+ str(local['numero'])


