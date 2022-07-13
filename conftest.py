import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    druver = webdriver
