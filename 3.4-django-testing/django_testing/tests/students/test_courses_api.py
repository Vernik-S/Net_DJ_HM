import dataclasses

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
