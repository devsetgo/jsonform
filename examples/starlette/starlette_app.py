from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse

from json_form.forms import form_engine
import model

app = Starlette()


@app.route("/", methods=["GET"])
def index(request):
    result = form_engine(pydantic_model=model.MainModel)

    if request.method == "POST":
        print(request.form)

    context = {
        "request": request,
    }
    return HTMLResponse(result, context=context)
