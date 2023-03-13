from cerberus import Validator
    
schema = {
    'name': {'type': 'string'}
}
val = Validator(schema)

document = {
    'name': 'john doe'
}
response = val.validate(document)

print(response)
print(val.errors)