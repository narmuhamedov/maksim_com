from django.db import models

class NewsModel(models.Model):
    TYPE_NEWS = (
        ('Политика', 'Политика'),
        ('Шоубизнес', 'Шоубизнес'),
        ('Спорт', 'Спорт')
    )
    title = models.CharField(max_length=40, verbose_name='Название новости')
    image = models.ImageField(upload_to='news/', verbose_name='Загрузите фото')
    description = models.TextField(verbose_name='Полная новость')
    type_news = models.CharField(max_length=10, choices=TYPE_NEWS, verbose_name='Выберите тип новостей')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
    
    