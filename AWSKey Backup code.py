import shutil
from datetime import datetime
import os

today = datetime.now()
x='AWS-Keys_'
source_dir = r"D:\AWS\Keys"
destination_dir = r"C:\Users\Iliyas\OneDrive\Documents\_" + (x) + today.strftime('%Y%m%d_%H_%M_%S')
shutil.copytree(source_dir, destination_dir)

