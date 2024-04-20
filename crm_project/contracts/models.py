from django.db import models
from django.db.models import (
    CharField,
    FileField,
    DateField,
    DecimalField,
    ForeignKey
)

from products.models import Products


class Contracts(models.Model):
    """Модель для представления рекламных компаний."""

    name: CharField = models.CharField(
        max_length=200,
        verbose_name="Название",
        unique=True
    )
    product: ForeignKey = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="products",
    )
    file: FileField = models.FileField(
        upload_to="contracts/%Y/%m/%d",
        default=""
    )
    start_date: DateField = models.DateField(verbose_name="Дата начала")
    end_date: DateField = models.DateField(verbose_name="Дата окончания")
    cost: DecimalField = models.DecimalField(
        verbose_name="Сумма", max_digits=14, decimal_places=2
    )

    def __str__(self):
        return f"{str(self.name)} / {str(self.product)}"

    class Meta:
        """
        Указываем сортировку и имена которые будут указываться
        в админ панели.
        """

        ordering = ("name",)
        verbose_name = "контракт"
        verbose_name_plural = "контракты"
