from typing import Dict


def template_check(template: Dict, form: Dict):
    """Compares template and form dicts, if all template keys are present in form
    and values match, returns True, else False"""
    # print(f'\n\nchecking {repr(template)} and {repr(form)}\n')

    tkeys = set(template.keys())
    fkeys = set(form.keys())
    inters = tkeys.intersection(fkeys)

    if inters == tkeys:
        for key in inters:
            if template[key] != form[key]:
                return False
        return True
    return False
