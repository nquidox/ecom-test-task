from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
import repository
from helpers import find_best_template, return_unmatched_types, validate_fields

router = APIRouter(tags=["Main"])


@router.post("/get_form")
async def get_form(r: Request):
    if r.headers.get('content-length') == '0':
        return Response(status_code=204)

    request_data = await r.json()
    typed_data = validate_fields(request_data)

    dbw = repository.dbworker()
    templates = dbw.get_all_templates()

    template_name = find_best_template(typed_data, templates)
    if template_name is None:
        resp = return_unmatched_types(request_data)
        return JSONResponse(content=resp, status_code=200)

    return Response(content=template_name, status_code=200)
