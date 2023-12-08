# import sys
# sys.path.append('./Diffusion-Pullback/src/')
# from utils.utils import get_stable_diffusion_model

from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler, DDPMScheduler, AutoencoderKL
import torch
import random
from PIL import Image
from run_diffusion import diffusion

class Args:
    model_name="prompthero/openjourney"
    dtype=torch.float32
    device=torch.device("cpu")

args = Args()
if torch.cuda.is_available():
    args.device = torch.device("cuda")

# PIPE = get_stable_diffusion_model(args)
PIPE = DiffusionPipeline.from_pretrained(
    "prompthero/openjourney", 
    torch_dtype=torch.float32
)
PIPE.scheduler = DPMSolverMultistepScheduler.from_config(PIPE.scheduler.config)
PIPE.vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=torch.float32)
NOISE_SCHEDULER = DDPMScheduler()
DENOISE_STEPS = 10
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

def noise_latent(input_latent, timesteps):
    torch.manual_seed(1)
    noise = torch.randn((4, 50, 75))
    # timesteps = torch.LongTensor([750])  # Somewhere between 500 and 999 seems to be good
    timesteps = torch.LongTensor([timesteps])  # Somewhere between 500 and 999 seems to be good
    noisey_latent = NOISE_SCHEDULER.add_noise(input_latent, noise, timesteps)
    return noisey_latent

def denoise_latent(input_latent, prompt=None, embed=None, guidance=9, **kwargs):
    if prompt is not None:
        embed, negative_embed = PIPE.encode_prompt(prompt, torch.device('cpu'), 1, True)
    output_latent = diffusion(PIPE,
        prompt_embeds = embed,
        num_inference_steps=DENOISE_STEPS,
        guidance_scale=guidance,
        height = DIMENSIONS[0],
        width = DIMENSIONS[1],
        generator = [torch.Generator().manual_seed(0)],
        latents = torch.unsqueeze(input_latent, dim=0),
        output_type = 'latent',
        **kwargs,
    ).images[0]
    return output_latent

def interpolate_latents(latent1, latent2, num_frames):
    latent_step_vector = (latent2 - latent1) / (num_frames - 1)
    frames = []
    for i in range(num_frames):
        frame = decode_latent(latent1 + i * latent_step_vector)
        frames.append(frame)
    return frames

# Linear interpolation in latent space between latent from prompt1 and latent from prompt2
def generate_frames(prompt1, prompt2, num_frames):
    assert num_frames >= 2
    torch.manual_seed(0)
    input_latent = torch.randn((4, 50, 75))
    output_latent1 = denoise_latent(input_latent, prompt=prompt1)
    output_latent2 = denoise_latent(input_latent, prompt=prompt2)
    frames = interpolate_latents(output_latent1, output_latent2)
    return frames

def generate_frames_embed_space(prompt1, prompt2, num_frames):
    assert num_frames >= 2
    torch.manual_seed(0)
    input_latent = torch.randn((4, 50, 75))
    embed1, _ = PIPE.encode_prompt(prompt1, torch.device('cpu'), 1, True)
    embed2, _ = PIPE.encode_prompt(prompt2, torch.device('cpu'), 1, True)
    embed_step_vector = (embed2 - embed1) / (num_frames - 1)
    frames = []
    for i in range(num_frames):
        output_latent = denoise_latent(input_latent, embed=(embed1 + i * embed_step_vector))
        frame = decode_latent(output_latent)
        frames.append(frame)
    return frames

# def generate_frames_noise_space(prompt1, prompt2, num_frames):
#     assert num_frames >= 2
#     torch.manual_seed(0)
#     input_latent = torch.randn((4, 50, 75))
#     output_latent1 = denoise_latent(input_latent, prompt=prompt1)
#     output_latent2 = denoise_latent(input_latent, prompt=prompt2)
#     noisy_latent1 = noise_latent(output_latent1)
#     noisy_latent2 = noise_latent(output_latent2)
#     noise_step_vector = (noisy_latent2 - noisy_latent1) / (num_frames - 1)
#     for i in range(num_frames):
#         output_latent = denoise_latent(noisy_latent1 + i * noise_step_vector, prompt=prompt1, guidance=0)
#         frame = decode_latent(output_latent)
#         frame.save(f"frames/frame{i}.jpg")

# def generate_frames_noise_space(prompt1, prompt2, num_frames):
#     assert num_frames >= 2
#     torch.manual_seed(0)
#     input_latent1 = torch.randn((4, 50, 75))
#     torch.manual_seed(1)
#     input_latent2 = torch.randn((4, 50, 75))
#     noise_step_vector = (input_latent2 - input_latent1) / (num_frames - 1)
#     for i in range(num_frames):
#         output_latent = denoise_latent(input_latent1 + i * noise_step_vector, prompt=prompt1)
#         frame = decode_latent(output_latent)
#         frame.save(f"frames/frame{i}.jpg")

def generate_frames_new_prompt(prompt1, prompt2, prompt3, num_frames=4, diverge_step=10):
    torch.manual_seed(3)
    input_latent1 = torch.randn((4, 50, 75))
    output_latent1 = denoise_latent(input_latent1, prompt=prompt1, end_timestep_idx=diverge_step)
    output_latent2 = denoise_latent(output_latent1, prompt=prompt2, start_timestep_idx=diverge_step)
    output_latent3 = denoise_latent(output_latent1, prompt=prompt3, start_timestep_idx=diverge_step)
    frames = interpolate_latents(output_latent2, output_latent3, num_frames)
    return frames

# def generate_frames_edit(prompt1, prompt2):
#     torch.manual_seed(0)
#     input_latent1 = torch.randn((4, 50, 75))
#     embed, negative_embed = PIPE.encode_prompt(prompt2, args.device, 1, True)
#     output_latent1 = denoise_latent(input_latent1, embed=embed, end_timestep_idx=3)
#     t = PIPE.scheduler.timesteps[3]
#     u, s, vT = PIPE.unet.local_encoder_pullback_zt(
#         sample=torch.unsqueeze(output_latent1, axis=0), timestep=t, encoder_hidden_states=embed, op='mid', block_idx=0,
#         pca_rank=50, chunk_size=5, min_iter=10, max_iter=50, convergence_threshold=1e-4,
#     )


# Linear interpolation between latent from prompt and unguided latent conditioned on latent from prompt
def generate_frames_no_guidance(prompt, num_frames):
    pass

# Linear interpolation between latent from prompt1 and latent conditioned on prompt1, renoised, and guided by prompt2
def generate_frames_new_guidance(prompt1, prompt2, num_frames):
    pass

if __name__ == "__main__":
    print(torch.cuda.is_available())
    # prompt1 = "Jungle with vines. Majestic lighting. Hyper realism. Symmetric artwork. Cinematic. High detail. 8k. --ar 2:3"
    # prompt2 = "Underwater coral reef. Majestic lighting. Hyper realism. Symmetric artwork. Cinematic. High detail. 8k. --ar 2:3"
    # prompt1 = "Large man centered, symmetric, outline, silhouette"
    # prompt2 = "astronaught in a purple suit, futuristic."
    # prompt3 = "alien in a red suit, futuristic."
    prompt1 = "A headshot of a man, closeup, resting face, calm, simple background, cartoon art, colorful"
    prompt2 = "An extremely happy man, smile, eyes wide open"
    prompt3 = "An extremely sad man, frown, crying, tears"
    frames = generate_frames_new_prompt(prompt1, prompt2, prompt3, diverge_step=3)
    for i, frame in enumerate(frames):
        frame.save(f"./frames/frame{i}.jpg")
