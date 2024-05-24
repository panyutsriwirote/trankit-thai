from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "adapter_model": ["CamembertAdapterModel"],
}


if TYPE_CHECKING:
    from .adapter_model import CamembertAdapterModel

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
    )
