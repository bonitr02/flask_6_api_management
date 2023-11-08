# This app was run in Visual Studio Code
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
def blood_glucose(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('This Blood Glucose HTTP function processed your request')

     bg = req.params.get('bg')

     return func.HttpResponse(
             "This Blood Glucose HTTP-triggered function executed successfully. Enter a blood glucose value in the query string or in the request body.",
             status_code=200
        )