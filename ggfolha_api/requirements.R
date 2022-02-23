install.packages(
     c(
	'extrafont'
#         #'languageserver',
#         #'devtools',
#         #'tidyverse',
#         # 'plumber'
#         #'IRkernel'
     ), 
     dependencies=TRUE,
     repos="https://cloud.r-project.org"
)

extrafont::font_import(prompt=FALSE)

token = scan(file='token', what='')
devtools::install_github('deltafolha/ggfolha', auth_token=token)
# devtools::install_local(path)

IRkernel::installspec()
