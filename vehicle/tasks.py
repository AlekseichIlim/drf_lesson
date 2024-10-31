from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage
            else:
                if prev_milage < m.milage:
                    print('Неверный пробег')
                    break
@shared_task
def check_filter():
    print('ghbhchvkbhljbgkjfkhcf')
