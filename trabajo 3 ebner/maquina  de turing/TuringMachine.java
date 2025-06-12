import javax.swing.*;

public class TuringMachine {
    private char[] tape;
    private int head;
    private String state;
    private final String[] finalStates = {"qf"};

    public TuringMachine(String input) {
        this.tape = input.toCharArray();
        this.head = 0;
        this.state = "q0";
    }

    private boolean isFinalState() {
        for (String fs : finalStates) {
            if (state.equals(fs)) return true;
        }
        return false;
    }

    private boolean step() {
        if (head >= tape.length) {
            char[] newTape = new char[tape.length + 1];
            System.arraycopy(tape, 0, newTape, 0, tape.length);
            newTape[tape.length] = '_';
            tape = newTape;
        } else if (head < 0) {
            char[] newTape = new char[tape.length + 1];
            System.arraycopy(tape, 0, newTape, 1, tape.length);
            newTape[0] = '_';
            tape = newTape;
            head = 0;
        }

        char symbol = tape[head];
        String key = state + symbol;

        switch (key) {
            case "q0a": tape[head] = '_'; head++; state = "q1"; return true;
            case "q0b": tape[head] = '_'; head++; state = "q2"; return true;
            case "q0_": tape[head] = '_'; head++; state = "qf"; return true;

            case "q1a": head++; state = "q1"; return true;
            case "q1b": head++; state = "q1"; return true;
            case "q1_": head--; state = "q3"; return true;
            case "q3a": tape[head] = '_'; head--; state = "q4"; return true;
            case "q3_": head++; state = "qf"; return true;

            case "q2a": head++; state = "q2"; return true;
            case "q2b": head++; state = "q2"; return true;
            case "q2_": head--; state = "q5"; return true;
            case "q5b": tape[head] = '_'; head--; state = "q4"; return true;
            case "q5_": head++; state = "qf"; return true;

            case "q4a": head--; state = "q4"; return true;
            case "q4b": head--; state = "q4"; return true;
            case "q4_": head++; state = "q0"; return true;
        }
        return false;
    }

    public boolean run() {
        while (!isFinalState()) {
            if (!step()) break;
        }
        return isFinalState();
    }

    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Ingrese una cadena con 'a' y 'b':");
        if (!input.matches("[ab]*")) {
            JOptionPane.showMessageDialog(null, "Solo se permiten las letras 'a' y 'b'");
            return;
        }

        TuringMachine tm = new TuringMachine(input);
        boolean result = tm.run();
        JOptionPane.showMessageDialog(null, result ? "Cadena aceptada (palíndromo)" : "Cadena rechazada");
    }
}