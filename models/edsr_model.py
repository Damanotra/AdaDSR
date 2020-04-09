import torch
from .dsr_model import DSRModel, base_SRModel
from .networks import AdaResBlock, AdaRCAGroup

class EDSRModel(DSRModel):
    @staticmethod
    def modify_commandline_options(parser, is_train=True):
        parser.set_defaults(
            n_resblocks = 32,
            n_feats = 256,
            block_mode = 'CRC'
        )
        return parser

    def __init__(self, opt):
        super(EDSRModel, self).__init__(opt, SRModel=SRModel)
        self.model_names = ['EDSR']
        self.optimizer_names = ['EDSR_optimizer_%s' % opt.optimizer]
        self.netEDSR = self.netDSR


class SRModel(base_SRModel):
    def __init__(self, opt):
        self.block = AdaResBlock
        self.n_blocks = opt.n_resblocks
        self.block_name = 'block'
        super(SRModel, self).__init__(opt)