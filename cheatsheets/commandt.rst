==========
Command T
==========

Bring up the Command-T file window by typing:::

    <Leader>t          "command t [dictation]"
    <Leader>b          "command t buffer [dictation]"
    n/a                "command t [tags | tag | jump]"

Type letters in the prompt to narrow down the selection, showing only the
files whose paths contain those letters in the specified order. Letters do not
need to appear consecutively in a path in order for it to be classified as a
match.

The following mappings are active when the prompt has focus:::

    <BS>       
    <Del>       
    <Left> / <C-h>
    <Right> / <C-l>
    <C-a>       move the cursor to the start (left)
    <C-e>       move the cursor to the end (right)
    <C-u>       clear the contents of the prompt
    <Tab>       change focus to the file listing

The following mappings are active when the file listing has focus:::

    <Tab>       change focus to the prompt

The following mappings are active when either the prompt or the file listing
has focus:::

    <CR>        open the selected file
    <C-CR>      open the selected file in a new split
    <C-s>       open the selected file in a new split
    <C-v>       open the selected file in a new vsplit
    <C-t>       open the selected file in a new tab
    <C-j>       select next file in the file listing
    <C-n>       select next file in the file listing
    <Down>      select next file in the file listing
    <C-k>       select previous file in the file listing
    <C-p>       select previous file in the file listing
    <Up>        select previous file in the file listing
    <C-f>       flush the cache
    <C-c>       cancel (dismisses file listing)
    <Esc>       cancel (dismisses file listing)

