"""High-level utilities to display markdown."""

import pandas as pd

from IPython.display import display, HTML, Markdown
from IPython.core.getipython import get_ipython


class Renderer:
    """
    Wrapper over IPython.display to easily write user-friendly Markdown documentation.
    If IPython is not available, the markdown text is printed in the console.

    Example:
    ```
        r = Renderer()
        r.h1("Some square roots")
        for x in range(1, 4):
            r.h2("number", x)
            r.text("The square root of", x, ",", r.math(f"\\sqrt{{{x}}}"), "is", math.sqrt(x))
        r.end_paragraph()
    ```
    """

    def __init__(self, use_ipython=None):
        """
        Args
            use_ipython (bool or None): whether to use the IPython display.
                If None (default), automatically detect whether IPython is available.
        """
        self.use_ipython = use_ipython
        if use_ipython is None:
            self.use_ipython = self._detect_ipython()
        # The renderer also has internal state to adapt renders.
        self._itemize = False  # Whether currently in an enumeration.

    def _detect_ipython(self):
        """Infers whether an IPython display is available."""
        try:
            get_ipython()
            return True
        except AttributeError:
            return False

    # Basic interface: rendering types of data.

    def text(self, *text: str, end: str = "", item: bool = False):
        """
        Renders Markdown text.

        Args:
            *text (str): the text to display, joined by a single whitespace.
            end (str, optional): a character to add at the end of the text.
            item (bool, optional): if True, this text is rendered as part of an enumeration.
        """
        text = " ".join([str(t) for t in text]) + end
        # Correct a common mistake: " ." --> "."
        if text.endswith(" ."):
            text = text[:-2] + "."
        # Add an enumeration symbol
        if item:
            text = " - " + text
        # Add a newline if starting or ending an enumeration.
        if item != self._itemize:
            self._itemize = item
            text = "\n" + text
        if self.use_ipython:
            display(Markdown(text))
        else:
            print(text)

    def dataframe(self, df: pd.DataFrame):
        """
        Renders a pandas DataFrame.

        Args:
            df (pd.DataFrame): the dataframe whose content should be displayed.
        """
        if self.use_ipython:
            display(HTML(df.to_html(index=False)))
        else:
            print(df)

    # High-level interface: methods with short names.

    def ln(self, *text, end=""):
        """Renders text with a linereturn."""
        self.text(*text, end=end + "\n")

    def h1(self, *text):
        """Renders a topmost title."""
        self.ln("#", *text)

    def h2(self, *text):
        """Renders a title."""
        self.ln("##", *text)

    def h3(self, *text):
        """Renders a subtitle."""
        self.ln("###", *text)

    def h4(self, *text):
        """Renders a subsubtitle."""
        self.ln("####", *text)

    def df(self, df):
        """Renders a pandas DataFrame."""
        self.dataframe(df)

    def __call__(self, *text, end=""):
        """Renders text with a line return (like self.ln)."""
        self.ln(*text, end=end)

    def item(self, *text):
        """Renders an item in an enumeration."""
        self.text(*text, item=True)

    def end_paragraph(self):
        """Ends the current paragraph with a line break."""
        if self.use_ipython:
            self.text("<br>")
        else:
            self.text("\n\n")

    # Sub-utilities that do not render, but format before rendering.

    def code(self, text: str):
        """Formats text as code."""
        return f"`{text}`"

    def code_block(self, text: str, lang=""):
        """Formats text as a code block."""
        return f"```{lang}\n{text}```"

    def math(self, text):
        """Formats text as a math entry."""
        return f"${text}$"

    def it(self, text: str):
        """Formats text as italics."""
        return f"*{text}*"

    def bf(self, text: str):
        """Formats text as boldface."""
        return f"**{text}**"
