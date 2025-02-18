"""Collection of helper resources"""

class MetaEnum(type):
    """Iterate like an enum, but return the **actual** value"""
    def __new__(mcs, name, bases, attrs):
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def __iter__(cls):
        """Return every attribute that's not a dunder"""
        for attr in dir(cls):
            if not attr.startswith("__"):
                yield getattr(cls, attr)

    def __len__(cls):
        return len(cls._as_list())

    def __getitem__(cls, index):
        return cls._as_list()[index]

    @classmethod
    def _as_list(mcs):
        return [
            getattr(mcs, attr) for attr in dir(mcs)
            if not attr.startswith("__")
        ]
