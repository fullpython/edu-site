from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    age = models.PositiveIntegerField(null=True, blank=True)
    teachable_courses = models.ManyToManyField(
        Course
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cycle(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.PositiveIntegerField()

    PRICE_UNITS = (
        ('UZS', "So'm"),
        ('USD', 'AQSH Dollar')
    )
    price_unit = models.CharField(
        choices=PRICE_UNITS, default='UZS', max_length=6)

    def __str__(self):
        return f'{self.course} ---'

class Room(models.Model):

    name = models.PositiveIntegerField()
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}__{self.capacity}'

class CycleTime(models.Model):
    MONDAY = 'DUSHANBA'
    TUESDAY = 'SESHANBA'
    WEDNESDAY = 'CHORSHANBA'
    THURSDAY = 'PAYSHANBA'
    FRIDAY = 'JUMA'
    SATURDAY = 'SHANBA'
    SUNDAY = 'YAKSHANBA'
    WEEKDAYS = (
        (MONDAY, 'Du'),
        (TUESDAY, 'Se'),
        (WEDNESDAY, 'Cho'),
        (THURSDAY, 'Pa'),
        (FRIDAY, 'Ju'),
        (SATURDAY, 'Sha'),
        (SUNDAY, 'Ya'),
    )
    weekday = models.CharField(choices=WEEKDAYS, max_length=12)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    cycle = models.ForeignKey(
        Cycle,
        on_delete=models.CASCADE)
    teacher=models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Subscription(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    cycle = models.ForeignKey(
        Cycle,
        on_delete=models.CASCADE
    )

    registered_date = models.DateField()
