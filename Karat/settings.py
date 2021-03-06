"""
Django settings for Karat project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#######################################################################################################################
#######################################################################################################################
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 安全警告：对生产过程中使用的密钥保密！！！！！！！！！！！！
SECRET_KEY = '!%a#sk0v(8ynco0cyiiel5_+&%e$i^r2d1(jcij@iz_v=1_oc8'  # 勿动！！！！！！
# SECRET_KEY = '!%a#sk0v(8ynco0cyiiel5_+&%e$i^r2d1(jcij@iz_v=1_oc8' # 备份
# SECURITY WARNING: don't run with debug turned on in production!
# ##################安全警告：不要在生产中打开调试的情况下运行！！！！！！！！！！！！！！！！！#######################
DEBUG = True
#DEBUG = False        # DEBUG = False 无法正常加载静态页面     python manage.py runserver 0.0.0.0:8000 --insecure
######################################################################################################################

ALLOWED_HOSTS = ["*"]
#######################################################################################################################
#######################################################################################################################
# Application definition
# 应用程序定义

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webshell',
    'RootAPP',
    'KaratAPP',
    "WeChatAPP",
    "VoteAPP",
    "EmailAPP",
    "UserAPP",
    "MapAPP",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',#解决跨域问题
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Karat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'Templates'),
            os.path.join(BASE_DIR, 'RootAPP/Templates'),
            os.path.join(BASE_DIR, 'MapAPP/Templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Karat.wsgi.application'
######################################################################################################################
#####################################################################################################################
# Database
# 数据库

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'karat',
        # "USER":"root",
        # "PASSWORD":"Karat@2020",
        # "HOST":"127.0.0.1",
        # "PORT":"3306",
    }
}
#######################################################################################################################
#######################################################################################################################
# Password validation
# 密码验证
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
######################################################################################################################
######################################################################################################################
# Internationalization
# 国际化
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
######################################################################################################################
######################################################################################################################
# Static files (CSS, JavaScript, Images)
# 静态文件(CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
###################################################################################################################
# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
# 访问本服务器静态资源之用
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
####################################################################################################################
# 引用静态文件路径前填写'/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # 全局静态文件
    os.path.join(BASE_DIR, 'static'),
    # Dangerous document
    os.path.join(BASE_DIR, '/RootAPP/static'),
    # 全景地图静态文件
    os.path.join(BASE_DIR, 'MapAPP/static'),
)
################################################################################
# 视频图片文件
# 引用视频图片文件路径前填写'/media/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# 脚本文件
# 引用脚本文件路径前填写'/script/'
SCRIPT_URL = '/script/'
SCRIPT_ROOT = os.path.join(BASE_DIR, 'script')
###################################################################################
# RequestHost
#RequestHost="www.aicheteach.com/karat"
RequestHost="10.32.12.75:8000"
RequestHost="127.0.0.1:8000"
###################################################################################
####################################################################################################################
