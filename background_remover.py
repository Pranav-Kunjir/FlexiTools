
import os
folder = "./tools_code/uploads/background-remover/"
layer_file = "layer-1.png"
def backgroundremoval(input_file, output_file):
    os.system(f"backgroundremover -i {input_file} -o {folder}{layer_file}")
    os.system(f"backgroundremover -i {folder}{layer_file} -o {folder}{output_file}")
def delete_cache_file(folder):
    os.system(f"rm -v {folder}*")






