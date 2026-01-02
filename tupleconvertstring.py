class TupleConvertString:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return{
            "required":{"text":("STRING",)}
        }
    
    RETURN_TYPES = "STRING"
    FUNCTION = "ToString"
    CATEGORY = "Roc_Nodes"

    def ToString(self,text):
        return text[0].encode('utf-8').decode('unicode-escape')

