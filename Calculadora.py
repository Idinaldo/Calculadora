from tkinter import *

preto = '#000000'
branco = '#ffffff'
laranja = '#cc7f04'
azul = '#38576b'
cinza = '#bdbbb9'


calculadora = Tk()

calculadora.title('Calculadora')
calculadora.geometry('279x283')
calculadora.resizable(width=0, height=0)

tela = Frame(calculadora, width=270, height=50, bg=cinza)
tela.place(x=0, y=0)

corpo = Frame(calculadora, width=270, height=233, bg=preto)
corpo.place(x=4, y=42)

mostrar = StringVar()

label = Label(tela, textvariable=mostrar, width=25, height=2, font='Ivy 12 bold', relief=FLAT, anchor='e',
              justify=RIGHT, bg=azul, fg=branco)
label.grid(row=0)

valores = ''


def MostrarValores(event):
    global valores
    global mostrar
    valores = valores + event
    mostrar.set(valores)


def calcular():
    try:
        global valores
        global mostrar
        valores = valores.replace(',', '.')
        valores = valores.replace('÷', '/')
        valores = valores.replace('^', '**')
        if '%' in valores:
            porcen = valores.find('%')
            primeira_parte = valores[0:porcen]
            segunda_parte = valores[(porcen+1):]
            valores = f'{primeira_parte} * {segunda_parte} / 100'
        if 'x' in valores:
            valores = valores.replace('x', '*')
            valores = ''
        if '*-' in valores:
            mostrar.set('Equação Inválida.')
            valores = ''
            limpar_tudo()
        if '*-' in valores:
            mostrar.set('Equação Inválida.')
            valores = ''
        resultado = eval(valores)
    except SyntaxError:
        mostrar.set('Equação Inválida.')
        valores = ''
    except ZeroDivisionError:
        mostrar.set('Impos. dividir por 0.')
        valores = ''
    except Exception:
        mostrar.set('Equação Inválida.')
        valores = ''
    else:
        mostrar.set(resultado)
        valores = ''



def limpar_ultimo_num():
    global valores
    global mostrar
    novos_valores = len(valores) - 1
    valores = valores[0:novos_valores]
    mostrar.set(valores)


def limpar_tudo():
    global mostrar
    global valores
    valores = ''
    mostrar.set('')


botao_C = Button(corpo, command=lambda: limpar_tudo(), text='c', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_C.grid(column=0, row=0)

botao_porcen = Button(corpo, command=lambda: MostrarValores('%'), text='%', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_porcen.grid(column=1, row=0)

botao_dividir = Button(corpo, command=lambda: MostrarValores('÷'), text='÷', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_dividir.grid(column=2, row=0)

botao_apagar = Button(corpo, command=limpar_ultimo_num, text='←', width=5, height=2, font='Ivy 10',bg=laranja, fg=branco, relief=RAISED, overrelief=RIDGE)
botao_apagar.grid(column=3, row=0)

botao_7 = Button(corpo, command=lambda: MostrarValores('7'), text='7', width=5, height=2, font='Ivy 10',relief=RAISED, overrelief=RIDGE)
botao_7.grid(column=0, row=1)

botao_8 = Button(corpo, command=lambda: MostrarValores('8'), text='8', width=5, height=2, font='Ivy 10',relief=RAISED, overrelief=RIDGE)
botao_8.grid(column=1, row=1)

botao_9 = Button(corpo, command=lambda: MostrarValores('9'), text='9', width=5, height=2, font='Ivy 10',relief=RAISED, overrelief=RIDGE)
botao_9.grid(column=2, row=1)

botao_vezes = Button(corpo, command=lambda: MostrarValores('x'), text='x', width=5, height=2, font='Ivy 10', bg=laranja, fg=branco, relief=RAISED, overrelief=RIDGE)
botao_vezes.grid(column=3, row=1)

botao_4 = Button(corpo, command=lambda: MostrarValores('4'), text='4', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_4.grid(column=0, row=2)

botao_5 = Button(corpo, command=lambda: MostrarValores('5'), text='5', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_5.grid(column=1, row=2)

botao_6 = Button(corpo, command=lambda: MostrarValores('6'), text='6', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_6.grid(column=2, row=2)

botao_menos = Button(corpo, command=lambda: MostrarValores('-'), text='-', width=5, height=2, font='Ivy 10', bg=laranja, fg=branco, relief=RAISED, overrelief=RIDGE)
botao_menos.grid(column=3, row=2)

botao_1 = Button(corpo, command=lambda: MostrarValores('1'), text='1', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_1.grid(column=0, row=3)

botao_2 = Button(corpo, command=lambda: MostrarValores('2'), text='2', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_2.grid(column=1, row=3)

botao_3 = Button(corpo, command=lambda: MostrarValores('3'), text='3', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_3.grid(column=2, row=3)

botao_mais = Button(corpo, command=lambda: MostrarValores('+'), text='+', width=5, height=2, font='Ivy 10', bg=laranja, fg=branco, relief=RAISED, overrelief=RIDGE)
botao_mais.grid(column=3, row=3)

botao_0 = Button(corpo, command=lambda: MostrarValores('0'), text='0', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_0.grid(column=0, row=4)

botao_virgula = Button(corpo, command=lambda: MostrarValores(','), text=',', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_virgula.grid(column=1, row=4)

botao_ajuda = Button(corpo, command=lambda: MostrarValores('^'), text='^', width=5, height=2, font='Ivy 10', relief=RAISED, overrelief=RIDGE)
botao_ajuda.grid(column=2, row=4)

botao_igual = Button(corpo, command=lambda: calcular(), text='=', width=5, height=2, font='Ivy 10', bg=laranja, fg=branco, relief=RAISED, overrelief=RIDGE)
botao_igual.grid(column=3, row=4)

calculadora.mainloop()

# código feito por Idinaldo
