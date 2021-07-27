from tkinter import *
import os

c=os.path.dirname(__file__)
nomeArquivo= c + "\\chamada.txt"

def gravarDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("Professor:%s" % vprofessor.get())
    arquivo.write("\nAluno....:%s" % valuno.get())
    arquivo.write("\nData.....:%s" % vdata.get())
    arquivo.write("\nSituação.:%s" % vsituacao.get())
    arquivo.write("\nObs......:%s" % vobs.get("1.0",END))
    arquivo.write("\n")
    arquivo.close()
program=Tk()

program.title("Validação")
program.geometry("500x350")
program.configure(background="#E0E0E0")

Label(program,text="Professor", background="#E0E0E0", foreground="#000", anchor=W).place(x=5, y=10)
vprofessor=Entry(program)
vprofessor.place(x=5,y=30, width=200, height=20)
Label(program,text="Aluno", background="#E0E0E0", foreground="#000", anchor=W).place(x=5, y=55)
valuno=Entry(program)
valuno.place(x=5,y=75, width=200, height=20)
Label(program,text="Data", background="#E0E0E0", foreground="#000", anchor=W).place(x=5, y=105)
vdata=Entry(program)
vdata.place(x=5,y=130, width=60, height=20)
Label(program,text="Situação", background="#E0E0E0", foreground="#000", anchor=W).place(x=5, y=160)
vsituacao=Entry(program)
vsituacao.place(x=5,y=185, width=60, height=20)
Label(program,text="Obs", background="#E0E0E0", foreground="#000", anchor=W).place(x=5, y=215)
vobs=Text(program)
vobs.place(x=5,y=240, width=250, height=50)

Button(program,text="Enviar",command=gravarDados).place(x=5,y=310,width=80,height=20)



program.mainloop()