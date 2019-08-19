from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, 'ご出席'),
        (2, 'ご欠席'),
    )

    name = models.CharField(
        verbose_name='ご芳名',
        max_length=200,
    )
    tel = models.CharField(
        verbose_name='お電話',
        max_length=200,
        null=True,
    )
    # addres = models.CharField(
    #     verbose_name='住所',
    #     max_length=200,
    # )
    # age = models.IntegerField(
    #     verbose_name='年齢',
    #     validators=[validators.MinValueValidator(1)],
    #     blank=True,
    #     null=True,
    # )

    yubin = models.CharField(
        verbose_name='ご住所',
        max_length=200,
        null=True,
    )
    address = models.CharField(
        verbose_name='',
        max_length=200,
        null=True,
    )

    sex = models.IntegerField(
        verbose_name='どちらかをお選びください',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='メッセージ',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'name'