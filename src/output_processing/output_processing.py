from prompts.prompts import Prompts

import re

class OutputProcessor:
    def process(self, output: str):
        output = re.sub("^\w+:", "", output, 1)
        return output
