# install.packages(
#     c(
#         #'languageserver',
#         #'devtools',
#         #'tidyverse',
#         # 'plumber'
#         #'IRkernel'
#     ), 
#     dependencies=TRUE,
#     repos="https://cloud.r-project.org"
# )

token = scan(file='token', what='')
IRkernel::installspec()
devtools::install_github('deltafolha/ggfolha', auth_token=token)
# devtools::install_local(path)

