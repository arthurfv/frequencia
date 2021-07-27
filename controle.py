from tkinter import *
import os
import banco



def gravarDados():
    if tb_nome.get() !="":
        vnome=tb_nome.get()
        vmatricula=tb_matricula.get()
        vturma=tb_turma.get()
        vdata=tb_data.get()
        vquery="INSERT INTO tb_alunos(a_nome, a_matricula, a_turma, a_data) VALUES ('" + vnome + "', '" + vmatricula +"', '"+ vturma +"', '"+ vdata +"' )"
        banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_matricula.delete(0,END)
        tb_turma.delete(0,END)
        tb_data.delete(0,END)
        print("Dados gravados")
        
    else:
            print("Error")
   

app=Tk()
app.title("Frequencia do Aluno")
app.geometry("250x290")
app.configure(background="#00FF00")

Label(app,text="Nome", background="#00FF00",foreground="#000",anchor=W).place(x=5,y=5,width=40,height=20)
tb_nome=Entry(app)
tb_nome.place(x=5,y=30,width=150,height=20)

Label(app,text="Matrícula", background="#00FF00",foreground="#000",anchor=W).place(x=5,y=65,width=55,height=20)
tb_matricula=Entry(app)
tb_matricula.place(x=5,y=90,width=100,height=20)

Label(app,text="Turma", background="#00FF00",foreground="#000",anchor=W).place(x=5,y=125,width=40,height=20)
tb_turma=Entry(app)
tb_turma.place(x=5,y=150,width=100,height=20)

Label(app,text="Data", background="#00FF00",foreground="#000",anchor=W).place(x=5,y=185,width=40,height=20)
tb_data=Entry(app)
tb_data.place(x=5,y=210,width=100,height=20)

Button(app,text="Enviar",command=gravarDados).place(x=5,y=260,width=80,height=20)

app.mainloop()