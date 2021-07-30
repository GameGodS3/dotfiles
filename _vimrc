" For Windows

syntax enable

" I prefer ZZ over escape for quitting from INSERT mode 
inoremap ZZ <Esc>
set wrap

" For moving lines up and down in V mode
vnoremap J :m '>+1<cr>gv=gv
vnoremap K :m '<-2<cr>gv=gv

" Color Scheme and line numbering
colorscheme monokai 
set number

" For setting 4 spaces when using <TAB>
set tabstop=4
set shiftwidth=4
set expandtab

" Vim Plug stuff

call plug#begin()

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'jiangmiao/auto-pairs'
Plug 'preservim/nerdtree'
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install()  }, 'for': ['markdown', 'vim-plug'] }
Plug 'dbeniamine/cheat.sh-vim'

call plug#end()

hi Pmenu ctermbg=05
hi Pmenu ctermfg=06

set backspace=indent,eol,start
