from flask import send_from_directory
import json
import os
from cert_issuer_identity import config

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def criteria_year_month_criteria_name_get(year, month, criteriaName):
    return 'do some magic!'

def issuer_issuer_filename_get(issuerFilename):
    return send_from_directory('issuer', issuerFilename, as_attachment=False)

def issuer_key_get(keyName):
    """Shows keys in the /keys folder"""

    key = get_key_by_name(keyName)
    if key:
        return key
    return 'Sorry, this page does not exist.', 404


def read_file(path):
    with open(path) as f:
        data = f.read()
    return data


def get_key_by_name(key_name):
    address = None
    if key_name == 'certs-public-key.asc':
        address = 'issuerKeys'
    elif key_name == 'certs-revoke-key.asc':
        address = 'revocationKeys'
    # TODO: improve this -- maybe load on startup?. Config file name
    issuer_file = read_file(os.path.join(BASE_DIR, 'issuer', config.default_issuer_file))
    issuer = json.loads(issuer_file)
    return issuer[address][0]['key']
