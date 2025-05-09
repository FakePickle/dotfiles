return {
    {
        "catgoose/nvim-colorizer.lua",
        event = "BufReadPre",
        opts = {
            filetypes = { "*" }, -- Enable for all filetypes
            user_default_options = {
                RGB = true,      -- Enable #RGB hex codes
                RRGGBB = true,   -- Enable #RRGGBB hex codes
                names = false,   -- Disable "Color names" like Blue or Red
                RRGGBBAA = true, -- Enable #RRGGBBAA hex codes
                rgb_fn = true,   -- Enable CSS rgb() and rgba() functions
                hsl_fn = true,   -- Enable CSS hsl() and hsla() functions
                css = true,      -- Enable all CSS features: rgb_fn, hsl_fn, names, etc.
                css_fn = true,   -- Enable all CSS *functions*: rgb_fn, hsl_fn
            },
        },
    },
}

