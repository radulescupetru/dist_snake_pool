#!/usr/bin/env python3

import json
import sys
from dataclasses import dataclass, field

from dataclasses_json import config, dataclass_json


@dataclass_json
@dataclass
class Body:
    type_: str = field(metadata=config(field_name="type"))
    msg_id: int
    in_reply_to: int
    kwargs: field(default_factory=dict)
    
    def __post_init__(self):
        [setattr(self, k, v) for k, v in self.kwargs.items()]

@dataclass_json
@dataclass
class Message:
    src: str 
    dst: str = field(metadata=config(field_name="dest"))
    body: Body
    
    
if __name__ == "__main__":
    for line in sys.stdin:
        decoded = json.loads(line)
        print(decoded)