from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, '出席'),
        (2, '欠席'),
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    # tel = models.CharField(
    #     verbose_name='電話番号',
    #     max_length=200,
    # )
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
    age = models.CharField(
        verbose_name='Address',
        max_length=200,
    )
    sex = models.IntegerField(
        verbose_name='どちらかを選択ください',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
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
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'