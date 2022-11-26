from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.table import Table 
# from rich.markdown import Markdown 
# from time import sleep
from rich.progress import track
from rich import box
# from rich.layout import Layout
# from rich.progress import Progress
from rich.panel import Panel

# console


theme = Theme({
    "success": "green italic",
    "error": "red italic bold",
    "warning": "white on yellow italic",
    "normal": "cyan italic bold"
})

console = Console(theme=theme)

def output(text, mode="normal"):
    text = Text(text)
    text.stylize(mode)
    # text.highlight_words()
    console.print(text)

def print_json(input):
    console.print_json(data=input)

def print_table_all(data, title):
    if data != []:
        table = Table(title="grades" + " | " + title, box=box.SIMPLE, header_style="bold blue", title_justify="center", title_style="bold red underline")
        table.add_column("title", style="cyan bold")
        table.add_column("subject",style="yellow")
        table.add_column("marks",style="purple bold")
        table.add_column("category",style="red")
        table.add_column("created at",style="green")
        table.add_column("updated at",style="magenta")
        table.add_column("ID", style="blue")

        # rows
        # for record in data:
        #     table.add_row(*record)

        for rec in data:
            table.add_row(
            rec["title"],
            rec["subject"],
            f"{rec['value']}/{rec['max_value']}",
            rec["category"],
            rec["createdAt"],
            rec["updatedAt"],
            rec["_id"] 
            )

        console.print(table)
    else:
        console.print("no rec found", style="warning")

def print_rec(data, message):
    if data != []:
        prstr = ''
        for field, value in data.items():
            if field not in ['user', '__v', '_id']:
                prstr += f"[bold light_blue]{field.capitalize()}[/] : {value} \n"
        panel = Panel(prstr, title=f"[bold green]{message}[/]{data['user']}", subtitle=data["_id"])
        console.print(panel, justify="center")
    else:
        console.print("No rec Found", style="warning")



def print_user(data):
    if data != []:
        prstr = ''
        for field, value in data.items():
            if field not in ['__v', '_id', "records"]:
                prstr += f"[bold green]{field.capitalize()}[/] : {value} \n"
            
        panel = Panel(prstr, title=f"[bold purple]Rec by[/] [underline green italic]{data['username']}[/]", subtitle=data["_id"])
        console.print(panel, justify="center")
        panel2 = Panel(f"[bold yellow]No of rec:[/] {len(data['records'])}")
        console.print(panel2, justify="center")
        # print_table_all(data["records"], "user rec")
    else:
        console.print("No user found", style="warning", justify="center")









        







# with console.status("Working...", spinner="aesthetic"):
# with Progress() as progress:
#     task1 = progress.add_task("[blue]Working...", total=100)
#     while not progress.finished:
#         progress.update(task1, advance=10)
#         print("hello world")
#         sleep(1.5)
#     # for i in track(range(20), description="working..."):
#     #     print("hello world" + str(i))
#     #     sleep(1)