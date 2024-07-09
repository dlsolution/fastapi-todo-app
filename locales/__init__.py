import i18n
from pydantic_i18n import PydanticI18n, JsonLoader
from os import path


i18n.set('fallback', "en")
i18n.set('locale', "en")
i18n.set('skip_locale_root_data', True)
i18n.set('file_format', 'json')
i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append(path.dirname(__file__))
loader = JsonLoader(path.join(path.dirname(__file__), 'validations'))
pydantic_trans = PydanticI18n(source=loader, default_locale="en")


def trans_pydantic_errors(errors):
    return pydantic_trans.translate(errors, locale=i18n.get('locale'))
