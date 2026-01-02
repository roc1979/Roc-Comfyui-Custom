
import os
import json
from datetime import datetime

class FileWriterNode:
    """
    ComfyUI自定义节点：将内容写入指定的文本文件
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "content": ("STRING", {
                    "multiline": True,
                    "default": "请输入要写入文件的内容..."
                }),
                
                "isappend":("BOOLEAN",{
                    "default":True,
                    "tooltip":"指定覆盖还是追加，True是追加，False是覆盖"
                }),
                "file_path": ("STRING", {
                    "default": "./output.txt",
                    "tooltip": "指定要写入的文件路径，可以是相对路径或绝对路径"
                }),
            },
            
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status_message",)
    FUNCTION = "write_to_file"
    CATEGORY = "Roc_Nodes"
    OUTPUT_NODE = True

    def write_to_file(self, content,isappend, file_path, append_mode=False):
        """
        将内容写入指定的文本文件
        """
        try:
            # 确保目录存在
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            if isappend: 
            # 确定写入模式
                mode = "a" 
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                timestamp_line = f"[{current_time}] "
                final_content ="\n" + timestamp_line + "\n" + content+ "\n"
            else:
                mode="w"
                final_content=content
            # 写入文件
            with open(file_path, mode, encoding="utf-8") as f:
                f.write(final_content)
            
            # 构建成功消息
            file_size = os.path.getsize(file_path)
            operation = "追加到" if append_mode else "写入"
            status_message = f"✅ 成功{operation}文件：{file_path}\n文件大小：{file_size} 字节"
            
            return (status_message,)
            
        except Exception as e:
            error_message = f"❌ 写入文件失败：{str(e)}"
            return (error_message,)


