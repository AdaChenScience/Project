from mindformers.models.glm import GLMConfig, GLMChatModel
from mindformers.models.glm.chatglm_6b_tokenizer import ChatGLMTokenizer
import mindspore as ms
from mindformers.models.glm.glm_processor import process_response

import numpy as np
import time

config = GLMConfig(
    position_encoding_2d=True,
    use_past=True,
    is_sample_acceleration=True,
)

class llm:
    def __init__(self):
        self.model = GLMChatModel(config)
        self.tokenizer = ChatGLMTokenizer('./checkpoint_download/glm/ice_text.model')
        ms.load_checkpoint("./checkpoint_download/glm/glm_6b.ckpt", self.model)
        ms.set_context(mode=ms.GRAPH_MODE, device_target="Ascend", device_id=0)


    def call_generate(self,query,history=[]):
        if not history:
            prompt = query
        else:
            prompt = ""
            for i, (old_query, response) in enumerate(history):
                prompt += "[Round {}]\n问：{}\n答：{}\n".format(i, old_query, response)
            prompt += "[Round {}]\n问：{}\n答：".format(len(history), query)
        inputs = self.tokenizer(prompt)

        start_time = time.time()
        outputs = self.model.generate(np.expand_dims(np.array(inputs['input_ids']).astype(np.int32), 0),
                                 max_length=config.max_decode_length, do_sample=False, top_p=0.7, top_k=1)
        end_time = time.time()
        print(f'generate speed: {outputs[0].shape[0] / (end_time - start_time):.2f} tokens/s')
        response = self.tokenizer.decode(outputs)
        response = process_response(response[0])

        print(response)

        history = history + [(query, response)]
        return response,history


if __name__ == "__main__":
    llm = llm()

    while True:
        input_query = input("请输入：")
        response,history = llm.call_generate(input_query)
