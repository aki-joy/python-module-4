import sys
import typing


def read_file(args: list[str]) -> str:

    if len(args) < 2:
        return print("Usage: ft_ancient_text.py <file>")

    filename = args[1]
    file: typing.IO[str]
    print(f"Accessing file {filename}")

    try:
        file = open(filename, "r")
        content = file.read()

        print(f"---\n\n{content}\n\n---")

        file.close()

        print(f"File {filename} closed.\n")
        return content

    except OSError as e:
        sys.stderr.write(f"[STDERR]  Error opening file: {filename}: {e}")


def write_file(content: str) -> None:

    lines = content.splitlines()
    new_content = ""
    for line in lines:
        new_content += line + "#\n"

    print(f"Transform data\n---\n\n{new_content}\n---")

    new_filename = get_new_file()
    if new_filename == "":
        return print("Not saving data.")
    try:
        file = open(new_filename, "w")
        print(f"Saving data to {new_filename}")
        file.write(new_content)
        print(f"Data saved in file {new_filename}")
        file.close()

    except Exception as e:
        sys.stderr.write(f"[STDERR]  Error opening file: {new_filename}: {e}")


def get_new_file() -> str:

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().rstrip("\n")

    return new_filename 


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    content = read_file(sys.argv)

    if content:
        write_file(content)
