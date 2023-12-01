from transformers import BertTokenizer
from imagetotext import get_image_transform
from .tsv_io import load_from_yaml_file
from azfuse import File
from .model import get_git_model
from .torch_common import torch_load
from .torch_common import load_state_dict
from .process_image import load_image_by_pil
import torch

class img_cap:
    def __init__(self,model_name,param={},max_text_len = 40,prefix=''):

        if File.isfile(f'output/{model_name}/parameter.yaml'):
            param = load_from_yaml_file(f'output/{model_name}/parameter.yaml')

        self.param = param


        self.tokenizer = BertTokenizer.from_pretrained(param['bert_model'])

        model = get_git_model(self.tokenizer, param)
        pretrained = f'output/{model_name}/snapshot/model.pt'
        checkpoint = torch_load(pretrained)['model']
        load_state_dict(model, checkpoint)
        model.cuda()
        model.eval()

        self.model = model
        self.max_text_len = max_text_len
        self.prefix = prefix


    def gene_txt(self,img_path):

        if isinstance(img_path,str):
            image_path = [img_path]

        img = [load_image_by_pil(i) for i in image_path]

        transforms = get_image_transform(self.param)
        img = [transforms(i) for i in img]

        prefix_encoding = self.tokenizer(self.prefix,
                                    padding='do_not_pad',
                                    truncation=True,
                                    add_special_tokens=False,
                                    max_length=self.max_text_len)

        payload = prefix_encoding['input_ids']

        if len(payload) > self.max_text_len - 2:
            payload = payload[-(self.max_text_len - 2):]
        input_ids = [self.tokenizer.cls_token_id] + payload

        with torch.no_grad():
            result = self.model({
                'image': img,
                'prefix': torch.tensor(input_ids).unsqueeze(0).cuda(),
            })
        cap = self.tokenizer.decode(result['predictions'][0].tolist(), skip_special_tokens=True)

        return cap

