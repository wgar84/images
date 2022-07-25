FROM mpl_jupyter

ARG token

USER root

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

RUN python -m pip install git+https://wgar84:${token}@github.com/deltafolha/zeresima.git

USER jovyan