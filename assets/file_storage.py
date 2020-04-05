import cloudinary
from cloudinary.uploader import upload
from config import asset
from  utilities import constant

class file_manager:
    def __init__(self,storage_type):
        if storage_type is None:
            self.storage_type = constant.STORAGE_TYPE_CLOUDINARY
        else:
            self.storage_type = storage_type

    def load_config(self):
        if  self.storage_type == constant.STORAGE_TYPE_CLOUDINARY
            config = asset.AssetConfiguration(None)
            cloud_name = config.cloud_name
            api_key = config.api_key
            api_secret = config.api_secret
            cloudinary.config(cloud_name = cloud_name, api_key = api_key, api_secret = api_secret)
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass
    
    def upload_file(self,file_name, custom_name=None):
        if  self.storage_type == constant.STORAGE_TYPE_CLOUDINARY
            if custom_name is None:
                return file_info = upload(file_name)            
            else:
                return file_info = upload(file_name, public_id = custom_name)
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass:
            