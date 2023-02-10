import os
from time import sleep

def main():
    show = False

    spreadsheet_name = ''
    columnn_compare = ''

    while spreadsheet_name == '':    
        spreadsheet_name = input('|> Informe o nome Aba da Panilha para geração dos códigos: ')
   
    while columnn_compare == '':    
        columnn_compare = input('|> Informe a coluna e linha de comparação: ')
    
    in_show = input('|> Digite 1 para mostrar o resultado em tela: ')

    if in_show == '1':
        show = True

    printline('|> Gerando códigos')
    codes = generate_code(spreadsheet_name, line_first=6, line_end=90, column_init=6, column_quantity=40, columnn_compare=columnn_compare, _print=show) 

    filename = export_to_file(codes)
    
    print('')
    print(f'|> Arquivo gerado: {filename}')

def printline(text):
    print(text, sep=' ', end='', flush=True)

def loading():
    printline('.')
    sleep(0.03)

def generate_code(spreadsheet, line_first=1, line_end=10, column_init=1, column_quantity=10, column_jump=4, columnn_compare='B4', _print=False):

    formulas = []
    columns = generate_column_sheet()

    for row in range(line_first, line_end):
        jump = 0
        __text = ''

        for _ in range(1, column_quantity):
            __text += f'SE({spreadsheet}!{columns[column_init + jump]}{row}={columnn_compare}; CONCATENAR({spreadsheet}!{columns[column_init + jump -2]}{row}; " - "; {spreadsheet}!{columns[column_init + jump -2]}3);'
        
            jump += column_jump

        if _print:
            print(f'={__text} "")\n\n')

        formulas.append(f'={__text} "")')
        loading()

    return formulas
    
def export_to_file(data=[], break_line='\r\n\n', filename='codes_sheets'):
    file_path = ''

    if data:
        if not os.path.isdir('output'):
            os.makedirs('output')
            
        file_path = f'output/{filename}.txt'
        file = open(file_path,'w')
        file.write(break_line.join(data))
        file.close()

    return file_path
        
def generate_column_sheet():
    alfabeto = []
    c = 0
    d = 0
    for i in range(ord('A'), ord('Z')+1):
        alfabeto.insert(c, chr(i))
        for j in range(ord('A'), ord('Z')+1):
            d += 1
            alfabeto.insert(c+d, chr(i)+chr(j))
            # for k in range(ord('A'), ord('Z')+1):
            #     alfabeto.append(chr(i)+chr(j)+chr(k))
        c += 1
    return alfabeto

if __name__ == '__main__':
    main() 