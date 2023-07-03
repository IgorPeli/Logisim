def assembly_to_binary(assembly_code):
  instruction_map = {
    "MOVE": "0000",
    "MOVE(X)": "0001",
    "ADD": "0010",
    "ADD(X)": "0011",
    "SUB": "0100",
    "SUB(X)": "0101",
    "OR": "0110",
    "OR(X)": "0111",
    "NOT": "1000",
    "NOT(X)": "1001",
    "SHF": "1010",
    "SHF(X)": "1011",
    "JPZ": "1100",
    "JPO": "1101",
    "GO": "1110",
    "STR": "1111",
    # Adicione outras instruções aqui
  }

  lines = assembly_code.split("\n")
  binary_code = []

  for line in lines:
    parts = line.strip().split()

    if not parts:
      continue

    instruction = parts[0]
    operands = parts[1:]

    if instruction not in instruction_map:
      raise ValueError("Instrução inválida: " + instruction)

    binary_instruction = instruction_map[instruction]
    binary_operands = []

    for operand in operands:
      if operand.isdigit():
        operand_decimal = int(operand)
      else:
        operand_decimal = int(operand, 16)

      operand_binary = bin(operand_decimal)[2:].zfill(4)
      binary_operands.append(operand_binary)

    binary_line = binary_instruction + " " + " ".join(binary_operands)
    binary_code.append(binary_line)

  return "\n".join(binary_code)


# Função para converter o binário para hexadecimal
def binary_to_hex(binary):
  hex_code = ""
  binary_parts = binary.split()

  for binary_num in binary_parts:
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num)[2:].upper()
    hex_code += hex_num

  return hex_code.strip()


# Solicita ao usuário a entrada do código assembly
print("Os números são em hexadecimais!!")
assembly_code = input("Digite o código assembly (Exemplo: MOVE A):  ")

print("Código Assembly:")
print(assembly_code)

binary_code = assembly_to_binary(assembly_code)
print("\nCódigo Binário:")
print(binary_code)

hex_code = binary_to_hex(binary_code)
print("\nCódigo Hexadecimal:")
print(hex_code)
