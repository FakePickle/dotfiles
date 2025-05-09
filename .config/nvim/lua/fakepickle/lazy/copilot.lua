return {
    {
        "zbirenbaum/copilot.lua",
        event = "VimEnter",
        config = function()
            require("copilot").setup({
                suggestion = {
                    auto_trigger = true,
                    enabled = true,
                    hide_during_completion = true,
                },
                filetypes = {
                    markdown = true,
                    python = true,
                    rust = true,
                    lua = true,
                    tex = true,
                    c = true,
                    cpp = true,
                    go = true,
                    javascript = true,
                    typescript = true,
                    html = true,
                    css = true,
                    scss = true,
                    json = true,
                    yaml = true,
                    toml = true,
                    shell = true,
                },
                panel = { enabled = true },
            })
        end,
    }
}

