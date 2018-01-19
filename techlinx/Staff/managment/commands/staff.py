from django.core.management.base import BaseCommand
from techlinx.Staff.models import Staff
from django.contrib.auth.models import User,Group
from faker import Faker



class Command(BaseCommand):
    help = "Crea 10 autores o 2 Editores"
    fake = Faker('es_MX')

    def _create_new_user(self,editor):
        name = self.fake.name().split(' ')[0:1]
        user = User.objects.create_user(
            username=self.fake.user_name(),
            password="techlinx2017",
            first_name=name,
            last_name=self.fake.last_name(),
            email = self.fake.email(),
            is_staff = True
        )
        grupo = Group.objects.get(name="Editores") if editor else Group.objects.get(name="Autores")
        grupo.user__set.add(user)

        return user

    def _create_new_staff(self,user,editor=False):
        user = user()
        num_staff = 2 if editor else 5
        for x in range(0,num_staff):
            staff = Staff.objects.create(
                user = user(),
                biografia = self.fake.text(),
                autor = not editor,
                editor = editor
            )



    def add_arguments(self,parser):
        parser.add_argument('-e','--Editor',dest="Editor")
    
    
    def handle(self,*args, **options):
        staff = Staff()
        
        if options['Editor']:
            pass
        else:
            pass