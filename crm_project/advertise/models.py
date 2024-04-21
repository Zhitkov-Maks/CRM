from django.db import models
from django.db.models import CharField, DecimalField, ForeignKey

from products.models import Products


class PromotionChannel(models.Model):
    """
    Сделал канал продвижения чтобы их можно было просто выбрать
    при создании рекламных кампаний, так как их не так много."""
    name: CharField = models.CharField(
        max_length=200,
        verbose_name="Канал продвижения",
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        """
        Указываем как будут сортироваться каналы и
        как будет показываться название в админ панели.
        """
        ordering: tuple = ("name",)
        verbose_name: str = "канал продвижения"
        verbose_name_plural: str = "каналы продвижения"


class Advertise(models.Model):
    """Модель для представления рекламных компаний."""

    name: CharField = models.CharField(
        max_length=300,
        verbose_name="Кампания",
        unique=True
    )
    budget: DecimalField = models.DecimalField(
        verbose_name="Бюджет", max_digits=14, decimal_places=2
    )
    product: ForeignKey = models.ForeignKey(
        Products,
        verbose_name="Услуга",
        related_name="services",
        on_delete=models.CASCADE,
    )
    promotion_channel: ForeignKey = models.ForeignKey(
        PromotionChannel,
        verbose_name="Канал продвижения",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{str(self.name)}"

    class Meta:
        """
        Указываем как будут сортироваться рекламные кампании и
        как будет показываться название в админ панели.
        """
        ordering: tuple = ("name",)
        verbose_name: str = "кампания"
        verbose_name_plural: str = "кампании"
