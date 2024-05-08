vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
	-- PACKER NVIM PLUGIN
	use 'wbthomason/packer.nvim'
	-- TELESCOPE PLUGIN
	use {
		'nvim-telescope/telescope.nvim', tag = '0.1.6',
		-- or                            , branch = '0.1.x',
		requires = { {'nvim-lua/plenary.nvim'} }
	}
	-- ROSE PINE PLUGIN
	use ({
		"rose-pine/neovim",
		as = "rose-pine",
		config = function()
			vim.cmd('colorscheme rose-pine')
		end
	})
	-- TREESITTER PLUGIN
	use('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
	use('nvim-treesitter/playground')
	-- HARPOON PLUGIN
	use('theprimeagen/harpoon')
	-- UNDOTREE PLUGIN
	use('mbbill/undotree')
	-- FUGITIVE PLUGIN
	use('tpope/vim-fugitive')
	-- LSP PLUGIN
	use {
		'VonHeikemen/lsp-zero.nvim',
		requires = {
			{'neovim/nvim-lspconfig'},
			{'williamboman/mason.nvim'},
			{'williamboman/mason-lspconfig.nvim'},
			{'hrsh7th/nvim-cmp'},
			{'hrsh7th/cmp-buffer'},
			{'hrsh7th/cmp-path'},
			{'saadparwaiz1/cmp_luasnip'},
			{'hrsh7th/cmp-nvim-lsp'},
			{'hrsh7th/cmp-nvim-lua'},
			{'L3MON4D3/LuaSnip'},
			{'rafamadriz/friendly-snippets'},
		}
	}
    -- COPILOT PLUGIN
    use('github/copilot.vim')
end)
