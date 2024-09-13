import zipfile
import os

class ZipFileManager:
    def __init__(self, sys_path, end_path):
        self.sys_path = sys_path
        self.end_path = end_path
        
    def extract_zip_files(self):
        if os.path.isdir(self.sys_path):
            list_sys = os.listdir(self.sys_path)
            print(f"Arquivos encontrados no diretório de origem: {list_sys}")
            
            for file in list_sys:
                if file.endswith(".zip"):
                    zip_file_path = os.path.join(self.sys_path, file)
                    
                    with zipfile.ZipFile(file=zip_file_path, mode="r") as zip_obj:
                        zip_obj.extractall(self.end_path)
                        print(f"Extraiu o arquivo {file} no diretório {self.end_path}")
    
    def rename_files(self):
        list_extract_dir = os.listdir(self.end_path)
        
        for file in list_extract_dir:
            if file.endswith(".EMPRECSV"):
                old_path = os.path.join(self.end_path, file)
                new_path = os.path.join(self.end_path, file.replace(".EMPRECSV", ".csv"))
                
                os.replace(old_path, new_path)
                print(f"Renomeou o arquivo {file} para {new_path}")

# Exemplo de uso da classe ZipFileManager -> Instanciando metodos
sys_path = "F:/mycodes/zipfilemanager/zips"
end_path = "F:/mycodes/zipfilemanager/extracts"

zip_manager = ZipFileManager(sys_path, end_path)
zip_manager.extract_zip_files()
zip_manager.rename_files()
