import simplejson


class CommandFactory():
    @staticmethod
    def serialize(self):
        params = {}
        for k in self.__slots__:
            params[k] = getattr(self, k)
        return simplejson.dumps(params)

    @staticmethod
    def unserialize(cls, params=None):
        if params is None:
            instance = cls()
        elif type(params).__name__ == 'dict':
            instance = cls(**params)
        elif type(params).__name__ in ('str', 'unicode'):
            instance = cls(**simplejson.loads(params))
        else:
            raise TypeError('argument must be None, dict, str, or unicode')
        return instance

    @staticmethod
    def parse_raw(json):
        parsed = simplejson.loads(json)
        if not hasattr(parsed, 'cmd'):
            raise AttributeError('No command specified')
        if not hasattr(parsed, 'args'):
            return parsed.get('cmd'), None
        return parsed.get('cmd'), parsed.get('args')


class Configurable():
    __slots__ = ()

    def __init__(self, **kwargs):
        for k in self.__slots__:
            if k in kwargs:
                setattr(self, k, kwargs.get(k))


class BaseCommand(Configurable):
    __slots__ = ('uuid', )

    def execute(self):
        raise TypeError('Not implemented!')


class Invoker():
    def __init__(self, cmd_map):
        self.cmd_map = cmd_map

    def invoke(self, cmd, args=None):
        cmd_cls = self.cmd_map.get(cmd)
        instance = CommandFactory.unserialize(cmd_cls, args)
        return instance.execute()

    def invoke_raw(self, data):
        cmd, args = CommandFactory.parse_raw(data)
        return self.invoke(cmd, args)
