from dataclasses import dataclass

@dataclass
class FileDTO(object):

    context: str
    fname: str
    url: str
    dframe: object


    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> object: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

    @property
    def url(self) -> object: return self._url

    @url.setter
    def url(self, url): self._url = url

