import dataclasses
import random

import pytest
from rest_framework.test import APIClient

from students.models import Course
from model_bakery import baker


# def test_example():
#    assert False, "Just test example"


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return  baker.make(Course, *args, **kwargs)
    return factory



@pytest.mark.django_db
def test_one_course(client, course_factory):
    # Arrange
    course_test = course_factory(_quantity=1)[0]
    id_course = course_test.id

    # Act
    response = client.get(f'/api/v1/courses/{id_course}/', follow=True)

    # Assert
    #assert course_test.id == 1
    #print(course_test.name)
    assert response.status_code == 200
    data = response.json()
    #assert  data["name"] == "random name"

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