FROM python:3.10

# RUN apt-add-repostory ppa:ubuntugis/ppa && apt update
RUN apt update
RUN apt install -y --fix-missing gdal-bin libgdal-dev pandoc texlive-xetex graphviz-dev lzma-dev liblzma-dev p7zip-full

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY mod /usr/local/share/jupyter/nbconvert/templates/mod

RUN groupadd -g 1000 jovyan
RUN useradd -ms /bin/bash -u 1000 -g 1000 jovyan

#COPY bin/* /usr/local/bin/
COPY wait-for-it.sh /usr/local/bin

USER jovyan

WORKDIR /home/jovyan
RUN mkdir .config
RUN mkdir .config/gspread_pandas
COPY google_secret.json .config/gspread_pandas
#ENV PYTHONPATH "${PYTHONPATH}:/usr/local/bin"

WORKDIR /home/jovyan/app
ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/app"

RUN jupyter notebook --generate-config

RUN echo \
    "c.NotebookApp.token = '4fcbc72db3dadfc4585c374a5c83b566b9a86944b1489e79'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

RUN echo \
    "c.NotebookApp.password = u'sha1:0bff055a03ce:c09cde8bab532481515d631285948252f72e8cc5'" \
    >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# ENTRYPOINT [ "wait-for-it.sh", "driver:4444", "--", "/bin/sh",  "-c" ]
# CMD jupyter notebook --no-browser --ip=0.0.0.0
