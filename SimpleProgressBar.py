from os import get_terminal_size


class ProgressBar:
    def __init__(
        self,
        total: int,
        name: str,
        bar_str: str = "%",
        percent_256color: int = 15,
        bar_256color: int = 15,
        # 256-color: https://www.ditig.com/publications/256-colors-cheat-sheet
        background_filling_mode: bool = False,
    ) -> None:
        self.total = total
        self.name = name
        self.bar_str = bar_str
        self.percent_256color = percent_256color
        self.bar_256color = bar_256color
        self.n_length = len(name)
        self.now = 0
        self.width = get_terminal_size().columns
        self.background_filling_mode = background_filling_mode
        if background_filling_mode:
            self.bar_str = " "

    def update(self, new: int) -> None:
        self.now = new
        self.show()

    def show(self):
        bar_size = self.width - 9
        percentage = round(self.now / self.total * 100, 1)
        if percentage < 10:
            percentage = "  " + str(percentage)
        elif percentage < 100:
            percentage = " " + str(percentage)
        filled_bar = round(self.now / self.total * bar_size)
        if self.background_filling_mode:
            bar_size += 2
            filled_bar = round(self.now / self.total * bar_size)
            bar = (
                f"\033[48;5;{self.bar_256color}m"
                + filled_bar * self.bar_str
                + "\033[0m"
                + " " * (bar_size - filled_bar)
            )
            final = f"\033[38;5;{self.percent_256color}m{percentage}% \033[0m{bar}"
        else:
            bar = (
                f"\033[38;5;{self.bar_256color}m"
                + filled_bar * self.bar_str
                + " " * (bar_size - filled_bar)
                + "\033[0m"
            )
            final = f"\033[38;5;{self.percent_256color}m{percentage}% \033[0m[{bar}]"
        print(final, end="\r")
        if self.now == self.total:
            print(f"{self.name} Complete!" + " " * (self.width - 10 - self.n_length))
