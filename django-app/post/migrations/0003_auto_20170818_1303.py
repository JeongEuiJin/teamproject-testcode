# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170817_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('art', '미술'), ('photo', '사진'), ('video', '영상'), ('crafts', '공예'), ('piece', '조각'), ('install', '설치'), ('etc', '기타')], default='art', help_text='장르 선택', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='grade',
            field=models.IntegerField(choices=[(0, '전체관람가'), (12, '12세이상 관람가'), (15, '15세이상 관람가'), (18, '청소년 관람불가')], default=0, help_text='관람 선택'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('seoul', '서울'), ('busan', '부산'), ('incheon', '인천'), ('daejeon', '대전'), ('daegu', '대구'), ('ulsan', '울산'), ('gwangju', '광주'), ('gyeonggi', '경기도'), ('gangwon', '강원도'), ('chungcheonnam', '충청남도'), ('chungcheonbuk', '충청북도'), ('gyeongsangnam', '경상남도'), ('gyeongsangbuk', '경상북도'), ('jeollanam', '전라남도'), ('jeollabuk', '전라북도'), ('jeju', '제주')], default='seoul', help_text='지역 선택', max_length=50),
        ),
    ]
