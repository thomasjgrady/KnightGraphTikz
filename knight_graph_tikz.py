import sys

def generate_graph(m, n):
    
    scale = 6/m

    tikz_code = '\\begin{tikzpicture}\n'

    for i in range(m):
        for j in range(n):
            tikz_code = tikz_code + f'\t\\node[shape=circle, draw=black, scale={scale}] ({i*n + j}) at ({j*scale},{i*scale}) {{}};\n'

    tikz_code = tikz_code + '\n'

    for i in range(m):
        for j in range(n):
            pos = [None] * 8
            pos[0] = (i+2, j-1)
            pos[1] = (i+2, j+1)
            pos[2] = (i-1, j+2)
            pos[3] = (i+1, j+2)
            pos[4] = (i-2, j-1)
            pos[5] = (i-2, j+1)
            pos[6] = (i-1, j-2)
            pos[7] = (i+1, j-2)

            node1_id = i*n + j
            
            for p in pos:
                if 0 <= p[0] < m and 0 <= p[1] < n:
                    node2_id = p[0]*n + p[1]
                    tikz_code = tikz_code + f'\t\\path [-] ({node1_id}) edge ({node2_id});\n'
    
    tikz_code = tikz_code + '\\end{tikzpicture}\n'
    
    fname = f'knights-tour-{m}-{n}.tex'
    with open(fname, 'w') as f:
        f.write(tikz_code)
    print(f'Tex code written to {fname}')

if __name__ == '__main__':

    if (len(sys.argv) != 3):
        print('Usage: python3 ./knight_graph_tikz_generator.py <m> <n>')
        sys.exit(1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])
    generate_graph(m, n)
