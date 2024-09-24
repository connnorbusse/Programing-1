import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.ForeColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(142, 65)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(172, 65)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._button1.Location = System.Drawing.Point(50, 213)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._button2.Location = System.Drawing.Point(232, 213)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self._button3.Location = System.Drawing.Point(405, 213)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Highlight
        self.ClientSize = System.Drawing.Size(499, 290)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Sehcule 2"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text =" 1st Auto,2nd ELA,3rd Math,4th science,5th Woodworking,6th Matels,7th History,8th Programing"

    def Button2Click(self, sender, e):
        self._label1.Text =""

    def Button3Click(self, sender, e):
        Application.Exit()