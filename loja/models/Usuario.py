from loja.models import *

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.IntegerField(choices=PERFIL, default=2)
    aniversario = models.DateField(default=None, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"
    
    @receiver(post_save, sender=user)
    def create_user_usuario(sender, instance, created, **kwargs):
        try:
            if created:
                Usuario.objects.create(user=instance)
        except: 
            pass
    
    @receiver(post_save, sender=user)
    def save_user_usuario(sender, instance, **kwargs):
        try:
            instance.usuario.save()
        except:
            pass
    
