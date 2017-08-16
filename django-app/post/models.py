from django.db import models


class PostList(models.Model):
    GRADE_CHOICES = (
        (0, '전체관람가'),
        (12, '12세이상 관람가'),
        (15, '15세이상 관람가'),
        (18, '청소년 관람불가'),
    )
    poster_title = models.CharField(max_length=30)
    poster_img = models.ImageField(upload_to='poster/post_img/')
    genre = models.CharField(max_length=30)
    grade = models.IntegerField(choices=GRADE_CHOICES, help_text='관람 선택', default=1)
    fee = models.IntegerField()
    location = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    thumbnail_img_1 = models.ImageField(upload_to='poster/thumbnail_1/')
    thumbnail_img_2 = models.ImageField(upload_to='poster/thumbnail_2/')
    time = models.TimeField(help_text='HH:MM')
    date_start = models.DateField(help_text='YYYY-MM-DD')
    date_end = models.DateField(help_text='YYYY-MM-DD')
