from matplotlib.patches import Polygon,Circle
from functools import reduce

class Neck():
    def __init__(self,
            x_maxs, 
            x_maxs_neck, 
            sf,
            y_range, 
            transform=lambda x,y: (y,x) ,
            cr=0.2
        ):
        self.x_maxs=x_maxs 
        self.x_maxs_neck=x_maxs_neck 
        self.sf=sf
        self.y_range=y_range 
        self.transform=transform
        self.cr=cr
        
        x_mins=[x*sf for x in x_maxs]
        x_mins_neck=[x*sf for x in x_maxs_neck]
        y_min,y_max=y_range
        
        self.x_min=min(x_mins)
        self.x_max=max(x_maxs)
        self.y_min=y_min
        self.y_max=y_max
        self.ys=[y(i,y_min,y_max) for i in range(24)]
        self.x_mins=x_mins
        self.x_mins_neck=x_mins_neck



    def plot_neck(self,ax):
        x_mins      = self.x_mins 
        x_maxs      = self.x_maxs 
        x_maxs_neck = self.x_maxs_neck 
        sf          = self.sf
        x_maxs_neck = self.x_maxs_neck
        x_mins_neck = self.x_mins_neck
        y_min = self.y_min
        y_max = self.y_max
        
        transform=self.transform
        cr=self.cr
        
        # plot neck
        neck=Polygon(
            [
                transform(x_mins_neck[0],y_min),
                transform(x_maxs_neck[0],y_max),
                transform(x_maxs_neck[1],y_max),
                transform(x_mins_neck[1],y_min)
            ],
            color="brown",
            alpha=0.1
            )
        ax.add_patch(neck)
        # plot strings
        for i,(x_min,x_max) in enumerate(zip(x_mins,x_maxs)):
            x_ext_min,y_ext_min=transform(x_min,y_min)
            x_ext_max,y_ext_max=transform(x_max,y_max)
            ax.plot(
                [x_ext_min,x_ext_max],
                [y_ext_min,y_ext_max],
                color="black",
                alpha=0.5,
                linewidth=i+1
            )
        
        # plot frets
        for i in range(25):
            y_i=y(i,y_min,y_max)
            x_min=x(y_i,x_mins_neck[0],x_maxs_neck[0],y_min,y_max)
            x_max=x(y_i,x_mins_neck[1],x_maxs_neck[1],y_min,y_max)
            
            x_ext_1,y_ext_1 = transform(x_min,y_i)
            x_ext_2,y_ext_2=transform(x_max,y_i)
            ax.plot(
                [x_ext_1,x_ext_2],
                [y_ext_1,y_ext_2],
                alpha=0.5,
                color="black",
            )
        
            # fret numbers (right)
            x_ext,y_ext=transform(x_max,y_i)
            ax.text(
                    #x_max,
                    #y_i,
                x_ext,
                y_ext,
                str(i),
                verticalalignment="center",
                fontsize="large"
            )
        
        # plot dots
        sdf=[3,5,7,9,15,17,21]
        for f in sdf:
            circle=Circle(self.external_fret_coords(f,0,0),radius=cr,color="gray")
            ax.add_patch(circle)
        
        # plot double dots
        ddf=[12,24]
        for f in ddf:
            x_center,y_center=self.internal_fret_coords(f,0,0)
            lc=Circle(
                transform(x_center+1.1*cr,y_center),
                radius=cr,
                color="gray"
            )
            rc=Circle(
                transform(x_center-1.1*cr,y_center),
                radius=cr,
                color="gray"
            )
            ax.add_patch(lc)
            ax.add_patch(rc)

    def plot_note(
        self,
        ax,
        f,
        st,
        txt,
        label=None,
        color="blue",
        alpha=0.5
    ):
        x_i,y_i=self.internal_stringed_fret_coords(st,f)#, x_mins, x_maxs, y_min, y_max)
        x_e,y_e=self.transform(x_i,y_i)
        cr=self.cr
        circle=Circle(
            (x_e,y_e),
            radius=4*cr,
            color=color,
            label=label,
            zorder=3,
            alpha=1,
        )
        ax.add_patch(circle)
        ax.text(
            x_e,
            y_e,
            txt,
            fontsize=14,
            zorder=4,
            verticalalignment="center",
            horizontalalignment="center"
        )

    def plot_single_string_scale(
        self,
        ax,
	    mi,
	    names,
	    sp,
	    st,
	    label=None,
	    color="blue",
        alpha=1,
    ):
        for i,f in enumerate(intervals2frets(mi,sp)):
            self.plot_note(
                ax=ax,
                f=f,
                st=st,
                txt=names[i],
                label=label if i==0 else None,
                color=color,
                alpha=alpha,
            )

    def internal_stringed_fret_coords(
        self,
        string,
        fret
    ):
        x_max=self.x_maxs[string]
        x_min=self.x_mins[string]
        return self.internal_fret_coords(fret,x_min,x_max)#,y_min,y_max)

    def internal_fret_coords(self,fret,x_min,x_max):#,y_min,y_max):
        y_min=self.y_min
        y_max=self.y_max
        y_f=y(fret,y_min,y_max)
        y_fl=y(fret-1,y_min,y_max)
        y_center=(y_f+y_fl)/2
        xi=x(y_center,x_min,x_max,y_min,y_max)
        return (xi,y_center)

    def external_fret_coords(self,fret,x_min,x_max):#,y_min,y_max):
        xi,y_center=self.internal_fret_coords(fret,x_min,x_max)
        x_ext,y_ext = self.transform(xi,y_center)
        return (x_ext,y_ext)

def lambda_fret(fret,lambda_max=1):
    root=0.25**(1.0/24) 
    return root**fret

def y(fret,y_min=0,y_max=1):
    delta_y=y_max-y_min
    return y_max-lambda_fret(fret,y_max-y_min)*delta_y

def x(y,x_min,x_max,y_min=0,y_max=1):
    delta_x_max=x_max-x_min
    delta_y_max=y_max-y_min
    delta_y=y-y_min
    return x_min+delta_x_max/delta_y_max * delta_y



    
def sequence2series(seq):
    '''return the series (the sequence of partial sums) of a sequence'''
    def add(acc,el):
        series,running_total = acc
        nrt=running_total+el
        return ([*series,nrt],nrt)

    acc_start=([],0)
    final_tup= reduce(
        add,
        seq,
        acc_start
    )
    #discard running total
    return final_tup[0]
        
    
def intervals2frets(mi,start_fret):
    return [ start_fret +d for d in  sequence2series(mi) ]




