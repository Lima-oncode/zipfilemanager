import zipfile
import py7zr
import os

class ZipFileManager:
    def __init__(self, sys_path, end_path):
        self.sys_path = sys_path
        self.end_path = end_path
        
    def extract_zip_files(self):
        if os.path.isdir(self.sys_path):
            list_sys = [file for file in os.listdir(self.sys_path) if file.endswith(".zip") or file.endswith(".7z")]
            print(f"Arquivos encontrados no diretório de origem: {list_sys}")
            
            for file in list_sys:
                zip_file_path = os.path.join(self.sys_path, file)
                zip_file_path = os.path.normpath(zip_file_path)

                print(zip_file_path)

                folder_name = os.path.splitext(file)[0]
                extract_path = os.path.join(self.end_path, folder_name)
                os.makedirs(extract_path, exist_ok=True)

                try:
                    if zip_file_path.endswith(".zip"):
                        with zipfile.ZipFile(file=zip_file_path, mode="r") as zip_obj:
                            zip_obj.extractall(extract_path)
                            print(f"Arquivo ZIP '{file}' extraído para {self.end_path}")
                    elif zip_file_path.endswith(".7z"):
                        with py7zr.SevenZipFile(file=zip_file_path, mode="r") as sevenz_obj:
                            sevenz_obj.extractall(extract_path)
                            print(f"Arquivo 7z '{file}' extraído para {extract_path}")
                except zipfile.BadZipFile:
                    print(f"O arquivo '{file}' não é um ZIP válido.")
                except py7zr.Bad7zFile:
                    print(f"O arquivo '{file}' não é um 7z válido.")
                except Exception as e:
                    print(f"Erro inesperado ao processar '{file}': {e}")
                
                os.remove(zip_file_path)

    
    def rename_files(self):
        list_extract_dir = os.listdir(self.end_path)
        
        for file in list_extract_dir:
            if file.endswith(".EMPRECSV"):
                old_path = os.path.join(self.end_path, file)
                new_path = os.path.join(self.end_path, file.replace(".EMPRECSV", ".csv"))
                
                os.replace(old_path, new_path)
                print(f"Renomeou o arquivo {file} para {new_path}")

# Exemplo de uso da classe ZipFileManager -> Instanciando metodos
sys_path = "D:/JOGOS/PCSX2/PS2 ISO"
end_path = "D:/JOGOS/PCSX2/PS2 ISO"



zip_manager = ZipFileManager(sys_path, end_path)
zip_manager.extract_zip_files()
# zip_manager.rename_files()
