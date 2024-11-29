import gradio as gr
import numpy as np
import torch
from diffusers import FluxFillPipeline
from PIL import Image
import random

MAX_SEED = np.iinfo(np.int32).max
MAX_IMAGE_SIZE = 2048
_pipe = FluxFillPipeline.from_pretrained("black-forest-labs/FLUX.1-Fill-dev", torch_dtype=torch.bfloat16).to("cuda")

def _xyz(a: Image.Image):
    _w, _h = a.size
    _min_ratio = 9 / 16
    _max_ratio = 16 / 9
    _fix_dim = 1024
    _r = _w / _h

    if _r > 1:
        _new_w = _fix_dim
        _new_h = round(_fix_dim / _r)
    else:
        _new_h = _fix_dim
        _new_w = round(_fix_dim * _r)

    _new_w = (_new_w // 8) * 8
    _new_h = (_new_h // 8) * 8

    _calc_ratio = _new_w / _new_h
    if _calc_ratio > _max_ratio:
        _new_w = (_new_h * _max_ratio // 8) * 8
    elif _calc_ratio < _min_ratio:
        _new_h = (_new_w / _min_ratio // 8) * 8

    _new_w = max(_new_w, 576) if _new_w == _fix_dim else _new_w
    _new_h = max(_new_h, 576) if _new_h == _fix_dim else _new_h

    return _new_w, _new_h

@spaces.GPU
def _abcd(_edit_images, _prompt, _seed=42, _rand_seed=False, _w=1024, _h=1024, _g_scale=3.5, _steps=28, _pg=gr.Progress(track_tqdm=True)):
    _img = _edit_images["background"]
    _w, _h = _xyz(_img)
    _mask = _edit_images["layers"][0]
    if _rand_seed:
        _seed = random.randint(0, MAX_SEED)
    _img = _pipe(
        prompt=_prompt,
        image=_img,
        mask_image=_mask,
        height=_h,
        width=_w,
        guidance_scale=_g_scale,
        num_inference_steps=_steps,
        generator=torch.Generator("cpu").manual_seed(_seed)
    ).images[0]
    return _img, _seed

_examples = [
    "a tiny astronaut hatching from an egg on the moon",
    "a cat holding a sign that says hello world",
    "an anime illustration of a wiener schnitzel",
]

_css = """
#col-container {
    margin: 0 auto;
    max-width: 1000px;
}
"""

with gr.Blocks(css=_css) as _demo:
    
    with gr.Column(elem_id="col-container"):
        gr.Markdown(f"""#)]
        """)
        with gr.Row():
            with gr.Column():
                _edit_image = gr.ImageEditor(
                    label='Upload and draw mask for inpainting',
                    type='pil',
                    sources=["upload", "webcam"],
                    image_mode='RGB',
                    layers=False,
                    brush=gr.Brush(colors=["#FFFFFF"], color_mode="fixed"),
                    height=600
                )
                _prompt = gr.Text(
                    label="Prompt",
                    show_label=False,
                    max_lines=1,
                    placeholder="Enter your prompt",
                    container=False,
                )
                _run_button = gr.Button("Run")
                
            _result = gr.Image(label="Result", show_label=False)
        
        with gr.Accordion("Advanced Settings", open=False):
            
            _seed = gr.Slider(
                label="Seed",
                minimum=0,
                maximum=MAX_SEED,
                step=1,
                value=0,
            )
            
            _rand_seed = gr.Checkbox(label="Randomize seed", value=True)
            
            with gr.Row():
                
                _w = gr.Slider(
                    label="Width",
                    minimum=256,
                    maximum=MAX_IMAGE_SIZE,
                    step=32,
                    value=1024,
                    visible=False
                )
                
                _h = gr.Slider(
                    label="Height",
                    minimum=256,
                    maximum=MAX_IMAGE_SIZE,
                    step=32,
                    value=1024,
                    visible=False
                )
            
            with gr.Row():

                _g_scale = gr.Slider(
                    label="Guidance Scale",
                    minimum=1,
                    maximum=30,
                    step=0.5,
                    value=50,
                )
  
                _steps = gr.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=50,
                    step=1,
                    value=28,
                )

    gr.on(
        triggers=[_run_button.click, _prompt.submit],
        fn = _abcd,
        inputs = [_edit_image, _prompt, _seed, _rand_seed, _w, _h, _g_scale, _steps],
        outputs = [_result, _seed]
    )

_demo.launch()
