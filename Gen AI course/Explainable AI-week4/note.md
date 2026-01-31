Python Environment::: (Can be replicated on any Programming language)

1. Write a python code for building a calculator with basic functions. (Use ChatGPT then save the file as calculator.py)
2. Run calculator.py
3. Open codex: echo $env:OPENAI_API_KEY | codex login --with-api-key
4. Prompts:
	a. Explain calculator.py to me. 
	b. Check any basic functionality of the calculator.
	c. Ask the LLM for any suggested improvements.
	d. Perform the suggested improvements.
	b. Ask it to make it an advanced calculator. (Try it yourself)
5. Add some errors intentionally and see if and how codex identifies the issue and resolves. (Try it yourself)



OpenAI Account and API Key Generation
--------------------------------------
1. Go to the OpenAI website: https://platform.openai.com/

2. Log in or sign up:

   > Click "Log in" if you already have an account.
   > Click "Sign up" to create a new account.

3. Navigate to the API Keys page:

   > Click your profile icon in the top-right corner.
   > Select "API Keys" from the dropdown menu.
   > Or go directly to: https://platform.openai.com/account/api-keys

4. Create a new key:

   > Click on the "+ Create new secret key" button.
   > Optionally, name the key to identify its purpose.

5. Copy the key immediately:

   > The secret key will be shown only once.
   > Copy it and save it securely.

Note: You have to load credits (we recommend at least $3) in your OpenAI account using a Debit/Credit card.


OpenAI CODEX
------------

1. Download NodeJS as per your OS: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

  > Windows (Install Executable): https://github.com/coreybutler/nvm-windows/releases/download/1.2.2/nvm-setup.exe
  > Linux    (Build from source): https://github.com/nodesource/distributions 

2. Install 'npm' using 'nvm': nvm install latest
3. Turn on 'nvm' to access 'npm': nvm on
4. Install Codex CLI using 'npm': npm i -g @openai/codex
5. Start codex using: codex
6. echo $env:OPENAI_API_KEY | codex login --with-api-key

Stable Diffusion
-----------------
Note: We recommend that you should have access to a CUDA GPU enabled system / cloud GPU compute platform.

> If you don't have access to GPU you can utilize the web-console provided by Stable Diffusion.

> If you have access to GPU: Install the packages and download models using the code below

PACKAGES:

pip install diffusers --upgrade
pip install invisible_watermark transformers accelerate safetensors

CODE:

    from diffusers import StableDiffusion3Pipeline
    from diffusers import DiffusionPipeline

    pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")





I suggest you reading the following books if you are interested to learn about LLMs:

1. Build a Large Language Model (From Scratch) by Sebastian Raschka
2. Foundations of Large Language Models by Tong Xiao and Jingbo Zhu 
3. Large Language Models: A Deep Dive (Springer)
4. Hands-On Large Language Models by Jay Alammar and Maarten Grootendorst (O'Reilly, 2024)
5. The Hundred-Page Language Models Book by Andriy Burkov
6. Large Language Models (MIT Press)



