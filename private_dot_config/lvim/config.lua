---- LunarVim config

-- Basic options
vim.opt.backup = false -- turns off backup file
vim.opt.clipboard = "unnamedplus" -- allows neovim to access the system clipboard
vim.opt.cmdheight = 1 -- number of screen lines to use for command-line
vim.opt.conceallevel = 1 -- concealed text is replaced with one charcter
vim.opt.fileencoding = "utf-8" -- the encoding written to a file
vim.opt.hlsearch = true -- highlight all matches on previous search pattern
vim.opt.incsearch = true -- incremental search
vim.opt.ignorecase = true -- ignore case in search patterns
vim.opt.mouse = "a" -- allow the mouse to be used in neovim
vim.opt.smartcase = true -- smart case
vim.opt.smartindent = true -- make indenting smarter again
vim.opt.splitbelow = true -- force all horizontal splits to go below current window
vim.opt.splitright = true -- force all vertical splits to go to the right of current window
vim.opt.swapfile = false -- turns off swapfile creation
vim.opt.termguicolors = true -- set term gui colors (most terminals support this)
vim.opt.undofile = true -- enable persistent undo
vim.opt.writebackup = false -- do not make backup before overwritting a file
vim.opt.expandtab = true -- convert tabs to spaces
vim.opt.shiftwidth = 4 -- the number of spaces inserted for each indentation
vim.opt.tabstop = 4 -- insert 4 spaces for a tab
vim.opt.number = true -- set numbered lines
vim.opt.relativenumber = true -- set relative numbered lines
vim.opt.signcolumn = "yes" -- always show the sign column, otherwise it would shift the text each time
vim.opt.wrap = false -- display lines as one long line
vim.opt.guifont = "Cascadia Code PL:h12" -- the font used in graphical neovim applications
vim.opt.listchars = { -- Set list chars
    eol = "↲",
    tab = "▷⋯",
    trail = "•",
    nbsp = "␣",
}
vim.opt.list = true
vim.opt.showbreak = "↳ " -- Show break for wrapped lines
vim.opt.formatoptions:append { "n", "1" }
vim.opt.formatoptions:remove { "r", "o" }
-- vim.g.python3_host_prog = "/usr/bin/python3"


-- normal mode keymaps
lvim.keys.normal_mode["<C-s>"] = ":w<CR>"
lvim.keys.normal_mode["<C-q>"] = ":q<CR>"
lvim.keys.normal_mode["<leader>."] = ":noh<CR>"
-- insert mode keymaps
lvim.keys.insert_mode["jk"] = "<Esc>"

-- plugins
lvim.plugins = {
  {"catppuccin/nvim"},
    {
      "folke/tokyonight.nvim",
      lazy = false,
      priority = 1000,
      opts = {},
    },
    {'NvChad/nvim-colorizer.lua'},
}

-- colorscheme
lvim.colorscheme = "tokyonight-night"
lvim.builtin.lualine.options.theme = "tokyonight"

-- colorizer
require 'colorizer'.setup()

---- python stuff (https://github.com/LunarVim/starter.lvim/blob/python-ide/config.lua)
-- setup formatting
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup { { name = "black" }, }
lvim.format_on_save.enabled = true
lvim.format_on_save.pattern = { "*.py" }

-- setup linting
local linters = require "lvim.lsp.null-ls.linters"
linters.setup { { command = "flake8", filetypes = { "python" } } }

