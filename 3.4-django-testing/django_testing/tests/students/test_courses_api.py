import dataclasses
import json
import random
from pprint import pprint

import pytest
from django.conf import settings
from rest_framework.test import APIClient

from students.models import Course, Student
from model_bakery import baker


# def test_example():
#    assert False, "Just test example"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_one_course(client, course_factory):
    # Arrange
    course_test = course_factory(_quantity=1)[0]
    id_course = course_test.id

    # Act
    response = client.get(f'/api/v1/courses/{id_course}/', follow=True)

    # Assert
    # assert course_test.id == 1
    # print(course_test.name)
    assert response.status_code == 200
    data = response.json()
    # assert  data["name"] == "random name"

    assert data["name"] == course_test.name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    # Arrange
    courses_test = course_factory(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/', follow=True)

    # Assert

    assert response.status_code == 200
    data = response.json()

    assert len(data) == len(courses_test)

    for i, response_course in enumerate(data):
        assert response_course['name'] == courses_test[i].name


@pytest.mark.django_db
def test_id_filter_courses(client, course_factory):
    # Arrange
    courses_test = course_factory(_quantity=10)
    random_course = random.choice(courses_test)

    # Act
    response = client.get(f'/api/v1/courses/?id={random_course.id}', follow=True)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data[0]

    assert data[0]["name"] == random_course.name


@pytest.mark.django_db
def test_name_filter_courses(client, course_factory):
    # Arrange
    courses_test = course_factory(_quantity=10)
    random_course = random.choice(courses_test)

    # Act
    response = client.get(f'/api/v1/courses/?name={random_course.name}', follow=True)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data[0]

    assert data[0]["id"] == random_course.id


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_create_course(client, student_factory):
    # Arrange

    students_test = student_factory(_quantity=10)

    test_course_body = {
        "name": "Test Course",
        "students": [student_test.id for student_test in students_test]
    }
    test_course_json = json.dumps(test_course_body)

    count_before_create = Course.objects.count()

    # pprint(test_course_json)

    # Act
    response = client.post(f'/api/v1/courses/', data=test_course_json, follow=True, content_type="application/json")
    # pprint(response.json())

    # Assert
    assert response.status_code == 201
    data = response.json()
    # pprint(data)
    assert data["name"] == "Test Course"
    assert len(data["students"]) == len(students_test)
    assert Course.objects.count() > count_before_create


@pytest.fixture
def test_course():
    return Course.objects.create(name="Test Course")


@pytest.mark.django_db
def test_update_course(client, test_course, student_factory):
    # Arrange

    students_test = student_factory(_quantity=10)

    test_course_update_body = {
        "name": "New Name",
        "students": [student_test.id for student_test in students_test]
    }
    test_course_json = json.dumps(test_course_update_body)

    # Act
    response_patch = client.patch(f'/api/v1/courses/{test_course.id}/', data=test_course_json, follow=True,
                                  content_type="application/json")
    response_get = client.get(f'/api/v1/courses/{test_course.id}/', follow=True)
    # pprint(response.json())

    # Assert
    assert response_patch.status_code == 200
    data = response_get.json()
    pprint(data)
    assert data["name"] == "New Name"
    assert len(data["students"]) == len(students_test)


@pytest.mark.django_db
def test_delete_course(client, test_course):
    # Arrange

    # Act
    response_del = client.delete(f'/api/v1/courses/{test_course.id}/', follow=True, )
    response_get = client.get(f'/api/v1/courses/{test_course.id}/', follow=True)
    # pprint(response.json())

    # Assert
    assert response_del.status_code == 204
    assert response_get.status_code == 404


@pytest.mark.parametrize(
    ["max_students_test", "expected_status"],
    (
            (1, 400),
            (4, 400),
            (5, 201),
    )
)
@pytest.mark.django_db
def test_max_students(client, student_factory, max_students_test, expected_status):
    # Arrange

    students_test = student_factory(_quantity=5)
    settings.MAX_STUDENTS_PER_COURSE=max_students_test

    test_course_body = {
        "name": "Test Course",
        "students": [student_test.id for student_test in students_test]
    }
    test_course_json = json.dumps(test_course_body)

    # Act
    response = client.post(f'/api/v1/courses/', data=test_course_json, follow=True, content_type="application/json")
    # pprint(response.json())

    # Assert
    assert response.status_code == expected_status