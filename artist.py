from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler, DDPMScheduler, AutoencoderKL
import torch
import random
from PIL import Image

PIPE = DiffusionPipeline.from_pretrained(
    "prompthero/openjourney", 
    torch_dtype=torch.float32
)
PIPE.scheduler = DPMSolverMultistepScheduler.from_config(PIPE.scheduler.config)
PIPE.vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=torch.float32)
NOISE_SCHEDULER = DDPMScheduler()
DENOISE_STEPS = 5
DIMENSIONS = (400, 600)

def decode_latent(latent):
    images = PIPE.vae.decode(torch.unsqueeze(latent, dim=0) / PIPE.vae.config.scaling_factor)[0].detach()
    do_denormalize = None
    if do_denormalize is None:
        do_denormalize = [PIPE.image_processor.config.do_normalize] * images.shape[0]
    images = torch.stack(
        [PIPE.image_processor.denormalize(images[i]) if do_denormalize[i] else images[i] for i in range(images.shape[0])]
    )
    images_np = PIPE.image_processor.pt_to_numpy(images)
    images_pil = PIPE.numpy_to_pil(images_np)
    return images_pil[0]

def noise_latent(input_latent):
    torch.manual_seed(1)
    noise = torch.randn((4, 50, 75))
    timesteps = torch.LongTensor([750])  # Somewhere between 500 and 999 seems to be good
    noisey_latent = noise_scheduler.add_noise(input_latent, noise, timesteps)
    return noisey_latent

def denoise_latent(input_latent, prompt=None, guidance=9):
    output_latent = PIPE(
        prompt = [prompt],
        num_inference_steps=DENOISE_STEPS,
        guidance_scale=guidance,
        height = DIMENSIONS[0],
        width = DIMENSIONS[1],
        generator = [torch.Generator().manual_seed(0)],
        latents = torch.unsqueeze(input_latent, dim=0),
        output_type = 'latent',
    ).images[0]
    return output_latent

# Linear interpolation in latent space between latent from prompt1 and latent from prompt2
def generate_frames(prompt1, prompt2, num_frames):
    assert num_frames >= 2
    torch.manual_seed(0)
    input_latent = torch.randn((4, 50, 75))
    output_latent1 = denoise_latent(input_latent, prompt=prompt1)
    output_latent2 = denoise_latent(input_latent, prompt=prompt2)
    frames = []
    latent_step_vector = (output_latent2 - output_latent1) / (num_frames - 1)
    for i in range(num_frames):
        frame = decode_latent(output_latent1 + i * latent_step_vector)
        frames.append(frame)
    return frames

# Linear interpolation between latent from prompt and unguided latent conditioned on latent from prompt
def generate_frames_no_guidance(prompt, num_frames):
    pass

# Linear interpolation between latent from prompt1 and latent conditioned on prompt1, renoised, and guided by prompt2
def generate_frames_new_guidance(prompt1, prompt2, num_frames):
    pass

if __name__ == "__main__":
    prompt1 = "Jungle with vines. Majestic lighting. Hyper realism. Symmetric artwork. Cinematic. High detail. 8k. --ar 2:3"
    prompt2 = "Underwater coral reef. Majestic lighting. Hyper realism. Symmetric artwork. Cinematic. High detail. 8k. --ar 2:3"
    frames = generate_frames(prompt1, prompt2, 4)
    for i, frame in enumerate(frames):
        frame.save(f"frame{i}.jpg")
