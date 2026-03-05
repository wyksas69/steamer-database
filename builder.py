import os
import json
import re

def build_database():
    database = {}
    root_dir = os.getcwd()
    
    print(f"[*] Скрипт запущен в: {root_dir}")
    items = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
    print(f"[*] Вижу папок: {len(items)}")

    for folder_name in items:
        folder_path = os.path.join(root_dir, folder_name)
        
        if folder_name.startswith('.'): continue
            
        found_id = None
        try:
            files = os.listdir(folder_path)
            for file_name in files:
                # ТЕПЕРЬ ИЩЕМ .manifest
                if file_name.lower().endswith(".manifest"):
                    # Выцепляем цифры из названия (например, из 271590.manifest)
                    match = re.search(r'\d+', file_name)
                    if match:
                        found_id = match.group()
                        break
        except Exception as e:
            print(f"[!] Ошибка в папке {folder_name}: {e}")

        if found_id:
            database[found_id] = folder_name
            if len(database) % 100 == 0:
                print(f"[+] Собрано игр: {len(database)}...")

    if not database:
        print("[!] ОШИБКА: Файлы .manifest не найдены!")
        return

    output_file = "ids_path.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(database, f, ensure_ascii=False, indent=4)
        
    print(f"\n[!] ПОБЕДА! Создан файл: {output_file}")
    print(f"[!] Итого в базе: {len(database)} игр.")

if __name__ == "__main__":
    build_database()
    input("\nНажми Enter, чтобы выйти...")
