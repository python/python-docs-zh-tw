import os
import google.generativeai as genai

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Static
from textual.containers import Container
from textual.binding import Binding
import polib
from pathlib import Path
import subprocess

class TranslationApp(App):
    BINDINGS = [
        Binding("left", "previous", "Previous Entry"),
        Binding("right", "next", "Next Entry"),
        Binding("enter", "accept", "Accept Translation"),
        Binding("ctrl+s", "save", "Save Changes"),
        Binding("ctrl+g", "generate", "Generate Translation"),
    ]
    CSS = """
    #status-container {
        height: auto;
        padding: 1;
        background: $accent-darken-2;
        color: $text;
        text-align: center;
        text-style: bold;
    }

    #status-line {
        text-style: bold;
    }

    #translation-container {
        layout: grid;
        grid-size: 4;
        grid-columns: 1fr;
        padding: 1;
    }
    
    .section-label {
        text-align: center;
        background: $accent;
        color: $text;
        padding: 1;
        border: solid $background;
    }

    .text-content {
        background: $surface;
        color: $text;
        padding: 1;
        border: solid $background;
        height: auto;
        min-height: 5;
        max-height: 100;
        overflow-y: auto;
    }

    .translation-input {
        width: 100%;
        min-height: 5;
        height: auto;
    }

    #button-container {
        layout: horizontal;
        height: auto;
        align: center middle;
        padding: 1;
    }
    """

    def __init__(self, po_file_path: Path):
        super().__init__()
        self.po_file_path = po_file_path
        self.po_file = polib.pofile(str(po_file_path))
        # Preserve original wrapping format
        self.po_file.wrapwidth = 0  # Disable wrapping to maintain original format
        self.current_entry_index = 0

        
    @staticmethod
    def translate_text(prompt: str) -> str:
        import textwrap
        genai.configure(api_key=os.getenv('GEMINI_API'))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        # Wrap text at 72 characters, which is a common standard for PO files
        wrapped_text = textwrap.fill(response.text, width=72)
        return wrapped_text

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static(id="status-line"),
            id="status-container"
        )
        yield Container(
            Static("Source Text", classes="section-label"),
            Static(id="source-text", classes="text-content"),
            Static("Raw Translation", classes="section-label"),
            Static(id="raw-translation", classes="text-content"),
            Static("New Translation", classes="section-label"),
            Input(classes="translation-input", id="translation-input"),
            Container(
                Button("Previous [←]", id="prev-btn"),
                Button("Accept [↵]", id="accept-btn"),
                Button("Next [→]", id="next-btn"),
                Button("Generate [^G]", id="generate-btn"),
                Button("Save [^S]", id="save-btn", variant="primary"),
                id="button-container"
            ),
            id="translation-container"
        )
        yield Footer()

    def on_mount(self) -> None:
        self.show_current_entry()

    def show_current_entry(self) -> None:
        if self.current_entry_index < len(self.po_file):
            entry = self.po_file[self.current_entry_index]
            status = f"File: {self.po_file_path.name} | Entry: {self.current_entry_index + 1}/{len(self.po_file)}"
            self.query_one("#status-line").update(status)
            self.query_one("#source-text").update(entry.msgid)
            self.query_one("#raw-translation").update(entry.msgstr)
            
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "accept-btn":
            translation = self.query_one("#translation-input").value
            if translation:
                self.po_file[self.current_entry_index].msgstr = translation
                self.navigate_entry(1)
        elif event.button.id == "next-btn":
            self.navigate_entry(1)
        elif event.button.id == "prev-btn":
            self.navigate_entry(-1)
        elif event.button.id == "generate-btn":
            entry = self.po_file[self.current_entry_index]
            try:
                prompt = ("Translate the following Python documentation into Traditional Chinese"
                f"for {self.po_file_path}:{entry.occurrences} with message {entry.msgid}. Ensure "
                "that the translation is accurate and uses appropriate technical terminology. The"
                " output must be in Traditional Chinese. Pay careful attention to context, idiomatic"
                " expressions, and any specialized vocabulary related to Python programming. Maintain "
                "the structure and format of the original documentation as much as possible to ensure"
                " clarity and usability for readers.")
                translation = self.translate_text(prompt)
                if translation:
                    self.query_one("#translation-input").value = translation
                    self.notify("Translation generated!")
                else:
                    self.notify("Failed to generate translation", severity="error")
            except Exception as e:
                self.notify(f"Error: {str(e)}", severity="error")
        elif event.button.id == "save-btn":
            self.po_file.save(str(self.po_file_path))
            try:
                subprocess.run(['powrap', str(self.po_file_path)], check=True)
                self.notify("Changes saved and wrapped successfully!")
            except subprocess.CalledProcessError:
                self.notify("Save successful, but powrap failed!", severity="error")
            except FileNotFoundError:
                self.notify("Save successful, but powrap not found!", severity="warning")

    def navigate_entry(self, direction: int) -> None:
        new_index = self.current_entry_index + direction
        if 0 <= new_index < len(self.po_file):
            self.current_entry_index = new_index
            self.show_current_entry()
            self.query_one("#translation-input").value = ""

    def action_previous(self) -> None:
        self.navigate_entry(-1)

    def action_next(self) -> None:
        self.navigate_entry(1)

    def action_accept(self) -> None:
        translation = self.query_one("#translation-input").value
        if translation:
            self.po_file[self.current_entry_index].msgstr = translation
            self.navigate_entry(1)

    def action_save(self) -> None:
        self.po_file.save(str(self.po_file_path))
        try:
            subprocess.run(['powrap', str(self.po_file_path)], check=True)
            self.notify("Changes saved and wrapped successfully!")
        except subprocess.CalledProcessError:
            self.notify("Save successful, but powrap failed!", severity="error")
        except FileNotFoundError:
            self.notify("Save successful, but powrap not found!", severity="warning")
            
    def action_generate(self) -> None:
        entry = self.po_file[self.current_entry_index]
        try:
            prompt = ("Translate the following Python documentation into Traditional Chinese"
                f"for {self.po_file_path}:{entry.occurrences} with message {entry.msgid[1]}. Ensure "
                "that the translation is accurate and uses appropriate technical terminology. The"
                " output must be in Traditional Chinese. Pay careful attention to context, idiomatic"
                " expressions, and any specialized vocabulary related to Python programming. Maintain "
                "the structure and format of the original documentation as much as possible to ensure"
                " clarity and usability for readers.")
            translation = self.translate_text(prompt)
            if translation:
                self.query_one("#translation-input").value = translation
                self.notify("Translation generated!")
            else:
                self.notify("Failed to generate translation", severity="error")
        except Exception as e:
            self.notify(f"Error: {str(e)}", severity="error")

def main(po_file_path: str):
    app = TranslationApp(Path(po_file_path))
    app.run()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a PO file path")
