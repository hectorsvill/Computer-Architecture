"""CPU functionality."""

#https://github.com/hectorsvill/Computer-Architecture/blob/master/LS8-spec.md

import sys
LDI = 130 # 0b10000010 
PRN = 71 # 0b01000111 
HLT = 1 # 0b00000001 
MUL = 162 # 10100010

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.halted = False
        self.ram = [0] * 256 # ram of 256 bytes
        self.reg = [0] * 8 # register
        self.pc = 0 # Program Counter, address of the currently executing instruction
        #self.reg_a =  0 #  Memory Address Register, holds the memory address we're reading or writing
        #self.reg_b = 0 # Memory Data Register, holds the value to write or the value just read
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
        #             print(val)
        # sys.exit()
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
    def hlt(self):
        '''
        halt the CPU and exit the emulator.
        '''
        self.halted = True
    def ldi(self, reg_a, reg_b):
        '''
        load "immediate", store a value in a register, or "set this register to this value".
        '''
        self.reg[reg_a] = reg_b
    def prn(self, reg_a):
        '''
        a pseudo-instruction that prints the numeric value stored in a register.
        '''
        value = self.reg[reg_a]
        print(value)
    def mul(self):
        '''
        Multiply the values in two registers together and store the result in registerA. Machine code:
        '''
        pass
    def run(self):
        '''
        run cpu
        '''
        # i = 0
        while not self.halted:
            instruction = self.ram_read(self.pc)
            reg_a = self.ram_read(self.pc + 1)
            reg_b = self.ram_read(self.pc + 2)
            
            # print(instruction)
            if instruction == HLT:
                self.hlt()
            elif instruction == LDI:
                self.ldi(reg_a, reg_b)
            elif instruction == PRN:
                self.prn(reg_a)
            else:
                pass
                # print(f"found nothing at: {instruction}")    
            
            self.pc += 1

            # if i == 14:
            #     break
            # i += 1

if __name__ == "__main__":
    cpu = CPU()
    cpu.load()
    cpu.run()
