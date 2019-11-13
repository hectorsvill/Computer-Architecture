"""CPU functionality."""

#https://github.com/hectorsvill/Computer-Architecture/blob/master/LS8-spec.md

import sys

LDI = 0b10000010 # 120
PRN = 0b01000111  # 71
HLT = 0b00000001 # 1
MUL = 0b10100010 # 162 

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.dispatch_table = self.create_dispatch_table() # dispatch table
        self.halted = False
        self.ram = [0] * 256 # ram of 256 bytes
        self.reg = [0] * 8 # register
        self.pc = 0 # Program Counter, address of the currently executing instruction
        self.reg_a =  0 #  Memory Address Register, holds the memory address we're reading or writing
        self.reg_b = 0 # Memory Data Register, holds the value to write or the value just read
    def create_dispatch_table(self):
        '''
        Create a dispatch table for faster access
        '''
        dispatch_table = {
            LDI: self.ldi,
            PRN: self.prn,
            HLT: self.hlt,
            MUL: self.mul,
        }
        return dispatch_table
    def load(self):
        """Load a program into memory."""
        if len(sys.argv) != 2:
            print("usage: cpu.py filename")
            sys.exit()
        else:
            address = 0
            program_name = sys.argv[1]
            with open(program_name) as f:
                for line in f:
                    line = line.split("#")[0]
                    line = line.strip()
                    if line == '':
                        continue
                    val = int(line, 2)
                    self.ram[address] = val
                    address += 1
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')
        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()
    def ram_read(self, reg_a):
        """
        should accept the address to read and return the value stored there.
        """
        return self.ram[reg_a]
    def raw_write(self, reg_a, reg_b):
        """
        Should accept a value to write, and the address to write it to.
        """
        self.ram[reg_a] = reg_b
    def reg_write(self, reg_a, reg_b):
        '''
        should accept a memmory address and memory data to registor 
        '''
        self.reg[reg_a] = reg_b
    def register(self):
        '''
        Register data in next two memory addresses
        '''
        self.reg_a = self.ram[self.pc + 1]
        self.reg_b = self.ram[self.pc + 2]
    def ldi(self):
        '''
        load "immediate", store a value in a register, or "set this register to this value".
        '''
        self.reg_write(self.reg_a, self.reg_b)
        self.pc += 3
    def prn(self):
        '''
        a pseudo-instruction that prints the numeric value stored in a register.
        '''
        print(self.reg[self.reg_a])
        self.pc += 2
    def mul(self):
        '''
        Multiply the values in two registers together and store the result in registerA. Machine code:
        '''
        result = self.reg[self.reg_a] * self.reg[self.reg_b]
        self.reg_write(self.reg_a, result)
        self.pc += 3
    def hlt(self):
        '''
        halt the CPU and exit the emulator.
        '''
        self.halted = True
    def run(self):
        '''
        run cpu
        '''
        while not self.halted:
            instruction = self.ram_read(self.pc)
            self.register()
            self.dispatch_table[instruction]()
if __name__ == "__main__":
    cpu = CPU()
    cpu.load()
    cpu.run()
