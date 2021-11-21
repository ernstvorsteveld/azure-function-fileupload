import logging
import json
import cgi

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    content_type = req.headers['Content-type']
    logging.info(f"{content_type}")
    if content_type == 'applicaton/json':
        return func.HttpResponse(json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'get_body': req.get_body().decode()
        }))

    ctype, pdict = cgi.parse_header(req.headers['Content-type'])
    if ctype == 'multipart/form-data':
        logging.info(f"{req.files['file']}")
        logging.info(f"{type(req.files['file'])}")
        return func.HttpResponse(req.files['file'].read())
    else:
        return func.HttpResponse(json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'get_body': req.get_body().decode()
        }))

    # if filename:
    #     return func.HttpResponse(f"Hello, {filename}. Uploaded your profile image file :{filename} to the blob. This function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
