vim.api.nvim_create_user_command("U", function()
    vim.cmd("AsyncRun! ~/projects/sound-on-keystroke/u.sh")
    -- write checkmark icon after the colon:
    vim.notify("Files copied! ✅", vim.log.levels.INFO, {})
end, {})

vim.api.nvim_create_user_command("K", function()
    vim.cmd("AsyncRun! ~/projects/sound-on-keystroke/kill.sh")
    -- write checkmark icon after the colon:
    vim.notify("Killed!", vim.log.levels.INFO, {})
end, {})
