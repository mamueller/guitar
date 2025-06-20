import matplotlib.pyplot as plt
from functools import reduce
from testinfrastructure.InDirTest import InDirTest
from guitar import Neck
from LatexTask import make_pdf


class Test(InDirTest):
    def setUp(self):
        self.neck=Neck(
            x_maxs=[-5,-3,-1,+1,3,5],
            x_maxs_neck=[-5.5,5.5],
            sf=0.75,
            #y_range=(0,64),
            y_range=(0,100),
            #build a coordinate transformation that flips the neck around
            transform=lambda x,y: (-y,x)
        )


    def test_C_Major_scale_on_low_E(self):
        fig=plt.figure(figsize=(14,4))
        ax=fig.subplots(1,1)
        ax.set_aspect(1)
        ax.set_axis_off()
        
        n=self.neck
        n.plot_neck(ax)
        
        # plot C-major scale
        n.plot_single_string_scale(
            ax,
            mi=[0,2,2,1,2,2,2,1],
            names=["C","D","E","F","G","A","B","C"],
            sp=8, # 8.th fret
            st=5, # low e
            label="C-major (C-Dur)",
            color="red",
            alpha=0.5,
        )
        ax.legend()
        fig.tight_layout()
        fig.savefig("plot.pdf")

    def test_all_Cs(self):
        n=self.neck
        fig=plt.figure(figsize=(20,3))
        ax=fig.subplots(1,1)
        ax.set_aspect(1)
        ax.set_axis_off()
        n.plot_neck(ax)
        fig.tight_layout()
        fig.savefig("plot_0.pdf")#, bbox_inches='tight')

        fig=plt.figure(figsize=(20,3))
        ax=fig.subplots(1,1)
        ax.set_aspect(1)
        ax.set_axis_off()
        n.plot_neck(ax)
        
        cs={    
            (5,8)  : "c'",
            (4,3)  : "c'",
            (3,10) : "c''",
            (2,5)  : "c''",
            (1,1)  : "c''",
            (0,8)  : "c'''"
        }
        
        for (st,f),label in cs.items():
            #st,f=combi
            n.plot_note(ax=ax,f=f,st=st,txt=label,color="red")
        ax.legend()
        fig.tight_layout()
        fig.savefig("plot_1.pdf")


        ##################################### 
        n=self.neck

        fig=plt.figure(figsize=(20,3))
        ax=fig.subplots(1,1)
        ax.set_aspect(1)
        ax.set_axis_off()
        n.plot_neck(ax)
        
        cs={    
            (5,0)  : "e",
            (5,1)  : "f",
            (5,3)  : "g",
            (5,5)  : "a",
            (5,7)  : "h",
            (5,8)  : "c'",
            (5,10)  : "d",
            (5,12)  : "e",
            (5,13)  : "f",
            (5,15)  : "g",
            (5,17)  : "a",
            (5,19)  : "h",
            (5,20)  : "c''",
            (5,22)  : "d",
            (5,24)  : "e",

            (4,0)  : "a",
            (4,2)  : "h",
            (4,3)  : "c'",
            (4,5)  : "d",
            (4,7)  : "e",
            (4,8)  : "f",
            (4,10)  : "g",
            (4,12)  : "a",
            (4,14)  : "h",
            (4,15)  : "c''",
            (4,17)  : "d",
            (4,19)  : "e",
            (4,20)  : "f",
            (4,22)  : "g",
            (4,24)  : "a",

            (3,0) : "d",
            (3,2) : "e",
            (3,3) : "f",
            (3,5) : "g",
            (3,7) : "a",
            (3,9) : "h",
            (3,10) : "c''",
            (3,12) : "d",
            (3,14) : "e",
            (3,15) : "f",
            (3,17) : "g",
            (3,19) : "a",
            (3,21) : "h",
            (3,22) : "c",
            (3,24) : "d",

            (2,0)  : "g",
            (2,2)  : "a",
            (2,4)  : "h",
            (2,5)  : "c''",
            (2,7)  : "d",
            (2,9)  : "e",
            (2,10)  : "f",
            (2,12)  : "g",
            (2,14)  : "a",
            (2,16)  : "h",
            (2,17)  : "c''",
            (2,19)  : "d",
            (2,21)  : "e",
            (2,22)  : "f",
            (2,24)  : "g",

            (1,0)  : "h",
            (1,1)  : "c''",
            (1,3)  : "d",
            (1,5)  : "e",
            (1,6)  : "f",
            (1,8)  : "g",
            (1,10)  : "a",
            (1,12)  : "h",
            (1,13)  : "c''",
            (1,15)  : "d",
            (1,17)  : "e",
            (1,18)  : "f",
            (1,20)  : "g",
            (1,22)  : "a",
            (1,24)  : "h",

            (0,0)  : "e",
            (0,1)  : "f",
            (0,3)  : "g",
            (0,5)  : "a",
            (0,7)  : "h",
            (0,8)  : "c'''",
            (0,10)  : "d",
            (0,12)  : "e",
            (0,13)  : "f",
            (0,15)  : "g",
            (0,17)  : "a",
            (0,19)  : "h",
            (0,20)  : "c'''",
            (0,22)  : "d",
            (0,24)  : "e",

        }
        
        for (st,f),label in cs.items():
            #st,f=combi
            n.plot_note(ax=ax,f=f,st=st,txt=label,color="red")
        ax.legend()
        fig.tight_layout()
        fig.savefig("plot_2.pdf")


        txt=r"""
\section*{Task}
\begin{flushleft}
The figure shows one note $C$ on every string.
Draw all the notes of the C-Major scale on the guitar neck and lable them!\\
\includegraphics[width=\textwidth,left]{plot_1}

$C^\prime$ is the middle $C$ which is the key in the middle of the piano keyboard. 
$C^{\prime \prime}$  is one octave higher and $C^{\prime \prime \prime}$ is the c two octaves higher.

\pagebreak
Training templates:\\
""" + reduce(
    lambda acc,el: acc+el,
    [
        r"\includegraphics[width=\textwidth,left]{plot_0}"
        +"\n"
        for i in range(9)
    ]
) + r"""
\pagebreak
\section*{Solution}
\includegraphics[width=\textwidth]{plot_2}
\end{flushleft}
"""
        res=make_pdf(
            txt,
            stem="Task"
        )
        self.assertEqual(res.returncode,0)


