from .tupleconvertstring import TupleConvertString
from .writetxtfile import *
from .textcombin import *
from .readtextfile import *

NODE_CLASS_MAPPINGS = {
    "TupleToString": TupleConvertString,
    "FileWriterNode": FileWriterNode,
    "TextCombin":TextCombin,
    "FileReadNode":FileReadNode,
   
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TupleToString": "TupleToString",
    "FileWriterNode": "WiteToTextFile",
    "TextCombin":"StringFormatOutput",
    "FileReadNode":"ReadTextFile",
    
}