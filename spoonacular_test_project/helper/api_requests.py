import json
import requests
from allure_commons.types import AttachmentType
import logging
import allure


def api_get(url, **kwargs):
    with allure.step('API Request'):
        result = requests.get(url='https://api.spoonacular.com/' + url, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.request.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name=''"Response",
                      attachment_type=AttachmentType.JSON, extension='json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


def api_post(url, **kwargs):
    with allure.step('API Request'):
        result = requests.post(url='https://api.spoonacular.com/' + url, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.request.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name='Response',
                      attachment_type=AttachmentType.JSON, extension='json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


def api_delete(url, **kwargs):
    with allure.step('API Request'):
        result = requests.delete(url='https://api.spoonacular.com/' + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name='Response',
                      attachment_type=AttachmentType.JSON, extension='json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result


