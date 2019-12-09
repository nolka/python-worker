from ..command import BaseCommand
from ..responses.response import BaseResponse


class ShellExecCommand(BaseCommand):

    def execute(self):
        return BaseResponse(uuid=self.uuid if hasattr(self, 'uuid') else None, code=1)
