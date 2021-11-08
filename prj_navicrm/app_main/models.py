from django.db import models

# Create your models here.

#-------------------------------------------- Организации
class tb_Organizations(models.Model):
    Name = models.CharField("Наименование", max_length=100)
    FullName = models.CharField("Полное наименование", max_length=200, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

#********************************

#-------------------------------------------- Типы ТС
class tb_CarsTypes(models.Model):
    Name = models.CharField("Наименование", max_length=100)
    FullName = models.CharField("Полное наименование", max_length=200, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Типы ТС"
        verbose_name_plural = "Тип ТС"
#************************************************************************************************

#-------------------------------------------- Марки ТС
class tb_MarksTypes(models.Model):
    Name = models.CharField("Наименование", max_length=100)
    FullName = models.CharField("Полное наименование", max_length=200, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Марки ТС"
        verbose_name_plural = "Марка ТС"
#************************************************************************************************

#-------------------------------------------- Список ТС
class tb_CarsList(models.Model):
    VIN = models.CharField("VIN номер", max_length=20, blank=True)
    GosNumber = models.CharField("Гос номер", max_length=20, blank=True)
    InventarNumber = models.CharField("Инвентарный номер", max_length=30, blank=True)
    WialonNumber = models.CharField("Номер в Виалон", max_length=20, blank=True)

    tb_Organizations_id = models.ForeignKey(tb_Organizations, verbose_name="Организация", on_delete=models.CASCADE)
    tb_CarsTypes_id = models.ForeignKey(tb_CarsTypes, verbose_name="Типы ТС", on_delete=models.CASCADE)
    tb_MarksTypes_id = models.ForeignKey(tb_MarksTypes, verbose_name="Марки ТС", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tb_CarsTypes_id} {self.tb_MarksTypes_id} {self.GosNumber}"

    class Meta:
        verbose_name = "ТС"
        verbose_name_plural = "Список ТС"
#************************************************************************************************

#-------------------------------------------- Производители оборудования
class tb_Produsers(models.Model):
    Name = models.CharField("Наименование", max_length=100)
    FullName = models.CharField("Полное наименование", max_length=200, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Производители оборудования"
        verbose_name_plural = "Производитель оборудования"
#************************************************************************************************

#-------------------------------------------- Типы оборудования
class tb_DevicesTypes(models.Model):
    Name = models.CharField("Наименование", max_length=100)
    FullName = models.CharField("Полное наименование", max_length=200, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Типы оборудования"
        verbose_name_plural = "Тип оборудования"
#************************************************************************************************

#-------------------------------------------- Марки оборудования
class tb_DevicesMarks(models.Model):
    Name = models.CharField("Наименование", max_length=100)

    tb_DevicesTypes_id = models.ForeignKey(tb_DevicesTypes, verbose_name="Типы устройствТС", on_delete=models.CASCADE)
    tb_Produsers_id = models.ForeignKey(tb_Produsers, verbose_name="Производитель оборудования", on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Марки оборудования"
        verbose_name_plural = "Марка оборудования"
#************************************************************************************************

#-------------------------------------------- Список оборудования
class tb_DevicesList(models.Model):
    SerialNumber = models.CharField("Наименование", max_length=100)
    tmp = models.CharField("Наименование", max_length=100)
    tb_DevicesMarks_id = models.ForeignKey(tb_DevicesMarks, verbose_name="Марка оборудования", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tb_DevicesMarks_id} {self.SerialNumber}"

    class Meta:
        verbose_name = "Список устройств"
        verbose_name_plural = "Устройство"
#************************************************************************************************