import os
import json
from datetime import datetime

class FileReadNode:
    """
    ComfyUI自定义节点：将内容写入指定的文本文件
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                    "file_path": ("STRING", {
                    "default": "",
                    "tooltip": "指定要读取的文件路径，可以是相对路径或绝对路径"
                }),
            },
            
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("outputstring",)
    FUNCTION = "read_text_file"
    CATEGORY = "Roc_Nodes"
    OUTPUT_NODE = True

    def read_text_file(self, file_path):
        """
        将内容写入指定的文本文件
        """
        try:
            # 确保目录存在
            if os.path.exists(file_path):
                outputstring=""
            
            # 读取文件
            with open(file_path, "r", encoding="utf-8") as f:
               outputstring= f.read()
                
            # 构建成功消息
           
            
            return (outputstring,)
            
        except Exception as e:
            error_message = f"❌ 写入文件失败：{str(e)}"
            return (error_message,)