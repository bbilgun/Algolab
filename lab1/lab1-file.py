def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Файлын агуулга:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"Алдаа: '{file_path}' файл олдсонгүй.")
    
    except PermissionError:
        print(f"Алдаа: '{file_path}' файлыг унших зөвшөөрөл алга.")
    
    except IsADirectoryError:
        print(f"Алдаа: '{file_path}' файл биш, хавтас байна.")
    
    except Exception as e:
        print(f"Тодорхойгүй алдаа: {e}")

file_path = "example.txt"
read_file(file_path)
