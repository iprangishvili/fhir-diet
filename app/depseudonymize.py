def perform_depseudonymization(resource, settings):
    return {'test': 123}


import fhirpathpy
from util import not_implemented
from actions.encrypt import encrypt_by_path

actions = {
    #"ttp": 'TODO',
    "encrypt": encrypt_by_path,
}

def perform_depseudonymization(resource, settings):
    for rule in settings.rules:
        fhirpathpy.engine.invocations['log'] = {'fn': lambda ctx, els: [{'path': x.path, 'value': x.data} for x in els]}
        matched_elements = fhirpathpy.evaluate(resource, rule['match'] + '.log()', [])
        for el in matched_elements:
            action = rule['action']
            if action in list(actions.keys()):
                actions[action](resource, el, rule['params'])
            else:
                not_implemented(f'Method {action} is not implemented')
    return resource
