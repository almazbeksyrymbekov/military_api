from django.db import models

class TroopType(models.Model): 
    name = models.CharField(max_length=100, unique=True, verbose_name="Название вида войск")
    description = models.TextField(verbose_name="Описание этого войска", null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид войск"
        verbose_name_plural = "Виды войск"


class Location(models.Model): 
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    area = models.FloatField(verbose_name="Занимаемая площадь (кв. м)")

    def __str__(self):
        return f"{self.city}, {self.country} ({self.address})"

    class Meta:
        verbose_name = "Место дислокации"
        verbose_name_plural = "Места дислокации"


class MilitaryUnit(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name="Номер части")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="military_units", verbose_name="Место дислокации")
    troop_type = models.ForeignKey(TroopType, on_delete=models.CASCADE, related_name="military_units", verbose_name="Вид войск")
    number_of_platoons = models.PositiveIntegerField(verbose_name="Количество рот")

    def __str__(self):
        return f"Часть №{self.number}"

    class Meta:
        verbose_name = "Часть"
        verbose_name_plural = "Части"


class Platoon(models.Model):  
    name = models.CharField(max_length=100, verbose_name="Название роты")
    number_of_personnel = models.PositiveIntegerField(verbose_name="Количество служащих")
    military_unit = models.ForeignKey(MilitaryUnit, on_delete=models.CASCADE, related_name="platoons", verbose_name="Часть")

    def __str__(self):
        return f"{self.name} (Часть №{self.military_unit.number})"

    class Meta:
        verbose_name = "Рота"
        verbose_name_plural = "Роты"


class Personnel(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, related_name="personnel", verbose_name="Рота")
    position = models.CharField(max_length=100, verbose_name="Должность")
    birth_year = models.PositiveIntegerField(verbose_name="Год рождения")
    service_start_year = models.PositiveIntegerField(verbose_name="Год поступления на службу")
    years_of_service = models.PositiveIntegerField(verbose_name="Выслуга лет")
    awards = models.TextField(blank=True, verbose_name="Награды")
    military_events = models.TextField(blank=True, verbose_name="Участие в военных мероприятиях")

    def __str__(self):
        return f"{self.last_name} ({self.position})"

    class Meta:
        verbose_name = "Личный состав"
        verbose_name_plural = "Личный состав"
    