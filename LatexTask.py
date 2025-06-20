from pathlib import Path
from subprocess import run

def make_pdf(txt,stem):
    template=r"""
\documentclass{article}
\usepackage[a4paper,portrait, margin=2cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[export]{adjustbox}
%\usepackage{lmodern}
%\usepackage{textcomp}
%\usepackage{lastpage}
%\usepackage{geometry}
%\geometry{tmargin=1cm,lmargin=10cm}
\usepackage{amsmath}
%\usepackage{tikz}
%\usepackage{pgfplots}
%\pgfplotsset{compat=newest}
\usepackage{graphicx}
\begin{document}"""

    template_end=r"""
\end{document}"""
    latex_file=f"{stem}.tex"
    with Path(latex_file).open("w") as f:
        f.write(
            template+
            txt+
            template_end
        )
    args=["pdflatex",f"{latex_file}"]
    res=run(args)
    return res
