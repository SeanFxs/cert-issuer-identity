from flask import send_from_directory


def criteria_year_month_criteria_name_get(year, month, criteriaName):
    return 'do some magic!'

def issuer_issuer_filename_get(issuerFilename):
    return send_from_directory('issuer', issuerFilename, as_attachment=False)
