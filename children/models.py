from django.db import models


class Children(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=255)
    diagnosis = models.CharField(verbose_name="Диагноз",max_length=255)
    dream_text = models.TextField(verbose_name="Мечта (текст)",)
    gift = models.CharField(verbose_name="Подарок",max_length=255)
    gift_price = models.IntegerField(verbose_name="Цена подарка",default=0, null=True, blank=True)
    active = models.BooleanField(verbose_name="Активна",default=True)
    photo = models.ImageField(verbose_name="Фото",upload_to="avatars/")
    phone_number = models.CharField("Номер телефона", max_length=30)
    address = models.TextField("Адрес", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Дети"
        verbose_name_plural = "Дети"


class Application(models.Model):
    class Type(models.TextChoices):
        DREAM = "DREAM", "Мечта"
        SELF = "SELF", "Лично"
        ORGRANIZATION = "ORGANIZATION", "Организация"

    type = models.CharField(
        "Тип заявки",
        choices=Type.choices,
        default=Type.DREAM,
    )
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField("Номер телефона", max_length=30)
    dream = models.TextField("Мечта", null=True, blank=True)
    time_to_call = models.DateTimeField(
        verbose_name="Время звонка",
        null=True,
        blank=True,
    )
    child = models.ForeignKey(
        Children,
        on_delete=models.PROTECT,
        verbose_name="Ребенок",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"
