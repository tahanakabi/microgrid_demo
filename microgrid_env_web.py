# Author: Taha Nakabi
from tcl_env_dqn_1 import MicroGridEnv
import numpy as np

RENDER_VALUES_list=['Energy Generated', 'Energy consumption' ,
                    'TCL SOCs', 'Outdoor temperatures (°C)' ,
                    'Price responsive Loads (kW)','Retail Sale prices (cents)',
                    'Battery SOC',
                    'Energy Sold','Energy purchased',
                    'Up regulation prices','Down-regulation Prices',
                    'Energy allocated to TCLs','Energy consumed by TCLs']
RENDER_VALUES_dict={}
def reset_dict():
    for key in RENDER_VALUES_list:
        RENDER_VALUES_dict[key]=[]

reset_dict()


class MicroGridEnvWeb(MicroGridEnv):

    def __init__(self,**kwargs):
        MicroGridEnv.__init__(self, **kwargs)

    def add_content(self, ax,i):
        ax.render_to_file('svgs/graph'+str(i)+'.svg')
        with open('svgs/graph'+str(i)+'.svg', "r") as f:
            rows = f.readlines()[1:]
        for row in rows:
            self.html_file.write(row)

    def add_graph(self,i):
        with open('svgs/graph'+str(i)+'.svg', "r") as f:
            rows = f.readlines()[1:]
        for row in rows:
            self.html_file.write(row)

    def render(self, R=0, **kwargs):
        MicroGridEnv.render(self,R=R,web=True)
        if self.time_step == self.iterations:
            self.html_file = open("app/templates/figure.html", 'w')
            self.html_file.write("{% extends \"base.html\" %}" + "\n" + "{% block content %}" + "\n")
            self.html_file.write("<h1>Day: {}</h1>".format(self.day))
            for i in range(1, 8):
                self.add_graph(i)
            self.html_file.write('<p>Profit: {} euros </p>'.format(100*R))
            self.html_file.write("\n <form action=\"\" method=\"post\" novalidate> \n" +
                                 "{{ form.hidden_tag() }} \n " +
                                 "<p>{{ form.next_day() }}</p>\n ")
            if self.day != self.day0:
                self.html_file.write("<p>{{ form.previous_day() }}</p>\n ")

            self.html_file.write(" </form>")
            self.html_file.write("{% endblock %}")
            self.html_file.close()
            #
