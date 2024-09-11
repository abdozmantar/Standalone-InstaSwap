import gradio as gr
import os
import folder_paths
from scripts.instaswap_logger import logger
from scripts.instaswap_swapper import swap_face
from basicsr.utils.download_util import load_file_from_url

#-----------------------------------
# MODELS
#-----------------------------------
models_dir = folder_paths.models_dir
INSIGHTFACE_MODEL_PATH = os.path.join(models_dir,"insightface")


if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
#-----------------------------------
# APP
#-----------------------------------
logger.job("InstaSwap library up and running !")


def Swap(input_image, source_image):

    # Check Models
    modelName = "inswapper_128.onnx"     
    if not os.path.exists(INSIGHTFACE_MODEL_PATH + "inswapper_128.onnx"):
        logger.job("Face Swap model is downloading...")
        load_file_from_url(url="https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx", model_dir=INSIGHTFACE_MODEL_PATH, progress=True, file_name=None)
        
    # Swap
    result = swap_face(source_image,input_image,source_faces_index = [0],faces_index = [0],model=modelName, gender_source=0,gender_target=0,face_model=None)

    return result



icon_url = "https://github.com/abdozmantar/ComfyUI-InstaSwap/blob/main/Logo.png?raw=true"

with gr.Blocks() as app:
  
    gr.HTML(f"""
        <table style="width: 100%; height: 150px">
          <tr>
            <td style="display:flex;  flex-direction: column; align-items: center;">
                <img src="{icon_url}" style="width: 150px;">
                <h1 style="font-size: 22px;">InstaSwap Standalone Version</h1>
            </td>
          </tr>
      </table>
    """)

    with gr.Row(): 
        img_input1 = gr.Image(label="Input")
        img_input2 = gr.Image(label="Source")
        img_output = gr.Image(label="Result")
    with gr.Tab("Parameters"): 
        gr.Markdown("FaceSwapper Model : inswapper_128.onnx")
        btn = gr.Button("Swap Faces")
   

    btn.click(Swap, inputs=[img_input1, img_input2], outputs=img_output)

app.title = "InstaSwap Standalone"
app.launch(inbrowser=True)
