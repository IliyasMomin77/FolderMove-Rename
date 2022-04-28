import shutil
from datetime import datetime
import os

today = datetime.now()
x='AWS-Data_'
source_dir = r"D:\AWS"
destination_dir = r"C:\Users\Iliyas\OneDrive\Documents\_" + (x) + today.strftime('%Y%m%d_%H_%M_%S')
shutil.copytree(source_dir, destination_dir)

