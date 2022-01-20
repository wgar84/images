import os
import sys


def main():
    py_path = sys.argv[1]
    parts = py_path.split('/')
    py_name = parts[-1]
    nb_name = 'out/{}'.format(py_name.replace('.py', '.ipynb'))
    html_name = py_name.replace('.py', '.html')
    os.system('ipynb-py-convert {py} {nb}'.format(py=py_path, nb=nb_name))
    convert_command = (
        'jupyter nbconvert --to html --no-input --execute'
        ' --template mod --output {html} {nb}'
    )
    os.system(convert_command.format(html=html_name, nb=nb_name))
    os.system('rm {nb}'.format(nb=nb_name))


if __name__ == '__main__':
    main()
	
