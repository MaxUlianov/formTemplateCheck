from typing import Dict


def template_check(template: Dict, form: Dict):
    """Compares template and form dicts, if all template keys are present in form
    and values match, returns True, else False"""
    # print(f'\n\nchecking {repr(template)} and {repr(form)}\n')

    tkeys = set(template.keys())
    fkeys = set(form.keys())
    inters = tkeys.intersection(fkeys)

    # print(inters)

    if inters == tkeys:
        for key in inters:
            if template[key] != form[key]:
                return False
        return True
    return False


if __name__ == "__main__":
    tem = {"k1": "v1", "k2": "v2", "k3": "v3"}

    fr = {"k1": "v1", "k2": "v2", "k3": "v3"}
    fr2 = {"k1": "v1", "k5": "v2", "k6": "v3"}
    fr3 = {"k1": "aaa", "k2": "bbb", "k3": "ccc"}
    fr4 = {"k1": "v1", "k2": "v2"}

    print(template_check(tem, fr))
    print(template_check(tem, fr2))
    print(template_check(tem, fr3))
    print(template_check(tem, fr4))
