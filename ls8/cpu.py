"""CPU functionality."""

#https://github.com/hectorsvill/Computer-Architecture/blob/master/LS8-spec.md

import sys
LDI = 0b10000010   # 130 
PRN = 0b01000111   # 71
HLT = 0b00000001   # 1

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.run = True
        self.ram = [0] * 256 # ram of 256 bytes
        self.reg = [0] * 8 # register
        self.pc = 0 # Program Counter, address of the currently executing instruction
        self.reg_a =  0 #  Memory Address Register, holds the memory address we're reading or writing
        self.reg_b = 0 # Memory Data Register, holds the value to write or the value just read
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
            sys.exit(0)
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

    def run(self): 
        print("run")

    # def run(self):
        # '''
        # Run the CPU.
        # '''
        print("here")
        # while self.run:
        #     address = self.ram_read(self.pc)
        #     print(address, self.pc)
        #     if address == HLT:
        #         print("htl")
        #         break
        #     elif address == LDI:
        #         print("ldi")
        #         self.pc + 1
        #     elif address == PRN:
        #         print("prn")
        #         self.pc += 1
        #     self.pc += 1

    def hlt(self):
        '''
        halt the CPU and exit the emulator.
        '''
        self.run = False

    def ldi(self):
        '''
        load "immediate", store a value in a register, or "set this register to this value".
        '''
        pass

    def prn(self):
        '''
        a pseudo-instruction that prints the numeric value stored in a register.
        '''
        pass


cpu = CPU()
cpu.load()
cpu.run()
print("here")