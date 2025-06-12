import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape, transitions, state, final_states):
        self.tape = list(tape)
        self.transitions = transitions
        self.state = state
        self.final_states = final_states
        self.head = 0

    def step(self):
        if self.head >= len(self.tape):
            self.tape.append('_')
        elif self.head < 0:
            self.tape.insert(0, '_')
            self.head = 0

        symbol = self.tape[self.head]
        key = (self.state, symbol)

        if key in self.transitions:
            new_symbol, direction, new_state = self.transitions[key]
            self.tape[self.head] = new_symbol
            self.state = new_state
            self.head += 1 if direction == 'R' else -1
        else:
            return False
        return True

    def run(self):
        while self.state not in self.final_states:
            if not self.step():
                break
        return self.state in self.final_states


def run_simulation():
    tape = entry.get()
    if any(c not in 'ab' for c in tape):
        messagebox.showerror("Error", "Solo se permiten las letras 'a' y 'b'")
        return

    tm = TuringMachine(
        tape=list(tape),
        transitions={
            ('q0', 'a'): ('_', 'R', 'q1'),
            ('q0', 'b'): ('_', 'R', 'q2'),
            ('q0', '_'): ('_', 'R', 'qf'),

            ('q1', 'a'): ('a', 'R', 'q1'),
            ('q1', 'b'): ('b', 'R', 'q1'),
            ('q1', '_'): ('_', 'L', 'q3'),
            ('q3', 'a'): ('_', 'L', 'q4'),  
            ('q3', '_'): ('_', 'R', 'qf'),  

            ('q2', 'a'): ('a', 'R', 'q2'),
            ('q2', 'b'): ('b', 'R', 'q2'),
            ('q2', '_'): ('_', 'L', 'q5'),
            ('q5', 'b'): ('_', 'L', 'q4'),
            ('q5', '_'): ('_', 'R', 'qf'),

            ('q4', 'a'): ('a', 'L', 'q4'),
            ('q4', 'b'): ('b', 'L', 'q4'),
            ('q4', '_'): ('_', 'R', 'q0'),
        },
        state='q0',
        final_states={'qf'}
    )

    result = tm.run()
    messagebox.showinfo("Resultado", "Cadena aceptada (palíndromo)" if result else "Cadena rechazada")


root = tk.Tk()
root.title("Máquina de Turing - Palíndromos con a y b")
tk.Label(root, text="Ingrese una cadena con 'a' y 'b':").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Ejecutar", command=run_simulation).pack()
root.mainloop()