from llm import llm
from image_caption import img_cap

class generator:
    def __init__(self,model_name,param={},max_text_len = 40,prefix=''):
        self.model = llm()
        self.img_cap = img_cap(model_name,param={},max_text_len = 40,prefix='')

        self.translate_prompt_prefix = '将这句英语翻译为中文:'
        self.optimizre_prompt_prefix = '你被要求提供完成一个文本优化的任务。这些任务的输入是从图像提取出来的文本描述。要求对输入的内容进行优化,' \
                                       '格式如下：示例1.输入: 阳光和沙滩，输出: 阳光和沙滩，是夏天的样子。示例2.输入: 向日葵和阳光, 输出: 阳光下的向日葵，微笑和阳光一样美好。输入:’

    def call_generate(self,img_path):
        caption = self.img_cap.gene_txt(img_path)
        zh_prompt = self.translate_prompt_prefix + caption
        zh_res,_ = self.model.call_generate(zh_prompt)
        op_prompt = self.optimizre_prompt_prefix + zh_res + '输出:'
        op_res,_ = self.model.call_generate(op_prompt)
        return op_res
        
