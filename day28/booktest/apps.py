from django.apps import AppConfig


class BooktestConfig(AppConfig): 
    # AppConfig作用: 用于配置应用程序的元数据
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booktest'
