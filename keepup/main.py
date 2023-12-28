import config.log_config as log_config
from summarizer import Summarizer
import typer

logger = log_config.logger("main")
app = typer.Typer()


@app.command()
def summarize(text: str = None, min_length: int = 30, max_length: int = 200, read_from: str = None,
              write_to: str = None):
    if text and read_from:
        print("Cannot specify both text and file input.")
        raise typer.Exit(code=1)

    if not text and not read_from:
        print("You must either provide the text the summarize as a command line argument or a file.")
        raise typer.Exit(code=1)

    summarizer = Summarizer()

    if read_from:
        with open(read_from) as input_file:
            to_summarize = '\n'.join(input_file.readlines())
    else:
        to_summarize = text

    result = summarizer.summarize(to_summarize, min_length=min_length, max_length=max_length)

    if write_to:
        with open(write_to, mode="w") as out:
            out.write(result)
    else:
        print(result)


if __name__ == "__main__":
    typer.run(summarize)
