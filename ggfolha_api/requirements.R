install.packages(
    c(
        'languageserver',
        'devtools',
        'tidyverse',
        'rplumber',
        'IRkernel'
    ), 
    dependencies=TRUE,
    repos="https://cloud.r-project.org"
)

IRkernel::installspec()
devtools::build('ggfolha/')