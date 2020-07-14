import random
import faker
from django.utils.datetime_safe import datetime
from django.utils import timezone
from django.db.utils import IntegrityError
from django.utils.timezone import make_aware
from os import urandom

from apps.mainsite.app_models import (
    User,
    Course,
    Check,
    Site,
)
faker.Faker.seed(urandom(64))
fake = faker.Faker()
EDUCATIONS = [
    ("mid", ("Middle School")),
    ("high", ("High School")),
    ("univ", ("University")),
    ("mas", ("Master")),
    ("doc", ("Doctorate")),
    ("none", ("Not a Student")),
]


def fake_user(count):
    count = int(count)
    password = 'strongestpassword123'
    for i in range(int(count)):
        fp = fake.profile(),
        fp = fp[0]
        first_name, last_name = fp['name'].rsplit(maxsplit=1)
        new_user = User(
            username=fp['username'],
            first_name=first_name,
            last_name=last_name,
            email=fp['mail'],
            address=fp['address'],
            job=fp['job'],
            gender=fp['sex'],
            birth_date=fp['birthdate'],
            phone_number=fp['ssn'],
            current_education=random.choice(EDUCATIONS)[0]
        )
        new_user.set_password(password)
        try:
            new_user.save()
        except IntegrityError:
            print('SKIPPED! : USER')
            pass
        print('CREATED USER:', new_user)


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return make_aware(start + timezone.timedelta(seconds=random_second))


d1_start = datetime.strptime('01/01/2020', '%d/%m/%Y')
d2_end = datetime.strptime('06/06/2020', '%d/%m/%Y')
d3_start = datetime.strptime('06/28/2020', '%m/%d/%Y')
d4_end = datetime.strptime('12/28/2020', '%m/%d/%Y')


def fake_site(count):
    count = int(count)
    is_active = True
    home_url = 'index/'
    domain = 'localhost'
    needs_document = True
    for i in range(count):
        new_site = Site(
            needs_document=needs_document,
            name=fake.name(),
            is_active=is_active,
            home_url=home_url,
            domain=domain,
            year=str(random.randint(1980, 2100)),
            application_start_date=random_date(d1_start, d2_end),
            event_end_date=random_date(d3_start, d4_end),
            update_accommodation_end_date=random_date(d1_start, d2_end),
            docs_end_date=random_date(d1_start, d2_end),
            morning=random.uniform(1, 3),
            afternoon=random.uniform(1, 3),
            evening=random.uniform(1, 3),
        )
        try:
            new_site.save()
        except IntegrityError:
            pass
        print('CREATED SITE:', new_site)


def fake_course(count):
    count = int(count)
    sites = Site.objects.all()
    users_all = User.objects.all()
    lecturers = User.objects.filter(is_staff=True)
    for i in range(count):
        new_course = Course(
            site=random.choice(sites),
            name=fake.name(),
            description=fake.text(),
        )
        try:
            new_course.save()
            new_course.lecturer.add(random.choice(lecturers))
            new_course.assistant.add(random.choice(lecturers))
            new_course.participant.add(random.choice(users_all))
        except IntegrityError:
            pass
        print('CREATED COURSE:', new_course)


c1_start = datetime.strptime('01/1/2020 1:30 AM', '%m/%d/%Y %I:%M %p')
c1_end = datetime.strptime('01/1/2020 2:50 PM', '%m/%d/%Y %I:%M %p')

c2_start = datetime.strptime('01/1/2020 2:50 AM', '%m/%d/%Y %I:%M %p')
c2_end = datetime.strptime('01/1/2020 4:50 PM', '%m/%d/%Y %I:%M %p')


def fake_checks(count):
    count = int(count)
    courses = Course.objects.all()
    for i in range(count):
        new_check = Check(
            course=random.choice(courses),
            start_check=random_date(c1_start, c1_end),
            end_check=random_date(c2_start, c2_end)
        )
        try:
            new_check.save()
        except IntegrityError:
            pass
        print('CREATED CHECK:', new_check)

if __name__ == '__main__':
    print('Recommended user count is 100')
    fake_user(input('User count: ') or 100)
    print('Recommended Site count is 100')
    fake_site(input('Site count: ') or 100)
    print('Recommended Course count is 100')
    fake_course(input('Course count: ') or 100)
    print('Recommended Check count is 100')
    fake_checks(input('Check count: ') or 100)