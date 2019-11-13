"""CPU functionality."""

import sys
LDI = 0b10000010   # 130 
PRN = 0b01000111   # 71
HLT = 0b00000001   # 1
LD = 0b010001010



class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0


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

    def ram_read(self, mar):
        """
        should accept the address to read and return the value stored there.
        """
        value = self.ram[mar]
        return value

    
    def raw_write(self, mdr, mar):
        """
        Should accept a value to write, and the address to write it to.
        """
        self.ram[mar] = mdr


    # def raw_ram_print(self):
    #     for instruction in self.ram:
    #         if instruction == self.HLT:
    #             return
    #         else:
    #             print(instruction)

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
    
    def hlt(self):
        '''
        halt the CPU and exit the emulator.
        '''
        pass

    def run(self):
        """Run the CPU."""
        while HLT != 0:
            address = self.ram_read(self.pc)
            print(address, self.pc)
            if address == HLT:
                break
            elif address == LDI:
                self.pc + 1
            elif address == PRN:
                self.pc += 1
            self.pc += 1
        # pass

