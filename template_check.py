from typing import Dict


def template_check(template: Dict, form: Dict):
    """Compares template and form dicts, if all template keys are present in form
    and values match, returns True, else False"""

    tkeys = set(template.keys())
    fkeys = set(form.keys())
    inters = tkeys.intersection(fkeys)

    if inters == tkeys:
        for key in inters:
            if template[key] != form[key]:
                return False
        return True
    return False
