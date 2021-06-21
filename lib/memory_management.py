import asyncio


class Memory:
    # Singleton
    __instance = None

    def __new__(cls, **kwargs):
        if Memory.__instance is None:
            Memory.__instance = object.__new__(cls)
            Memory.__instance._locks = {}
            Memory.__instance._memory = {}
        Memory.__instance.__dict__.update(**kwargs)
        return Memory.__instance

    async def get(self, key):
        result = None
        if key in self._locks:
            while True:
                if self._locks[key]:
                    await asyncio.sleep(1)
                else:
                    self._locks[key] = True
                    result = self._memory[key]
                    self._locks[key] = False
                    break
        return result

    async def set(self, key, value):
        if key not in self._locks:
            self._locks[key] = False
            self._memory[key] = None
        while True:
            if self._locks[key]:
                await asyncio.sleep(1)
            else:
                self._locks[key] = True
                self._memory[key] = value
                self._locks[key] = False
                break


def memory(f):
    async def new_f(*args, **kwargs):
        _memory = Memory()
        return await f(*args, **kwargs, memory=_memory)

    new_f.__name__ = f.__name__
    return new_f
