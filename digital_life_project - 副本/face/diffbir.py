from typing import List
import math
import numpy as np
import torch
import einops
import pytorch_lightning as pl
from PIL import Image
from omegaconf import OmegaConf
from tqdm import tqdm

from ldm.xformers_state import disable_xformers
from model.spaced_sampler import SpacedSampler
from model.cldm import ControlLDM
from utils.image import auto_resize, pad
from utils.common import instantiate_from_config, load_state_dict


class ImageProcessor:
    def __init__(self, config_path: str, ckpt_path: str, device: str = "cuda", reload_swinir: bool = False, swinir_ckpt: str = ""):
        self.device = device
        if self.device == "cpu":
            disable_xformers()
        self.model: ControlLDM = instantiate_from_config(OmegaConf.load(config_path))
        load_state_dict(self.model, torch.load(ckpt_path, map_location="cpu"), strict=True)
        if reload_swinir:
            print(f"reload swinir model from {swinir_ckpt}")
            load_state_dict(self.model.preprocess_model, torch.load(swinir_ckpt, map_location="cpu"), strict=True)
        self.model.freeze()
        self.model.to(self.device)
        self.sampler = SpacedSampler(self.model, var_type="fixed_small")

    @torch.no_grad()
    def process(self, control_img: Image.Image, num_samples: int, sr_scale: int, disable_preprocess_model: bool, strength: float, positive_prompt: str, negative_prompt: str, cfg_scale: float, steps: int, use_color_fix: bool, seed: int, tiled: bool, tile_size: int, tile_stride: int) -> List[np.ndarray]:
        # [The existing code inside the process function goes here, adjusted as necessary]

        # Return the list of predictions
        return preds
