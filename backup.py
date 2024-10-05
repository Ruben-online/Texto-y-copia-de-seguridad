def create_backup(source_file = "Test_dividido.txt", backup_file="Copy.txt"):
    with open(source_file, "r", encoding="utf-8") as original_file:
        with open(backup_file, "w", encoding="utf-8") as backup:
            backup.write(original_file.read())

    print(f"Copia de seguridad creada en '{backup_file}'")