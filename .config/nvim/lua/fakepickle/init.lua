require("fakepickle.set")
require("fakepickle.remap")
require("fakepickle.lazy-init")

vim.api.nvim_set_keymap('i', '(', '()<Left>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('i', '{', '{}<Left>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('i', '[', '[]<Left>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('i', '"', '""<Left>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('i', "'", "''<Left>", { noremap = true, silent = true })

vim.g.netrw_browse_split = 0
vim.g.netrw_banner = 0
vim.g.netrw_winsize = 25

local augroup = vim.api.nvim_create_augroup
local fakepickleGroup = augroup('fakepickleGroup', {})

local autocmd = vim.api.nvim_create_autocmd
local yank_group = augroup('HighlightYank', {})

function R(name)
    require("plenary.reload").reload_module(name)
end

vim.filetype.add({
    extension = {
        templ = 'templ',
    }
})

autocmd('TextYankPost', {
    group = yank_group,
    pattern = '*',
    callback = function()
        vim.highlight.on_yank({
            higroup = 'IncSearch',
            timeout = 40,
        })
    end,
})

autocmd({"BufWritePre"}, {
    group = fakepickleGroup,
    pattern = "*",
    command = [[%s/\s\+$//e]],
})

