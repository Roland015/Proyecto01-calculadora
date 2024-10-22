# INICIO CON LA IMPORTACION DE LA LIBRERIA
import tkinter as tk

# agregamos la clase calculadora
class Calculadora:
    def __init__(self, master) -> None:
        self.master = master
        master.title('Calculadora Basica')
        master.geometry('308x380+500+150')
        master.resizable(0,0)

        self.resultado = tk.StringVar()

        self.entrada = tk.Entry(master, textvariable=self.resultado, width=16, font=('Arial',24), bd=10, insertwidth=4, bg='powder blue', justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)

        # BOTONES
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        fila = 1
        col = 0
# APLICAMOS EL BUCLE FOR 
        for boton in botones:
            tk.Button(master, text=boton, padx=20, pady=20, font=('Arial', 16), command=lambda b=boton: self.click(b)).grid(row=fila, column=col)

            col += 1
            if col > 3:
                col = 0
                fila += 1

# AGREGANDO LA FUNCION CLICK
    def click(self, boton):
        if boton == 'C':
            self.resultado.set(" ")
        elif boton == '=':
            try:
                self.resultado.set(eval(self.resultado.get()))
            except Exception as e:
                self.resultado.set("Error")
        else:
            self.resultado.set(self.resultado.get() + boton)


if __name__ == "__main__":
    root = tk.Tk()
    Calculadora = Calculadora(root)
    root.mainloop()