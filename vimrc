syntax enable

" I prefer ZZ over escape for quitting from INSERT mode 
inoremap ZZ <Esc>
set wrap

" Color Scheme and line numbering
colorscheme codedark 
set number

" For setting 4 spaces when using <TAB>
set tabstop=4
set shiftwidth=4
set expandtab

" Vim Plug stuff

call plug#begin()

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'jiangmiao/auto-pairs'

call plug#end()
