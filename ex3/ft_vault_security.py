def secure_archive(
        filename: str,
        action: str | None = None,
        new_content: str | None = None,
        ) -> tuple[bool, str]:
    if action == 'w':
        if new_content is not None:
            try:
                with open(filename, 'w') as file:
                    file.write(new_content)
                return True, 'Content successfully written to file'

            except IOError as e:
                return (False, str(e))

        return (False, "Nothing turned in as the new content")

    else:
        try:
            with open(filename, 'r') as file:
                content = file.read()
            return True, content

        except OSError as e:
            return (False, str(e))


if __name__ == "__main__":
    print(
        "=== Cyber Archives Security ===\n\n"

        "Using 'secure_archive' to read from a nonexistent file:\n"
        f"{secure_archive('nonexistent')}\n"
        "\nUsing 'secure_archive' to read from an inaccessible file:\n"
        f"{secure_archive('inaccessible.txt')}\n"
        "\nUsing 'secure_archive' to read from a regular file:\n"
        f"{secure_archive('test1.txt', 'r')}\n"
        "\nUsing 'secure_archive' to write previous content to a new file:\n"
        f"{secure_archive('test1.txt', 'w', 'new')}\n"
    )
