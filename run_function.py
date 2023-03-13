from cerberus import Validator

def validate_body(body):
    body_validator = Validator({
        'data': {
         'schema': {
             'age': {'type': 'integer', 'required': True,'empty': False},
             'height': {'type': 'float', 'required': False,'empty': False},
             'name': {'type': 'string', 'required': True,'empty': False},
             'document': {'type': 'string', 'required': False,'empty': True}
         }   
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)

    print('OK!')


input = {
    'data': {
        'age': 27,
        'height': 1.62,
        'name': 'Brunna',
        'document': ""
    }
}

validate_body(input)