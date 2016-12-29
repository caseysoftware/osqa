from django.contrib import messages
from forum import settings, REQUEST_HOLDER
from django.core.management.base import NoArgsCommand
from forum.models import User
import sys

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        msg = None
        if msg == None:
            print 'to run this command, please first edit the file %s' % __file__
            sys.exit(1)
        for u in User.objects.all():
            messages.info(REQUEST_HOLDER.request, message = msg % u.username)
