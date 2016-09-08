from .base import *

INSTALLED_APPS += [
	'django_extensions',
	'debug_toolbar',
] 


DEBUG_TOOLBAR_PATCH_SETTINGS = False

def show_toolbar(request):
    print('Em show_toolbar - ip=' + request.META['REMOTE_ADDR'])
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar



INTERNAL_IPS = ('192.168.99.1', '127.0.0.1', '0.0.0.0')
print('\n\n\n\n\n*********** env=dev ************')
