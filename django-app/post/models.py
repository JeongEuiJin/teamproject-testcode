from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    GRADE_CHOICES = (
        (0, '전체관람가'),
        (12, '12세이상 관람가'),
        (15, '15세이상 관람가'),
        (18, '청소년 관람불가'),
    )
    GENRE_CHOICES = (
        ('art', '미술'),
        ('photo', '사진'),
        ('video', '영상'),
        ('crafts', '공예'),
        ('piece', '조각'),
        ('install', '설치'),
        ('etc', '기타'),
    )
    AREA_CHOICES = (
        ('seoul', '서울'),
        ('busan', '부산'),
        ('incheon', '인천'),
        ('daejeon', '대전'),
        ('daegu', '대구'),
        ('ulsan', '울산'),
        ('gwangju', '광주'),
        ('gyeonggi','경기도'),
        ('gangwon','강원도'),
        ('chungcheonnam', '충청남도'),
        ('chungcheonbuk', '충청북도'),
        ('gyeongsangnam', '경상남도'),
        ('gyeongsangbuk', '경상북도'),
        ('jeollanam', '전라남도'),
        ('jeollabuk', '전라북도'),
        ('jeju', '제주'),
    )

    poster_title = models.CharField(max_length=30)
    poster_img = models.ImageField(upload_to='poster/post_img/')
    genre = models.CharField(max_length=50,choices=GENRE_CHOICES,help_text='장르 선택', default='art')
    grade = models.IntegerField(choices=GRADE_CHOICES, help_text='관람 선택', default=0)
    poster_description = models.CharField(max_length=500, blank=True,null=True)
    fee = models.IntegerField()
    location = models.CharField(max_length=50,choices=AREA_CHOICES, help_text='지역 선택',default='seoul')
    place = models.CharField(max_length=100)
    thumbnail_img_1 = models.ImageField(upload_to='poster/thumbnail_1/')
    thumbnail_img_2 = models.ImageField(upload_to='poster/thumbnail_2/')
    time_start = models.TimeField(help_text='HH:MM')
    time_end = models.TimeField(help_text='HH:MM')
    date_start = models.DateField(help_text='YYYY-MM-DD')
    date_end = models.DateField(help_text='YYYY-MM-DD')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.poster_title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_created=True)