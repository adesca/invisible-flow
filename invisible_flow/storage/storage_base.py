import abc


class StorageBase(abc.ABC):
    """Interface to an implementation of storage communication"""

    @abc.abstractmethod
    def get(self, filename, path):
        pass

    @abc.abstractmethod
    def store_byte_string(self, filename, file_content: bytes, path: str):
        pass

    @abc.abstractmethod
    def store_string_with_type(self, filename, file_content: bytes, path: str, file_type: str):
        pass
