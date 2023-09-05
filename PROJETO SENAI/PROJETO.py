from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import pandas as pd

CINZA = '#9c9c9c'
BRANCO = '#ffffff'
AZUL = '#4287f5'
DATAANO = str(date.today().year)
DATAMES = str(date.today().month)

if len(DATAMES) == 1:
    DATAMES = '0'+ DATAMES

def iconeJanela(janela):
    icon = PhotoImage(file='Caminhao.png', format='png')
    janela.iconphoto(False, icon)

def fotoLogo(tam_x, tam_y, pos_x, pos_y, janela):
    foto = Image.open("foto1.png")
    foto_resize = foto.resize([tam_x, tam_y])
    foto1 = ImageTk.PhotoImage(foto_resize)
    label1 = Label(janela, image=foto1)
    label1.image = foto1
    label1.place(x=pos_x, y=pos_y)

def Menu():

    def criaJanelaMenu():
        wdw.title('TRANSPORTADORA TRANSIPA')
        wdw.geometry('400x450')
        iconeJanela(wdw)
        wdw.resizable(False, False)
        wdw.configure(bg=BRANCO)

    def labelFuncionario():
        label2 = Label(wdw, text='FUNCIONÁRIOS: ', font='Bahnschrift 24', relief='solid')
        label2.place(y=25, x=135)

    def funcionarios():
        label3 = Button(wdw, text='Rogério', font='Bahnschrift 18', relief='solid', width='15', command=JanelaFunc1)
        label3.place(x=20, y=110)

        label3 = Button(wdw, text='Cláudio', font='Bahnschrift 18', relief='solid', width='15', command=JanelaFunc2)
        label3.place(x=20, y=200)

        label3 = Button(wdw, text='Márcia', font='Bahnschrift 18', relief='solid', width='15', command=JanelaFunc3)
        label3.place(x=20, y=290)

        label3 = Button(wdw, text='Luciana', font='Bahnschrift 18', relief='solid', width='15', command=JanelaFunc4)
        label3.place(x=20, y=380)

    criaJanelaMenu()
    fotoLogo(80, 80, 10, 10, wdw)
    labelFuncionario()
    funcionarios()

def criarJanelaFunc(janela, tmnho = '600x720'):
    janela.title('TRANSPORTADORA TRANSIPA')
    janela.geometry(tmnho)
    iconeJanela(janela)
    janela.resizable(False, False)
    janela.configure(bg=BRANCO)

def parteDeCima(janela, nome_empregado, veiculo, placa):
    def labelMercadorias(jnela):
        label1 = Label(jnela, text='Cadastro de Entregas', bg=CINZA, font='Bahnschrift 18', width='23', relief='solid')
        label1.place(x=250, y=30)

    def labelMesAno(jnela):
        global DATAMES

        label_mes = Label(jnela, text='Mês:', font='Bahnschrift 16', bg=BRANCO)
        label_mes.place(x=580, y=115)

        label_data_mes = Label(jnela, text=DATAMES, font='Bahnschrift 16 underline',underline=2, bg=BRANCO, fg=AZUL)
        label_data_mes.place(x=710, y=115)

        label_ano = Label(jnela, text='Ano:', font='Bahnschrift 16', bg=BRANCO)
        label_ano.place(x=580, y=155)

        label_data_ano = Label(jnela, text=DATAANO, font='Bahnschrift 16 underline',underline=4, bg=BRANCO, fg=AZUL)
        label_data_ano.place(x=690, y=155)

    def labelNomeEmpregado(jnela, nome):
        label_nome = Label(jnela, text='Nome do Empregado: ', font='Bahnschrift 16', bg=BRANCO)
        label_nome.place(x=5, y=90)

        label_texto_nome = Label(jnela, text=nome, font='Bahnschrift 16', bg=BRANCO, fg=AZUL)
        label_texto_nome.place(x=210, y=90)

    def labelTransporte(jnela, transporte):
        label_veiculo = Label(jnela, text='Veículo:', font='Bahnschrift 16', bg=BRANCO)
        label_veiculo.place(x=5, y=120)

        label_nome_veiculo = Label(jnela, text=transporte, font='Bahnschrift 16', bg=BRANCO, fg=AZUL)
        label_nome_veiculo.place(x=90, y=120)

        label_placa = Label(jnela, text='Placa:', font='Bahnschrift 16', bg=BRANCO)
        label_placa.place(x=5, y=150)

        label_valor_placa = Label(jnela, text=placa, font='Bahnschrift 16', bg=BRANCO, fg=AZUL)
        label_valor_placa.place(x=75, y=150)

    labelMercadorias(janela)
    labelNomeEmpregado(janela, nome_empregado)
    labelMesAno(janela)
    labelTransporte(janela,veiculo)

def JanelaFunc1():
    def tabela(janela):
        tbela = Label(janela, text=rogerio, relief='solid', font='Arial 14')
        tbela.place(x=10, y=200)
    rogerio = pd.read_excel('Rogerio.xlsx')
    rogerio = rogerio.to_string(index=False, col_space=20, justify='left')
    func1 = Toplevel(wdw)
    criarJanelaFunc(func1, tmnho='760x350')
    fotoLogo(80, 80, 20, 10, func1)
    parteDeCima(func1, 'Rogério Da Silva Júnior', veiculo='Caminhão 1', placa='QUA2-U33')
    tabela(func1)
    func1.mainloop()

def JanelaFunc2():
    def tabela(janela):
        tbela = Label(janela, text=claudio, relief='solid', font='Arial 14')
        tbela.place(x=10, y=200)
    claudio = pd.read_excel('Claudio.xlsx')
    claudio = claudio.to_string(index=False, col_space=20, justify='left')
    func2 = Toplevel(wdw)
    criarJanelaFunc(func2, tmnho='760x350')
    fotoLogo(80, 80, 20, 10, func2)
    parteDeCima(func2, 'Cláudio Ferreira Costa', veiculo='Caminhão 2', placa='RRT4-98N')
    tabela(func2)
    func2.mainloop()

def JanelaFunc3():
    def tabela(janela):
        tbela = Label(janela, text=marcia, relief='solid', font='Arial 14')
        tbela.place(x=10, y=200)
    marcia = pd.read_excel('Marcia.xlsx')
    marcia = marcia.to_string(index=False, col_space=20, justify='left')
    func3 = Toplevel(wdw)
    criarJanelaFunc(func3, tmnho='760x350')
    fotoLogo(80, 80, 20, 10, func3)
    parteDeCima(func3, 'Márcia Lopes Silva', veiculo='Caminhão 3', placa='T21O-YYU')
    tabela(func3)
    func3.mainloop()

def JanelaFunc4():
    def tabela(janela):
        tbela = Label(janela, text=luciana, relief='solid', font='Arial 14')
        tbela.place(x=10, y=200)
    luciana = pd.read_excel('Luciana.xlsx')
    luciana = luciana.to_string(index=False, col_space=20, justify='left')
    func4 = Toplevel(wdw)
    criarJanelaFunc(func4, tmnho='760x350')
    fotoLogo(80, 80, 20, 10, func4)
    parteDeCima(func4, 'Luciana Brito Marques', veiculo='Caminhão 2', placa='RRT4-98N')
    tabela(func4)
    func4.mainloop()

wdw = Tk()
Menu()
wdw.mainloop()
