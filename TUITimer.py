# ======================================================================
# TODO List and Features
# ======================================================================
# TODO: Create a graphical TUI display
# TODO: Add buttons for start/stop/reset
# TODO: Take an input for the amount of time.
# TODO: Play a notification sound
# TODO: Push a notification to the screen with the notification daemon.
# ======================================================================
from textual.app import App,  ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Button, Digits, Footer, Header

class TimeDisplay(Digits):
    """extends digits"""

class Stopwatch(HorizontalGroup):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id =="stop":
            self.remove_class("started")
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")

class StopwatchApp(App):
    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        #Create header for the app
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
