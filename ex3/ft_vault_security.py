def secure_archive(filename: str, stats: str, new_content: str) -> None:

    try:
        if stats == "r":
            with open(filename, "r") as file:
                content = file.read()

            return True, content

        elif stats == "w":
            with open("a.txt", "w") as file:
                file.write(new_content)

            return True, "Content successfully written to file"

    except OSError as e:
        return False, str(e)
    

if __name__ == "__main__":
    print(
        "=== Cyber Archives Security ===\n"

        "Using secure_archive to read from a nonexistent file:\n"
        f"{secure_archive("nonexistent", "r", "")}\n"
        "\nUsing secure_archive to read from an inaccessible file:\n"
        f"{secure_archive("inaccessible.txt", "r", "")}\n"
        "\nUsing secure_archive to read from a regular file:\n"
        f"{secure_archive("test1.txt", "r", "")}\n"
        "\nUsing secure_archive to write previous content to a new file:\n"
        f"{secure_archive("test1.txt", "w", "new")}\n"
    )
