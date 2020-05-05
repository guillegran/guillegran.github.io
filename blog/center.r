#############
## CENTER TXT
center = function(x){
  if(out_type == 'latex' || out_type == 'beamer')
    paste0("\\begin{center}\n", x, "\n\\end{center}")
  else if(out_type == 'html')
    paste0("<center>\n", x, "\n</center>")
  else
    x
}
