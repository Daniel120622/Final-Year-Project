class Parameter:
    def __init__(self, height=512, width=512, num_inference=20, seed=-1, guidance_scale=7.5, batch_size=1,
                 sampler="DDPM", VAE = None, preprocessor = "OpenPose", model = "runwayml/stable-diffusion-v1-5"):
        self.height = height  # default height of Stable Diffusion
        self.width = width  # default width of Stable Diffusion
        self.num_inference = num_inference  # Number of denoising steps
        self.guidance_scale = guidance_scale  # Scale for classifier-free guidance
        self.seed = seed
        self.batch_size = batch_size

        self.sampler = sampler
        self.Vae = VAE
        self.preprocessor = preprocessor
        self.model = model

def printParameter():
    print(CurrentParameter.sampler, CurrentParameter.Vae, CurrentParameter.preprocessor,
          CurrentParameter.height, CurrentParameter.width, CurrentParameter.seed, CurrentParameter.batch_size,CurrentParameter.guidance_scale, CurrentParameter.num_inference)

HumanParameter = Parameter()
HumanParameter.height = 768
HumanParameter.num_inference = 25
HumanParameter.model = "chilloutmix"

Default = Parameter()
ClothParameter = Parameter(512, 512, 35, -1, 7.5, 1)
CurrentParameter = Default

def giveFeedback(feedback):
    if feedback == "sampler":
        print("Suggest sampler to become....")
        Sampler_feedback(input("Which one would you like to change? \n"))
    elif feedback == "step":
        print("Suggest step to become.... ")
        Step_feedback(input("Which one would you like to choose?\n"))
    elif feedback == "VAe":
        print("Suggest VAE to become...")
        VAE_feedback(input("Which one would you like to choose?\n"))
    elif feedback == "preprocessor":
        print("Suggest Preprocessor to become")
        Preprocessor_feedback(input("Which one would you like to choose?\n"))
    elif feedback == "model":
        print("Suggest Model to become...")
        Model_feedback(input("Which one would you like to choose?\n"))
    elif feedback == "guidance scale":
        print("Suggest guidance scale to become ....")
        guidance_scale_feedback(input("Which one would you like to choose?\n"))
    elif feedback == "Change Parameter":
        parameter_feedback(input("Which parameter you want to select..."))
    else:
        print("Wrong input. Return to the main index")


def parameter_feedback(parameter):
    if parameter == "Human" or parameter == "human":
        CurrentParameter = HumanParameter
        printParameter()
    elif parameter == "Cloth" or parameter == "cloth":
        CurrentParameter = ClothParameter
        printParameter()

def Sampler_feedback(Sampler):
    CurrentParameter.sampler = Sampler
    print(CurrentParameter.sampler,CurrentParameter.Vae, CurrentParameter.preprocessor,
          CurrentParameter.height,CurrentParameter.width,CurrentParameter.seed,CurrentParameter.batch_size,CurrentParameter.guidance_scale,CurrentParameter.num_inference)
    # It is better to use DPM++ 2M / DPM++2M Karras or UniPC
    # If we want to get some surprise and changes, we can use DPM++ SDE、DPM++ SDE Karras、DPM2 a Karras.
def Step_feedback(Step):
    CurrentParameter.num_inference = Step
    print(CurrentParameter.sampler, CurrentParameter.Vae, CurrentParameter.preprocessor,
          CurrentParameter.height, CurrentParameter.width, CurrentParameter.seed, CurrentParameter.batch_size,
          CurrentParameter.guidance_scale, CurrentParameter.num_inference)
def VAE_feedback(VAE):
    CurrentParameter.Vae = VAE
    printParameter()
def Preprocessor_feedback(Preprocessor):
    CurrentParameter.preprocessor = Preprocessor
    printParameter()
def Model_feedback(Model):
    CurrentParameter.model = Model
    printParameter()
def guidance_scale_feedback(Guidance_scale):
    CurrentParameter.guidance_scale = Guidance_scale
    printParameter()

