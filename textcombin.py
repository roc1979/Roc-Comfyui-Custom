class TextCombin:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "delimiter": ("STRING", {"default": "{{text_a}}{{text_b}} ","multiline":True}),
                        },
            "optional": {
                "text_a": ("STRING", {"forceInput": True}),
                "text_b": ("STRING", {"forceInput": True}),
                "text_c": ("STRING", {"forceInput": True}),
                "text_d": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "combintext"
    CATEGORY = "Roc_Nodes"

    def combintext(self, delimiter,  **kwargs):
        text_inputs = []

        # Handle special case where delimiter is "\n" (literal newline).
        if delimiter in ("\n", "\\n"):
            delimiter = "\n"
        result=delimiter
        # Iterate over the received inputs in sorted order.
        for k in sorted(kwargs.keys()):
            v = kwargs[k]
            
            temp=f"[[{k}]]"
            result= result.replace(temp,str(v))
            # Only process string input ports.
            # if isinstance(v, str):
            #     if clean_whitespace == "true":
            #         # Remove leading and trailing whitespace around this input.
            #         v = v.strip()

            #     # Only use this input if it's a non-empty string, since it
            #     # never makes sense to concatenate totally empty inputs.
            #     # NOTE: If whitespace cleanup is disabled, inputs containing
            #     # 100% whitespace will be treated as if it's a non-empty input.
            #     if v != "":
            #         text_inputs.append(v)

        # # Merge the inputs. Will always generate an output, even if empty.
        # merged_text = delimiter.join(text_inputs)

        return (result,)
