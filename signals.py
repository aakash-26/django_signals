import threading
from .models import Student, StudentProfile
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver, Signal
import random

test_signal = Signal(providing_args=["name", "surname"])


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    from .middleware import RequestMiddleware
    request = RequestMiddleware(get_response=None)
    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user  # get logged in user

    if instance._state.adding:
        print("-------------inside pre save signal save ----------")

    else:
        try:
            instance._pre_save_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            instance._pre_save_instance = instance  # get instance before update

        print("-------------inside pre save signal update ----------")


@receiver(post_save, sender=Student)
def post_save_student(sender, instance, created, **kwargs):
    from .middleware import RequestMiddleware
    request = RequestMiddleware(get_response=None)

    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    if created == False:
        print("here post")
    else:
        print("-----------inside update-----------")


@receiver(pre_delete, sender=Student)
def post_delete_student(sender, instance, **kwargs):
    from .middleware import RequestMiddleware
    request = RequestMiddleware(get_response=None)

    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    print("-----------inside pre delete signal------------", user)
    print("-----record about to delete is -----------\n", instance)


@receiver(post_delete, sender=Student)
def post_save_student(sender, instance, **kwargs):
    from .middleware import RequestMiddleware
    request = RequestMiddleware(get_response=None)

    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    print("-----------inside post delete signal------------")
    print("-----deleted record is -----------\n", instance)


@receiver(test_signal)  # custom signal
def test_signal_test(sender, **kwargs):
    from .middleware import RequestMiddleware
    request = RequestMiddleware(get_response=None)

    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    print("-----------kwargs-------------", kwargs)
