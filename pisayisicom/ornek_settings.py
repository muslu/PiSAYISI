# -*- coding: utf-8 -*-
muslu = u"yüksektepe"

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'suit',
    'django.contrib.admin',
    'konular', 'tinymce'

)

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    # 'theme_advanced_buttons1': "newdocument,|,bold,italic,underline,|,justifyleft,justifycenter,justifyright,fontselect,fontsizeselect,formatselect",
    # 'theme_advanced_buttons2': "cut,copy,paste,|,bullist,numlist,|,outdent,indent,|,undo,redo,|,link,unlink,anchor,image,|,code,preview,|,forecolor,backcolor",
    # 'theme_advanced_buttons3': "insertdate,inserttime,|,spellchecker,advhr,,removeformat,|,sub,sup,|,charmap,emotions",
    'plugins': "emotions,spellchecker,advhr,insertdatetime,preview,paste,table,media,directionality,style,xhtmlxtras,nonbreaking,pagebreak",

    'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,ltr,rtl",
    'theme_advanced_buttons4': "styleprops,|,cite,abbr,acronym,del,ins,attribs,|,nonbreaking,pagebreak",
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'paste_text_sticky': True,
    'paste_text_sticky_default': True,
    'theme_advanced_resizing': True,
    'valid_styles': "@[id|class|style|title|dir<ltr?rtl|lang|xml::lang],"
                    + "a[rel|rev|charset|hreflang|tabindex|accesskey|type|"
                    + "name|href|target|title|class],strong/b,em/i,strike,u,"
                    + "#p[style],-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|"
                    + "src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup,"
                    + "-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|"
                    + "height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|"
                    + "height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot,"
                    + "#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor"
                    + "|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div,"
                    + "-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face"
                    + "|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite],"
                    + "object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width"
                    + "|height|src|*],map[name],area[shape|coords|href|alt|target],bdo,"
                    + "button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|"
                    + "valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method],"
                    + "input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value],"
                    + "kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value],"
                    + "q[cite],samp,select[disabled|multiple|name|size],small,"
                    + "textarea[cols|rows|disabled|name|readonly],tt,var,big",
    'extended_valid_elements': "p[style]",
    'inline_styles': True,
    'verify_html': False

}
DATABASES = {
    'default': {
        'NAME': 'pisayisicomDB',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'roootto',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'Pi Sayısı',
    'HEADER_DATE_FORMAT': 'j F Y l',  # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i:s',  # 18:42
    'CONFIRM_UNSAVED_CHANGES': False,
    'LIST_PER_PAGE': 100
}

logging.basicConfig(level=logging.INFO, format='%(message)s', filename='/home/muslu/django/djangoLog.log', )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_to_stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
    },
    'loggers': {
        'main': {
            'handlers': ['log_to_stdout'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

SECRET_KEY = 'dsfsdfs34v534v534v534v534v5345v34asdasdv53t54'

MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR + "/static/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

# EMAIL_BACKEND                                   =       'django.core.mail.backends.smtp.EmailBackend'
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.AppDirectoriesFinder', 'django.contrib.staticfiles.finders.FileSystemFinder',)
# IGNORABLE_404_URLS                              =       ( re.compile(r'^/apple-touch-icon.*\.png$'), re.compile(r'^/favicon\.ico$'), re.compile(r'^/robots\.txt$'),)
ADMINS = (('Muslu', 'musluyuksektepe@gmail.com'),)
MANAGERS = ADMINS
LANGUAGE_CODE = 'tr_TR'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = False
USE_TZ = False

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
ROOT_URLCONF = 'pisayisicom.urls'
WSGI_APPLICATION = 'pisayisicom.wsgi.application'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [BASE_DIR + "/templates"],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [

                "django.core.context_processors.debug",
                "django.core.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                # "django.core.context_processors.csrf",
            ],
        },
    },
]



# CACHES                                              = {
#                                                         'default': {
#                                                             'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#                                                             'LOCATION': '127.0.0.1:11211',
#                                                         }
#                                                     }
