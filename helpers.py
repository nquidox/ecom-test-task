import validators


def validate_fields(data: dict) -> dict:
    typed = {}
    for k, v in data.items():
        match k:
            case "email":
                if validators.validate_email(data[k]):
                    typed[k] = k
            case "phone":
                if validators.validate_phone(data[k]):
                    typed[k] = k
            case "date":
                if validators.validate_date(data[k]):
                    typed[k] = k
            case _:
                if isinstance(v, str):
                    typed[k] = "string"
                elif isinstance(v, (int, float)):
                    typed[k] = "number"
    return typed


def find_best_template(data: dict, templates: list[dict]) -> dict:
    best_template = None
    max_matches = 0

    for template in templates:
        for template_name, fields in template.items():
            matches = sum(1 for key in fields if key in data)

            if matches > max_matches:
                max_matches = matches
                best_template = template_name

    return best_template


def return_unmatched_types(body: dict) -> dict:
    resp = {}
    for k, v in body.items():
        if isinstance(v, (int, float)):
            resp[k] = "number"
        elif str(v).lower() == "true" or str(v).lower() == "false":
            resp[k] = "boolean"
        elif isinstance(v, (list, set, tuple)):
            resp[k] = "array"
        elif isinstance(v, dict):
            resp[k] = "object"
        else:
            resp[k] = "string"
    return resp
